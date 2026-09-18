param(
	[ValidateSet('shell', 'api', 'list', 'add', 'delete')]
	[string]$Mode = 'shell',
	[string]$Message,
	[long]$Id
)

$ErrorActionPreference = 'Stop'
$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$workspaceRoot = Split-Path -Parent (Split-Path -Parent $scriptRoot)
$repoRoot = Join-Path (Join-Path $workspaceRoot 'languages') 'java'
Write-Host "Opening Java workspace: $repoRoot"
Write-Host "Target container: java-test"
Write-Host "Database: mysql.database.svc.cluster.local:3306"
if (Test-Path $repoRoot) {
	$repoRoot = (Resolve-Path $repoRoot).Path
	Set-Location $repoRoot
} else {
	throw "Path not found: $repoRoot"
}

$kubectlCmd = Get-Command kubectl -ErrorAction SilentlyContinue
if (-not $kubectlCmd) {
	throw 'kubectl not found. Install kubectl or add it to PATH.'
}
$kubectl = $kubectlCmd.Source

if ($Mode -eq 'shell') {
	$shellCmd = "export PS1='[java-test] \\u@\\h:\\w\\$ '; exec bash --noprofile --norc -i"
	Write-Host "Launching container shell with prompt marker [java-test]..."
	& $kubectl exec -it -n apps deploy/java-test -- bash --noprofile --norc -lc $shellCmd
	if ($LASTEXITCODE -ne 0) { throw 'Failed to launch java shell in pod.' }
	exit $LASTEXITCODE
}

$pod = (& $kubectl get pods -n apps -l app=java-test --field-selector=status.phase=Running -o jsonpath='{.items[0].metadata.name}').Trim()
if (-not $pod) {
	throw 'No running java-test pod found in namespace apps.'
}

Write-Host "Syncing Java project into pod $pod..."
& $kubectl exec -n apps $pod -- bash -lc "rm -rf /tmp/java-app"
if ($LASTEXITCODE -ne 0) { throw 'Failed to prepare /tmp/java-app in pod.' }
& $kubectl cp . "apps/${pod}:/tmp/java-app"
if ($LASTEXITCODE -ne 0) { throw 'Failed to copy Java project into pod.' }

switch ($Mode) {
	'api' {
		Write-Host 'Starting REST API on port 8080 inside java-test pod...'
		Write-Host 'Use port-forward in another terminal: kubectl port-forward -n apps deploy/java-test 8080:8080'
		& $kubectl exec -it -n apps $pod -- bash -lc "cd /tmp/java-app && mvn -q spring-boot:run"
		if ($LASTEXITCODE -ne 0) { throw 'Failed to start Java REST API.' }
	}
	'list' {
		& $kubectl exec -n apps $pod -- bash -lc "cd /tmp/java-app && mvn -q -DskipTests -Dexec.args='list --spring.main.web-application-type=none' compile exec:java"
		if ($LASTEXITCODE -ne 0) { throw 'Failed to run Java list command.' }
	}
	'add' {
		if (-not $Message) {
			$Message = "Hello from launcher at $(Get-Date -Format o)"
		}
		& $kubectl exec -n apps $pod -- env CLI_MESSAGE="$Message" bash -lc "cd /tmp/java-app && mvn -q -DskipTests -Dexec.args='add --spring.main.web-application-type=none' compile exec:java"
		if ($LASTEXITCODE -ne 0) { throw 'Failed to run Java add command.' }
	}
	'delete' {
		if (-not $Id) {
			throw 'delete mode requires -Id <messageId>'
		}
		& $kubectl exec -n apps $pod -- env CLI_ID="$Id" bash -lc "cd /tmp/java-app && mvn -q -DskipTests -Dexec.args='delete --spring.main.web-application-type=none' compile exec:java"
		if ($LASTEXITCODE -ne 0) { throw 'Failed to run Java delete command.' }
	}
}

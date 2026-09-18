$ErrorActionPreference = 'Stop'
$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$workspaceRoot = Split-Path -Parent (Split-Path -Parent $scriptRoot)
$repoRoot = Join-Path (Join-Path $workspaceRoot 'languages') 'php'
Write-Host "Opening PHP workspace: $repoRoot"
Write-Host "Target container: php-test"
Write-Host "Database: mysql.database.svc.cluster.local:3306"
if (Test-Path $repoRoot) { Set-Location $repoRoot } else { Write-Warning "Path not found: $repoRoot" }

$shellCmd = "export PS1='[php-test] \\u@\\h:\\w\\$ '; exec bash --noprofile --norc -i"
Write-Host "Launching container shell with prompt marker [php-test]..."
& kubectl exec -it -n apps deploy/php-test -- bash --noprofile --norc -lc $shellCmd

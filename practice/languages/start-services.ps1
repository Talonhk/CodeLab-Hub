param(
    [ValidateSet('up', 'status', 'restart')]
    [string]$Action = 'up',
    [string]$Context = 'kind-fedora-lab',
    [string]$RootPassword = 'rootpass123!',
    [string]$AppDatabase = 'appdb',
    [string]$AppUser = 'appuser',
    [string]$AppPassword = 'apppass123!'
)

$ErrorActionPreference = 'Stop'

function Get-HelmCommand {
    $defaultHelm = 'C:\Users\_\bin\helm.exe'
    if (Test-Path $defaultHelm) {
        return $defaultHelm
    }

    $helmCmd = Get-Command helm -ErrorAction SilentlyContinue
    if ($helmCmd) {
        return $helmCmd.Source
    }

    throw 'Helm not found. Install Helm or add it to PATH.'
}

$kubectlCmd = Get-Command kubectl -ErrorAction SilentlyContinue
if (-not $kubectlCmd) {
    throw 'kubectl not found. Install kubectl or add it to PATH.'
}
$kubectl = $kubectlCmd.Source
$helm = Get-HelmCommand

$repoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$chartPath = Join-Path $repoRoot 'devops\zarf-testing\helm\coding-lab'

if (-not (Test-Path $chartPath)) {
    throw "Coding-lab chart not found: $chartPath"
}

Write-Host "Using kubectl: $kubectl"
Write-Host "Using helm: $helm"
Write-Host "Target context: $Context"

$availableContexts = & $kubectl config get-contexts -o name
if ($availableContexts -notcontains $Context) {
    throw "Context '$Context' not found. Available contexts: $($availableContexts -join ', ')"
}

& $kubectl config use-context $Context | Out-Null

if ($Action -eq 'status') {
    & $kubectl get ns
    & $kubectl get deploy,statefulset,svc -A
    & $helm list -A
    exit 0
}

foreach ($ns in @('database', 'apps', 'tools')) {
    & $kubectl create namespace $ns --dry-run=client -o yaml | & $kubectl apply -f - | Out-Null
}

foreach ($ns in @('database', 'apps')) {
    & $kubectl -n $ns create secret generic mysql-credentials `
        --from-literal=root-password=$RootPassword `
        --from-literal=app-database=$AppDatabase `
        --from-literal=app-user=$AppUser `
        --from-literal=app-password=$AppPassword `
        --dry-run=client -o yaml | & $kubectl apply -f - | Out-Null
}

& $helm upgrade --install coding-lab $chartPath --set createNamespaces=false

if ($Action -eq 'restart') {
    $restartDeployments = @(
        'apps/python-test',
        'apps/node-test',
        'apps/go-test',
        'apps/php-test',
        'apps/java-test',
        'apps/cpp-test',
        'tools/workspace-launcher'
    )

    foreach ($item in $restartDeployments) {
        $parts = $item.Split('/')
        & $kubectl -n $parts[0] rollout restart "deploy/$($parts[1])" | Out-Null
    }
    & $kubectl -n database rollout restart statefulset/mysql | Out-Null
}

& $kubectl -n database rollout status statefulset/mysql --timeout=300s
foreach ($name in @('python-test', 'node-test', 'go-test', 'php-test', 'java-test', 'cpp-test')) {
    & $kubectl -n apps rollout status "deploy/$name" --timeout=300s
}
& $kubectl -n tools rollout status deploy/workspace-launcher --timeout=300s

Write-Host ''
Write-Host 'Coding-lab services are ready.'
& $kubectl get deploy,statefulset,svc -A

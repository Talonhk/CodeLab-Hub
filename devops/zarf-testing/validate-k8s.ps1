$ErrorActionPreference = 'Stop'

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$k8sDir = Join-Path $scriptRoot 'k8s'

if (-not (Test-Path $k8sDir)) {
    throw "Kubernetes manifest directory not found: $k8sDir"
}

$kubectlCmd = Get-Command kubectl -ErrorAction SilentlyContinue
if (-not $kubectlCmd) {
    throw 'kubectl not found. Install kubectl or add it to PATH.'
}
$kubectl = $kubectlCmd.Source
Write-Host "Using kubectl: $kubectl"

$yamlFiles = Get-ChildItem -Path $k8sDir -Recurse -File | Where-Object { $_.Extension -in '.yaml', '.yml' } | Sort-Object FullName
if (-not $yamlFiles) {
    throw "No YAML files found under: $k8sDir"
}

Write-Host 'Validating Kubernetes manifests (client dry-run)...'
foreach ($file in $yamlFiles) {
    Write-Host "- $($file.FullName)"
    & $kubectl apply --dry-run=client --validate=true -f $file.FullName | Out-Host
}

Write-Host '---'
Write-Host 'All manifest files validated successfully.'

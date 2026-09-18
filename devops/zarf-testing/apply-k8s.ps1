param(
    [switch]$SkipValidation,
    [switch]$SkipRolloutCheck
)

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

function Invoke-Kubectl {
    param(
        [string[]]$CmdArgs,
        [switch]$AllowBoundPvcImmutable
    )

    $previousEap = $ErrorActionPreference
    $ErrorActionPreference = 'Continue'
    $output = & $kubectl @CmdArgs 2>&1
    $exitCode = $LASTEXITCODE
    $ErrorActionPreference = $previousEap
    $output | Out-Host

    if ($exitCode -ne 0) {
        if ($AllowBoundPvcImmutable -and ($output -match 'PersistentVolumeClaim.+is invalid: spec: Forbidden: spec is immutable after creation')) {
            Write-Warning 'Ignoring known bound-PVC immutability warning during apply.'
            return
        }
        throw "kubectl failed: kubectl $($CmdArgs -join ' ')"
    }
}

$yamlFiles = Get-ChildItem -Path $k8sDir -Recurse -File |
    Where-Object { $_.Extension -in '.yaml', '.yml' } |
    Sort-Object FullName

if (-not $yamlFiles) {
    throw "No YAML files found under: $k8sDir"
}

if (-not $SkipValidation) {
    Write-Host 'Validating manifests (client dry-run) before apply...'
    foreach ($file in $yamlFiles) {
        Write-Host "- Validate $($file.Name)"
        Invoke-Kubectl -CmdArgs @('apply', '--dry-run=client', '--validate=true', '-f', $file.FullName)
    }
    Write-Host 'Validation passed.'
} else {
    Write-Host 'Skipping validation by request.'
}

# Apply in deterministic order to reduce dependency surprises.
$applyOrder = @(
    'namespaces.yaml',
    'workspace-map.yaml',
    'mysql.yaml',
    'language-apps.yaml'
)

Write-Host 'Applying manifests to cluster...'
foreach ($name in $applyOrder) {
    $target = Join-Path $k8sDir $name
    if (Test-Path $target) {
        Write-Host "- Apply $name"
        if ($name -eq 'mysql.yaml') {
            Invoke-Kubectl -CmdArgs @('apply', '-f', $target) -AllowBoundPvcImmutable
        } else {
            Invoke-Kubectl -CmdArgs @('apply', '-f', $target)
        }
    }
}

if (-not $SkipRolloutCheck) {
    Write-Host 'Checking rollout status for app deployments...'
    $deployments = @(
        @{ Name = 'python-test'; Namespace = 'apps' },
        @{ Name = 'node-test'; Namespace = 'apps' },
        @{ Name = 'go-test'; Namespace = 'apps' },
        @{ Name = 'php-test'; Namespace = 'apps' },
        @{ Name = 'java-test'; Namespace = 'apps' },
        @{ Name = 'cpp-test'; Namespace = 'apps' },
        @{ Name = 'workspace-launcher'; Namespace = 'tools' }
    )
    foreach ($dep in $deployments) {
        Write-Host "- Rollout $($dep.Name) [$($dep.Namespace)]"
        Invoke-Kubectl -CmdArgs @('rollout', 'status', "deployment/$($dep.Name)", '-n', $dep.Namespace, '--timeout=240s')
    }
}

Write-Host '---'
    Invoke-Kubectl -CmdArgs @('get', 'deploy', '-n', 'apps', '-o', 'wide')
Write-Host '---'
    Invoke-Kubectl -CmdArgs @('get', 'pods', '-n', 'apps', '-o', 'wide')

Write-Host 'Apply complete.'

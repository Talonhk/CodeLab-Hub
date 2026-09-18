param(
    [switch]$SkipReapplyCurrentManifests
)

$ErrorActionPreference = 'Stop'

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$psExe = if (Get-Command pwsh -ErrorAction SilentlyContinue) { 'pwsh' } else { 'powershell' }

$kubectl = $null
$preferredKubectl = "$HOME\bin\kubectl.exe"
if (Test-Path $preferredKubectl) {
    $kubectl = $preferredKubectl
} else {
    $kubectlCmd = Get-Command kubectl -ErrorAction SilentlyContinue
    if ($kubectlCmd) {
        $kubectl = $kubectlCmd.Source
    }
}

if (-not $kubectl) {
    throw 'kubectl not found. Install kubectl or add it to PATH.'
}

Write-Host "Using kubectl: $kubectl"
$backupRoot = 'C:\Users\_\coding-lab-backups'

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
            Write-Warning 'Ignoring known bound-PVC immutability warning during restore apply.'
            return
        }
        throw "kubectl failed: kubectl $($CmdArgs -join ' ')"
    }
}

if (-not (Test-Path $backupRoot)) {
    throw "Backup root not found: $backupRoot"
}

$latest = Get-ChildItem $backupRoot | Where-Object { $_.PSIsContainer } | Sort-Object Name -Descending | Select-Object -First 1

if (-not $latest) {
    throw 'No backup snapshot found.'
}

$backupPath = $latest.FullName
Write-Host "Restoring from snapshot: $backupPath"

$files = @(
    'namespaces.yaml',
    'persistentvolumeclaims.yaml',
    'configmaps.yaml',
    'statefulsets.yaml',
    'deployments.yaml',
    'services.yaml',
    'all-resources.yaml'
)

foreach ($file in $files) {
    $full = Join-Path $backupPath $file
    if (Test-Path $full) {
        Write-Host "Applying $file"
        if ($file -eq 'persistentvolumeclaims.yaml' -or $file -eq 'all-resources.yaml') {
            Invoke-Kubectl -CmdArgs @('apply', '-f', $full) -AllowBoundPvcImmutable
        } else {
            Invoke-Kubectl -CmdArgs @('apply', '-f', $full)
        }
    }
}

if (-not $SkipReapplyCurrentManifests) {
    $applyScript = Join-Path $scriptRoot 'apply-k8s.ps1'
    if (Test-Path $applyScript) {
        Write-Host '---'
        Write-Host 'Re-applying current lab manifests to include latest changes...'
        & $psExe -ExecutionPolicy Bypass -File $applyScript
    } else {
        Write-Warning "apply-k8s.ps1 not found at $applyScript; skipping current manifest reapply."
    }
}

Write-Host '---'
Invoke-Kubectl -CmdArgs @('get', 'pods', '-A', '-o', 'wide')
Write-Host '---'
Invoke-Kubectl -CmdArgs @('get', 'nodes', '-o', 'wide')

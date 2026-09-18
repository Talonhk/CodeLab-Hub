param(
    [Parameter(Mandatory = $true, Position = 0)]
    [ValidateSet('validate', 'apply', 'restore', 'status', 'java-api')]
    [string]$Action,

    [int]$LocalPort = 8080,

    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$PassthroughArgs
)

$ErrorActionPreference = 'Stop'

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$validateScript = Join-Path $scriptRoot 'validate-k8s.ps1'
$applyScript = Join-Path $scriptRoot 'apply-k8s.ps1'
$restoreScript = Join-Path $scriptRoot 'restore-lab.ps1'
$javaLauncher = Join-Path $scriptRoot 'launchers\java.ps1'
$psExe = if (Get-Command pwsh -ErrorAction SilentlyContinue) { 'pwsh' } else { 'powershell' }

function Invoke-LabScript {
    param(
        [string]$ScriptPath,
        [string[]]$Args
    )

    if (-not (Test-Path $ScriptPath)) {
        throw "Required script not found: $ScriptPath"
    }

    & $psExe -NoProfile -ExecutionPolicy Bypass -File $ScriptPath @Args
    $exitCode = $LASTEXITCODE
    if ($exitCode -ne 0) {
        throw "Script failed ($exitCode): $ScriptPath"
    }
}

switch ($Action) {
    'validate' {
        Write-Host 'Running manifest validation...'
        Invoke-LabScript -ScriptPath $validateScript -Args $PassthroughArgs
    }
    'apply' {
        Write-Host 'Running safe apply (validate -> apply -> rollout checks)...'
        Invoke-LabScript -ScriptPath $applyScript -Args $PassthroughArgs
    }
    'restore' {
        Write-Host 'Running restore workflow...'
        Invoke-LabScript -ScriptPath $restoreScript -Args $PassthroughArgs
    }
    'status' {
        $kubectlCmd = Get-Command kubectl -ErrorAction SilentlyContinue
        if (-not $kubectlCmd) {
            throw 'kubectl not found. Install kubectl or add it to PATH.'
        }
        $kubectl = $kubectlCmd.Source
        Write-Host "Using kubectl: $kubectl"
        & $kubectl get nodes -o wide
        & $kubectl get deploy -n apps -o wide
        & $kubectl get deploy -n tools -o wide
        & $kubectl get pods -n apps -o wide
        & $kubectl get pods -n tools -o wide
    }
    'java-api' {
        if (-not (Test-Path $javaLauncher)) {
            throw "Java launcher not found: $javaLauncher"
        }

        Write-Host 'Starting Java API in a new PowerShell window...'
        Start-Process -FilePath $psExe -ArgumentList @(
            '-NoProfile',
            '-ExecutionPolicy',
            'Bypass',
            '-File',
            $javaLauncher,
            '-Mode',
            'api'
        ) | Out-Null

        Start-Sleep -Seconds 3

        Write-Host "Starting port-forward in a new PowerShell window on localhost:$LocalPort -> java-test:8080..."
        Start-Process -FilePath $psExe -ArgumentList @(
            '-NoProfile',
            '-ExecutionPolicy',
            'Bypass',
            '-Command',
            "kubectl port-forward -n apps deploy/java-test $LocalPort`:8080"
        ) | Out-Null

        Start-Sleep -Seconds 2
        $url = "http://localhost:$LocalPort/api/messages"
        Write-Host "Opening: $url"
        Start-Process $url | Out-Null
        Write-Host 'Java API quick-start launched. Keep both spawned PowerShell windows open.'
    }
}

Write-Host 'safe-k8s completed successfully.'

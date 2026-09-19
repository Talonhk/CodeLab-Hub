param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$Language,

    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$LauncherArgs
)

$ErrorActionPreference = 'Stop'
$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$workspaceRoot = Split-Path -Parent (Split-Path -Parent $scriptRoot)
$launcherDir = Join-Path $workspaceRoot 'devops\zarf-testing\launchers'

if (-not (Test-Path $launcherDir)) {
    throw "Launcher directory not found: $launcherDir"
}

$normalized = $Language.Trim().ToLowerInvariant()

switch ($normalized) {
    'python'     { $launcher = 'python.ps1' }
    'py'         { $launcher = 'python.ps1' }
    'javascript' { $launcher = 'javascript.ps1' }
    'js'         { $launcher = 'javascript.ps1' }
    'node'       { $launcher = 'javascript.ps1' }
    'go'         { $launcher = 'go.ps1' }
    'php'        { $launcher = 'php.ps1' }
    'java'       { $launcher = 'java.ps1' }
    'cpp'        { $launcher = 'cpp.ps1' }
    'c++'        { $launcher = 'cpp.ps1' }
    default {
        throw "Unknown language '$Language'. Use: python, javascript, go, php, java, cpp"
    }
}

$launcherPath = Join-Path $launcherDir $launcher
if (-not (Test-Path $launcherPath)) {
    throw "Launcher not found: $launcherPath"
}

Write-Host "Opening language: $Language"
Write-Host "Using launcher: $launcherPath"

$psExe = if (Get-Command pwsh -ErrorAction SilentlyContinue) { 'pwsh' } else { 'powershell' }
& $psExe -ExecutionPolicy Bypass -File $launcherPath @LauncherArgs
$exitCode = $LASTEXITCODE
if ($exitCode -ne 0) {
    throw "Launcher failed with exit code $exitCode"
}

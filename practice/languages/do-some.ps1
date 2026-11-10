param(
    [ValidateSet('python', 'javascript', 'go', 'php', 'java', 'cpp')]
    [string]$Language,

    [ValidateSet('up', 'status', 'restart')]
    [string]$Action = 'up',

    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$LauncherArgs
)

$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$servicesScript = Join-Path $repoRoot 'practice\languages\start-services.ps1'
$launcherScript = Join-Path $repoRoot 'devops\zarf-testing\open-language.ps1'

if ($Action -eq 'status') {
    & $servicesScript -Action status
    exit 0
}

if (-not $Language) {
    throw "Language is required for action '$Action'. Example: .\do-some.ps1 java"
}

& $servicesScript -Action $Action
& $launcherScript $Language @LauncherArgs

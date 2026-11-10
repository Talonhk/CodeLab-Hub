param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$LauncherArgs
)

$ErrorActionPreference = 'Stop'
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..\..')).Path
$servicesScript = Join-Path $repoRoot 'practice\languages\start-services.ps1'
$launcherScript = Join-Path $repoRoot 'devops\zarf-testing\open-language.ps1'

& $servicesScript -Action up
& $launcherScript cpp @LauncherArgs

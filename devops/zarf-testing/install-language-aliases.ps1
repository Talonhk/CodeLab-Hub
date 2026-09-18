$ErrorActionPreference = 'Stop'

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$entryScript = Join-Path $scriptRoot 'open-language.ps1'

if (-not (Test-Path $entryScript)) {
    throw "Entry script not found: $entryScript"
}

if (-not (Test-Path $PROFILE)) {
    $profileDir = Split-Path -Parent $PROFILE
    if (-not (Test-Path $profileDir)) {
        New-Item -ItemType Directory -Path $profileDir -Force | Out-Null
    }
    New-Item -ItemType File -Path $PROFILE -Force | Out-Null
}

$markerStart = '# >>> coding-lab language aliases >>>'
$markerEnd = '# <<< coding-lab language aliases <<<'

$psExe = if (Get-Command pwsh -ErrorAction SilentlyContinue) { 'pwsh' } else { 'powershell' }

$aliasBlock = @"
$markerStart
`$codingLabEntry = '$entryScript'
function python { & $psExe -ExecutionPolicy Bypass -File `$codingLabEntry python @args }
function javascript { & $psExe -ExecutionPolicy Bypass -File `$codingLabEntry javascript @args }
function go { & $psExe -ExecutionPolicy Bypass -File `$codingLabEntry go @args }
function php { & $psExe -ExecutionPolicy Bypass -File `$codingLabEntry php @args }
function java { & $psExe -ExecutionPolicy Bypass -File `$codingLabEntry java @args }
function cpp { & $psExe -ExecutionPolicy Bypass -File `$codingLabEntry cpp @args }
$markerEnd
"@

$current = Get-Content -Path $PROFILE -Raw
if ($current -match [regex]::Escape($markerStart)) {
    $pattern = [regex]::Escape($markerStart) + '[\s\S]*?' + [regex]::Escape($markerEnd)
    $updated = [regex]::Replace($current, $pattern, [System.Text.RegularExpressions.MatchEvaluator]{ param($m) $aliasBlock })
    Set-Content -Path $PROFILE -Value $updated -NoNewline
} else {
    if ($current -and -not $current.EndsWith("`n")) {
        $current += "`r`n"
    }
    Set-Content -Path $PROFILE -Value ($current + $aliasBlock) -NoNewline
}

Write-Host "Language aliases installed in: $PROFILE"
Write-Host "Open a new PowerShell terminal, then type: python | javascript | go | php | java | cpp"

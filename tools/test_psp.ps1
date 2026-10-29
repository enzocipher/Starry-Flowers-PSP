param(
    [Parameter(Mandatory = $true)][string]$Emulator,
    [string]$Python = 'python',
    [ValidateSet('performance', 'full')][string]$Mode = 'performance',
    [ValidateSet('vulkan', 'opengl')][string]$Backend = 'vulkan',
    [int]$Resolution = 1,
    [int]$TimeoutSeconds = 180
)
$ErrorActionPreference = 'Stop'
$taskRoot = Split-Path -Parent $PSScriptRoot
$taskSource = (Resolve-Path -LiteralPath $Emulator).Path
$taskRuntime = Join-Path $taskRoot "psp/test-emulator/runs/$Backend"
$taskExe = Join-Path $taskRuntime 'PPSSPPWindows64.exe'
New-Item -ItemType Directory -Path $taskRuntime -Force | Out-Null
Copy-Item -LiteralPath $taskSource -Destination $taskExe -Force
if (-not (Test-Path -LiteralPath (Join-Path $taskRuntime 'assets'))) {
    Copy-Item -LiteralPath (Join-Path (Split-Path -Parent $taskSource) 'assets') -Destination $taskRuntime -Recurse
}
$taskSystem = Join-Path $taskRuntime 'memstick/PSP/SYSTEM'
New-Item -ItemType Directory -Path $taskSystem -Force | Out-Null
$taskBackendId = if ($Backend -eq 'vulkan') { 3 } else { 0 }
@"
[General]
FirstRun = False
AutoRun = True
PauseOnLostFocus = False
PauseWhenMinimized = False
CheckForNewVersion = False
Enable Logging = True
[Graphics]
GraphicsBackend = $taskBackendId
InternalResolution = $Resolution
FrameSkip = 0
AutoFrameSkip = False
[SystemParam]
PSPModel = 0
[CPU]
CPUSpeed = 0
"@ | Set-Content -LiteralPath (Join-Path $taskSystem 'ppsspp.ini') -Encoding utf8

Push-Location $taskRoot
$taskProcess = $null
try {
    [string[]]$taskPackageArgs = if ($Mode -eq 'performance') { @('--performance-audit') } else { @('--audit') }
    & $Python tools/package_psp.py @taskPackageArgs
    if ($LASTEXITCODE -ne 0) { throw 'Audit packaging failed.' }
    $taskIso = Join-Path $taskRoot 'psp/dist/StarryFlowers-audit.iso'
    $taskSave = Join-Path $taskRuntime 'memstick/PSP/SAVEDATA/STARRYFLOWERS'
    $taskResultName = if ($Mode -eq 'performance') { 'PERF.JSON' } else { 'AUDIT.JSON' }
    $taskResult = Join-Path $taskSave $taskResultName
    $taskStarted = Get-Date
    $taskProcess = Start-Process -FilePath $taskExe -WorkingDirectory $taskRuntime -WindowStyle Hidden -PassThru -ArgumentList @('--windowed', '--escape-exit', ('"' + $taskIso + '"'), ('--log="' + (Join-Path $taskRuntime 'audit.log') + '"'))
    Write-Output "Testing $Mode with $Backend, ${Resolution}x resolution, PSP-1000 / 32 MiB."
    while (((Get-Date) - $taskStarted).TotalSeconds -lt $TimeoutSeconds) {
        # Native save replacement briefly moves the previous file to .BAK.
        # Read metadata once: Test-Path followed by Get-Item races that rename.
        $taskResultInfo = Get-Item -LiteralPath $taskResult -ErrorAction SilentlyContinue
        if ($taskResultInfo -and $taskResultInfo.LastWriteTime -ge $taskStarted) {
            $taskJson = Get-Content -LiteralPath $taskResult -Raw | ConvertFrom-Json
            if ($Mode -eq 'full' -and -not $taskJson.passed) { throw 'Native audit reported failure.' }
            if ($Mode -eq 'performance' -and $taskJson.navigation.menu_return.returns -ne 12) { throw 'Missing menu-return regression results.' }
            $taskJson | ConvertTo-Json -Depth 10 | Set-Content -LiteralPath (Join-Path $taskRoot "psp/dist/$Mode-$Backend-${Resolution}x.json") -Encoding utf8
            Write-Output "Passed: $taskResult"
            exit 0
        }
        Start-Sleep -Milliseconds 500
    }
    throw "No fresh audit result within $TimeoutSeconds seconds. See $taskRuntime/audit.log and native screenshots in $taskSave."
} finally {
    if ($taskProcess -and -not $taskProcess.HasExited) { Stop-Process -Id $taskProcess.Id -ErrorAction SilentlyContinue }
    Pop-Location
}

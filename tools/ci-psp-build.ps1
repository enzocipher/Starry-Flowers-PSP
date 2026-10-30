param([string]$Python = 'python')
$ErrorActionPreference = 'Stop'
$taskRoot = Split-Path -Parent $PSScriptRoot
Push-Location $taskRoot
try {
    # Use only tracked assets, the same build entry point, and the pinned toolchain.
    & ./tools/build_psp.ps1 -Python $Python
    & $Python tools/verify_psp_native.py
    if ($LASTEXITCODE -ne 0) { throw 'Native PSP package verification failed.' }
    & $Python tools/package_psp_release.py
    if ($LASTEXITCODE -ne 0) { throw 'PSP release packaging failed.' }
} finally {
    Pop-Location
}

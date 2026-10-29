$ErrorActionPreference = 'Stop'
$taskRoot = Split-Path -Parent $PSScriptRoot
$taskStorySource = Join-Path $taskRoot 'story.json'
$taskPspStory = Join-Path $taskRoot 'psp/story.json'
$taskToolchain = 'nightly-2026-10-05-x86_64-pc-windows-gnu'

if (-not (Test-Path -LiteralPath $taskStorySource -PathType Leaf)) {
    throw 'The tracked root story.json is required for the PSP CI build.'
}

# psp/story.json is ignored and normally generated from local original assets.
# CI stages the repository's real compiled story so this build needs no assets.
$null = Get-Content -LiteralPath $taskStorySource -Raw | ConvertFrom-Json
Copy-Item -LiteralPath $taskStorySource -Destination $taskPspStory -Force

Push-Location (Join-Path $taskRoot 'psp')
try {
    & cargo "+$taskToolchain" psp --release --locked '-Zbuild-std=core,alloc,compiler_builtins,panic_unwind'
    if ($LASTEXITCODE -ne 0) { throw 'PSP compilation failed.' }
} finally {
    Pop-Location
}

$taskPrx = Join-Path $taskRoot 'psp/target/mipsel-sony-psp/release/starryflowers-psp.prx'
if (-not (Test-Path -LiteralPath $taskPrx -PathType Leaf)) {
    throw "PSP build completed without the expected executable: $taskPrx"
}
Write-Output "Built PSP executable: $taskPrx"

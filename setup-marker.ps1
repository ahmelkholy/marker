<#
    setup-marker-readme.ps1  (v2 - July 2025)
    -------------------------------------------------
    Creates either
      • a stand-alone lightweight clone in $TargetPath   OR
      • a sparse submodule under third_party/marker
    that tracks only README.md from datalab-to/marker (branch = master).

    Usage examples
    --------------
    .\setup-marker-readme.ps1
    .\setup-marker-readme.ps1 -TargetPath "D:\Repos\marker-readme"
    .\setup-marker-readme.ps1 -Submodule
#>

[CmdletBinding()]
param (
    [string]$TargetPath     = "$PSScriptRoot\marker-readme",
    [switch]$Submodule,
    [string]$ParentRepoPath = (Get-Location)
)

function Test-GitVersion {
    $raw = (& git --version) -replace 'git version ', ''   # e.g. 2.50.0.windows.1
    # Keep only first three numeric components: 2.50.0
    $trimmed = ($raw -split '\.')[0..2] -join '.'
    if ([version]$trimmed -lt [version]'2.34.0') {
        throw "Git ≥ 2.34 required; found $raw"
    }
}

Write-Host "`n=== Checking Git version ==="
Test-GitVersion
Write-Host "✔ Git version OK`n"

if (-not $Submodule) {
    # ------------------------------------------------------------------
    # OPTION A – stand-alone minimal clone
    # ------------------------------------------------------------------
    Write-Host "=== Creating fresh sparse-clone of README.md ==="

    if (Test-Path $TargetPath) {
        $backup = "$TargetPath.bak_$(Get-Date -Format 'yyyyMMdd_HHmmss')"
        Write-Host "Target path exists – backing up to $backup"
        Rename-Item $TargetPath $backup
    }

    git clone --depth 1 --filter=blob:none `
              https://github.com/datalab-to/marker.git `
              $TargetPath               | Write-Host

    Set-Location $TargetPath
    git sparse-checkout init               | Write-Host   # pattern-mode (non-cone)
    git sparse-checkout set README.md      | Write-Host

    Write-Host "`n🎉  Done!  Your slim clone lives in $TargetPath"
    Write-Host "    To pull the latest README later:"
    Write-Host "        git -C $TargetPath pull`n"
}
else {
    # ------------------------------------------------------------------
    # OPTION B – sparse submodule inside an existing repo
    # ------------------------------------------------------------------
    Write-Host "=== Adding sparse submodule that tracks only README.md ==="

    if (-not (Test-Path $ParentRepoPath)) {
        throw "Parent repo path '$ParentRepoPath' not found"
    }
    Set-Location $ParentRepoPath

    git submodule add https://github.com/datalab-to/marker.git third_party/marker `
        | Write-Host

    Push-Location third_party/marker
    git sparse-checkout init           | Write-Host
    git sparse-checkout set README.md  | Write-Host
    Pop-Location

    git add .gitmodules third_party/marker
    git commit -m "Add marker/README.md as sparse submodule"

    Write-Host "`n🎉  Submodule ready!"
    Write-Host "    To refresh later:"
    Write-Host "        git submodule update --remote --depth 1 third_party/marker`n"
}
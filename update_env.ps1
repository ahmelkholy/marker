<#
.SYNOPSIS
    Automated .env updater for Marker, MarkerPDF, and MarkItDown packages
.DESCRIPTION
    This script updates .env files with latest package versions and API endpoints
    Activates virtual environment, checks for updates, and syncs configuration
.PARAMETER VenvPath
    Path to virtual environment (default: .\.venv)
.PARAMETER EnvFile
    Path to .env file (default: .\.env)
#>

param(
    [string]$VenvPath = ".\.venv",
    [string]$EnvFile = ".\.env"
)

$ErrorActionPreference = "Stop"
$WarningPreference = "Continue"

# Colors for output
$script:Colors = @{
    Success = "Green"
    Warning = "Yellow"
    Error = "Red"
    Info = "Cyan"
}

function Write-Log {
    param(
        [string]$Message,
        [ValidateSet("Success", "Warning", "Error", "Info")]
        [string]$Level = "Info"
    )
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$timestamp] [$Level] $Message" -ForegroundColor $script:Colors[$Level]
}

function Test-VenvActivation {
    param([string]$VenvPath)
    
    if (-not (Test-Path -Path $VenvPath)) {
        Write-Log "Virtual environment not found at $VenvPath" -Level Error
        return $false
    }
    
    $activateScript = Join-Path -Path $VenvPath -ChildPath "Scripts\Activate.ps1"
    if (-not (Test-Path -Path $activateScript)) {
        Write-Log "Activation script not found at $activateScript" -Level Error
        return $false
    }
    
    return $true
}

function Get-PackageVersions {
    param(
        [array]$PackageNames = @("marker-pdf", "markitdown", "python-dotenv")
    )
    
    Write-Log "Fetching package versions from pip..." -Level Info
    $versions = @{}
    
    foreach ($package in $PackageNames) {
        try {
            $output = & pip show $package 2>&1
            if ($LASTEXITCODE -eq 0) {
                $versionLine = $output | Where-Object { $_ -match "^Version:" }
                if ($versionLine -match "Version:\s+(.+)$") {
                    $versions[$package] = $matches[1]
                    Write-Log "Found $package version: $($matches[1])" -Level Success
                }
            } else {
                Write-Log "Package $package not found in environment" -Level Warning
            }
        }
        catch {
            Write-Log "Error retrieving $package version: $_" -Level Warning
        }
    }
    
    return $versions
}

function New-EnvTemplate {
    param(
        [hashtable]$Versions
    )
    
    $template = @"
# Marker PDF Configuration
# Generated: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")

# Package Versions
MARKER_PDF_VERSION=$(if ($Versions['marker-pdf']) { $Versions['marker-pdf'] } else { 'N/A' })
MARKITDOWN_VERSION=$(if ($Versions['markitdown']) { $Versions['markitdown'] } else { 'N/A' })
PYTHON_DOTENV_VERSION=$(if ($Versions['python-dotenv']) { $Versions['python-dotenv'] } else { 'N/A' })

# API Configuration
# Add your API keys and endpoints below
ANTHROPIC_API_KEY=
OPENAI_API_KEY=
GOOGLE_API_KEY=

# Output Configuration
OUTPUT_DIR=./OutputPdf
LOG_LEVEL=INFO

# Processing Configuration
ENABLE_OCR=true
ENABLE_MATH=true
BATCH_SIZE=10

# Virtual Environment
VENV_PATH=$VenvPath

# Last Updated
LAST_UPDATED=$(Get-Date -Format "yyyy-MM-dd HH:mm:ss")
"@
    
    return $template
}

function Merge-EnvFiles {
    param(
        [string]$EnvPath,
        [string]$NewTemplate
    )
    
    $mergedContent = @{}
    
    # Parse existing .env if it exists
    if (Test-Path -Path $EnvPath) {
        Write-Log "Parsing existing .env file..." -Level Info
        $content = Get-Content -Path $EnvPath
        foreach ($line in $content) {
            if ($line -match "^\s*#" -or [string]::IsNullOrWhiteSpace($line)) {
                continue
            }
            if ($line -match "^([^=]+)=(.*)$") {
                $key = $matches[1]
                $value = $matches[2]
                $mergedContent[$key] = $value
            }
        }
    }
    
    # Parse new template
    $templateLines = $NewTemplate -split "`n"
    foreach ($line in $templateLines) {
        if ($line -match "^([^=]+)=(.*)$") {
            $key = $matches[1]
            $value = $matches[2]
            # Only add if key doesn't exist (preserve existing values)
            if (-not $mergedContent.ContainsKey($key)) {
                $mergedContent[$key] = $value
            } else {
                # Update version and timestamp keys
                if ($key -match "VERSION|UPDATED") {
                    $mergedContent[$key] = $value
                }
            }
        }
    }
    
    # Build final content
    $output = @"
# Marker PDF Configuration
# Generated: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")
# This file was auto-updated. Preserve your custom values above the package versions section.

"@
    
    foreach ($key in ($mergedContent.Keys | Sort-Object)) {
        $output += "$key=$($mergedContent[$key])`n"
    }
    
    return $output
}

function Backup-EnvFile {
    param([string]$EnvPath)
    
    if (Test-Path -Path $EnvPath) {
        $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
        $backupPath = "$EnvPath.backup_$timestamp"
        Copy-Item -Path $EnvPath -Destination $backupPath
        Write-Log "Backup created: $backupPath" -Level Success
        return $backupPath
    }
    return $null
}

function Update-PipPackages {
    param(
        [array]$PackageNames = @("marker-pdf", "markitdown", "python-dotenv")
    )
    
    Write-Log "Checking for package updates..." -Level Info
    
    foreach ($package in $PackageNames) {
        try {
            Write-Log "Updating $package..." -Level Info
            & pip install --upgrade $package -q 2>&1 | Out-Null
            if ($LASTEXITCODE -eq 0) {
                Write-Log "$package updated successfully" -Level Success
            } else {
                Write-Log "Error updating $package" -Level Warning
            }
        }
        catch {
            Write-Log "Error updating $($package): $($_.Exception.Message)" -Level Warning
        }
    }
}

function Main {
    Write-Log "Starting .env auto-update process..." -Level Info
    Write-Log "VenvPath: $VenvPath | EnvFile: $EnvFile" -Level Info
    
    # Test venv
    if (-not (Test-VenvActivation -VenvPath $VenvPath)) {
        Write-Log "Failed to activate virtual environment" -Level Error
        exit 1
    }
    
    # Activate venv
    $activateScript = Join-Path -Path $VenvPath -ChildPath "Scripts\Activate.ps1"
    Write-Log "Activating virtual environment..." -Level Info
    & $activateScript
    
    # Update packages
    Update-PipPackages
    
    # Get versions
    $versions = Get-PackageVersions
    
    # Backup existing .env
    if (Test-Path -Path $EnvFile) {
        $backup = Backup-EnvFile -EnvPath $EnvFile
    }
    
    # Create template
    $template = New-EnvTemplate -Versions $versions
    
    # Merge with existing
    $merged = Merge-EnvFiles -EnvPath $EnvFile -NewTemplate $template
    
    # Write .env
    Set-Content -Path $EnvFile -Value $merged -Encoding UTF8
    Write-Log ".env file updated successfully: $EnvFile" -Level Success
    
    Write-Log "Update process completed!" -Level Success
    Write-Log "Versions updated:`n$($versions | ConvertTo-Json)" -Level Info
}

try {
    Main
}
catch {
    Write-Log "Unexpected error: $_" -Level Error
    exit 1
}

# .env Auto-Update Script

## Overview
`update_env.ps1` is a PowerShell automation script that manages and updates `.env` files for Marker PDF, MarkItDown, and related Python packages. It intelligently updates package versions, preserves existing configurations, and maintains backups.

## Features
✅ **Automatic Package Updates** - Updates marker-pdf, markitdown, and python-dotenv to latest versions  
✅ **Version Tracking** - Stores package versions in .env for reference  
✅ **Smart Merging** - Preserves custom API keys and settings while updating package info  
✅ **Automatic Backups** - Creates timestamped backups before updates  
✅ **Virtual Environment Support** - Works seamlessly with .venv  
✅ **Colored Logging** - Clear, timestamped status messages  
✅ **Error Handling** - Graceful error recovery with detailed logging  

## Prerequisites
- PowerShell 5.0 or higher
- Python virtual environment at `.\.venv`
- pip package manager available in venv

## Installation

### Option 1: Direct Usage
```powershell
cd D:\Proj.Other\Marker_pdf
powershell -ExecutionPolicy Bypass -File .\update_env.ps1
```

### Option 2: With Custom Paths
```powershell
powershell -ExecutionPolicy Bypass -File .\update_env.ps1 `
    -VenvPath ".\.venv" `
    -EnvFile ".\.env"
```

## Usage

### Basic Usage
```powershell
.\update_env.ps1
```

### Custom Virtual Environment Path
```powershell
.\update_env.ps1 -VenvPath "C:\path\to\.venv"
```

### Custom .env File Location
```powershell
.\update_env.ps1 -EnvFile "C:\path\to\.env"
```

### Both Custom Paths
```powershell
.\update_env.ps1 -VenvPath "C:\custom\.venv" -EnvFile "C:\custom\.env"
```

## What the Script Does

1. **Validates Environment** - Checks if virtual environment exists and is accessible
2. **Activates venv** - Loads the Python virtual environment
3. **Updates Packages** - Upgrades marker-pdf, markitdown, and python-dotenv
4. **Fetches Versions** - Reads current versions from pip
5. **Creates Backup** - Saves existing .env as `.env.backup_YYYYMMDD_HHMMSS`
6. **Merges Configuration** - Combines existing settings with updated versions
7. **Updates .env** - Writes updated configuration to .env file

## .env Template

The script generates/maintains the following structure:

```env
# Marker PDF Configuration
# Generated: 2025-11-03 00:50:50

# Package Versions (auto-updated)
MARKER_PDF_VERSION=1.10.1
MARKITDOWN_VERSION=0.1.3
PYTHON_DOTENV_VERSION=1.2.1

# API Configuration (preserve your keys here)
ANTHROPIC_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here
GOOGLE_API_KEY=your_key_here

# Output Configuration
OUTPUT_DIR=./OutputPdf
LOG_LEVEL=INFO

# Processing Configuration
ENABLE_OCR=true
ENABLE_MATH=true
BATCH_SIZE=10

# Virtual Environment
VENV_PATH=.\.venv

# Last Updated
LAST_UPDATED=2025-11-03 00:50:50
```

## Features Explained

### Smart Merging
- **Preserves Existing Values**: Your API keys and custom settings are never overwritten
- **Updates Package Versions**: Version strings are always updated to reflect current packages
- **Maintains Structure**: Configuration remains organized and readable

### Backup System
Automatic backups are created before each update:
- **Format**: `.env.backup_YYYYMMDD_HHMMSS`
- **Example**: `.env.backup_20251103_004950`
- **Location**: Same directory as .env

### Logging
Clear, timestamped log output:
```
[2025-11-03 00:49:31] [Info] Starting .env auto-update process...
[2025-11-03 00:50:50] [Success] .env file updated successfully
```

## Scheduling

### Windows Task Scheduler (Recommended)
1. Open Task Scheduler
2. Create Basic Task → Name: "Update Marker .env"
3. Set Trigger: Daily/Weekly as needed
4. Set Action: `powershell.exe -ExecutionPolicy Bypass -File "D:\Proj.Other\Marker_pdf\update_env.ps1"`
5. Check "Run whether user is logged in or not"

### PowerShell Schedule (Alternative)
```powershell
$trigger = New-JobTrigger -Daily -At 2:00AM
$options = New-ScheduledJobOption -RunElevated -ContinueIfGoingOnBattery -StartIfOnBattery
Register-ScheduledJob -Name "MarkerEnvUpdate" `
    -ScriptBlock { & "D:\Proj.Other\Marker_pdf\update_env.ps1" } `
    -Trigger $trigger `
    -ScheduledJobOption $options
```

## Troubleshooting

### ExecutionPolicy Error
```
"update_env.ps1 cannot be loaded because running scripts is disabled"
```
**Solution**: Run with `-ExecutionPolicy Bypass` or set permanently:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Virtual Environment Not Found
```
"Virtual environment not found at .\.venv"
```
**Solution**: Ensure .venv exists or specify correct path:
```powershell
.\update_env.ps1 -VenvPath "path\to\your\.venv"
```

### Package Not Found Warnings
These are non-fatal. The script continues and captures available versions.

### .env Not Created
**Solution**: Check that the script completed successfully and the directory is writable:
```powershell
Test-Path ".\.env"
Get-Item ".\.env" | Select-Object FullName, Length
```

## Configuration Options

### Adding Custom Environment Variables
Edit `.env` manually or modify the `New-EnvTemplate` function to include new variables:

```powershell
# In New-EnvTemplate function, add:
MY_CUSTOM_VAR=value
```

### Changing Packages to Update
Modify the `@PackageNames` parameter in the `Update-PipPackages` function:

```powershell
@("marker-pdf", "markitdown", "python-dotenv", "your-package-name")
```

## API Configuration Guide

### Anthropic API
```env
ANTHROPIC_API_KEY=your_anthropic_key_from_console.anthropic.com
```

### OpenAI API
```env
OPENAI_API_KEY=your_openai_key_from_platform.openai.com
```

### Google AI API
```env
GOOGLE_API_KEY=your_google_api_key
```

## Best Practices

✅ Run script before major operations  
✅ Check .env after updates  
✅ Keep backups for 30 days  
✅ Use Task Scheduler for automated updates  
✅ Document any custom variables added  
✅ Store API keys securely (consider using secrets management)  

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-11-03 | Initial release |

## Support

For issues:
1. Check the Troubleshooting section
2. Review script output logs
3. Verify file permissions
4. Ensure Python packages are installed

## License

This script is provided as-is for managing Marker PDF environments.

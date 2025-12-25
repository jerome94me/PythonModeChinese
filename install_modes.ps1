# ==================================================
# File Name: install_modes.ps1
# Description: Automatically install third-party Python modules for the project.
# Note: Built-in standard libraries (e.g., datetime, sys) have been removed.
# ==================================================

Write-Host "--- Starting Installation of Third-Party Modules ---" -ForegroundColor Cyan

# Define the list of modules to be installed
$modules = @(
    "rich",
    "keyboard",
    "numpy",
    "mpmath",
    "playsound",
    "pywin32",         # Package name for win32com
    "deep_translator",
    "python-barcode",
    "pillow",
    "selenium",
    "sounddevice",
    "scipy",
    "psutil"
)
foreach ($module in $modules) {
    Write-Host "Installing: $module ..." -ForegroundColor Yellow
    pip install $module
}

Write-Host "--- All Third-Party Modules Installed Successfully! ---" -ForegroundColor Green
Write-Host "Note: datetime, json, sys, logging, and random are built-in libraries and do not need to be installed." -ForegroundColor Gray
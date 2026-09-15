param([switch]$Mock)

$ErrorActionPreference = "Stop"

Write-Host "=== Load Shedding Tracker: Build & Run ===" -ForegroundColor Cyan

if (-not (Test-Path ".venv")) {
    Write-Host "Creating virtual environment..."
    python -m venv .venv
}

& .\.venv\Scripts\Activate.ps1

Write-Host "Installing dependencies..."
pip install -q -r requirements.txt

Write-Host "Checking syntax..."
$pyFiles = Get-ChildItem -Path src, config, analysis -Filter *.py -Recurse | ForEach-Object { $_.FullName }
python -m py_compile $pyFiles

Write-Host "Running tests..."
pytest tests\ -v

Write-Host "Running pipeline..."
if ($Mock) {
    python -m src.main --mock
} else {
    python -m src.main
}

Write-Host "Generating visualization..."
if (-not (Test-Path "screenshots")) {
    New-Item -ItemType Directory -Path "screenshots" | Out-Null
}
python -m analysis.visualize
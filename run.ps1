$ErrorActionPreference = "Stop"

Write-Host "=== Load Shedding Tracker: Build & Run ===" -ForegroundColor Cyan

# 1. Create venv if it doesn't exist
if (-not (Test-Path ".venv")) {
    Write-Host "Creating virtual environment..."
    python -m venv .venv
}

# 2. Activate venv
& .\.venv\Scripts\Activate.ps1

# 3. Install dependencies
Write-Host "Installing dependencies..."
pip install -q -r requirements.txt

# 4. Syntax check ("compile") all source files
Write-Host "Checking syntax..."
python -m py_compile src\*.py config\*.py analysis\*.py

# 5. Run tests
Write-Host "Running tests..."
pytest tests\ -v

# 6. Run the pipeline
Write-Host "Running pipeline..."
python -m src.main
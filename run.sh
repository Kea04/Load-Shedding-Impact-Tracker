#!/usr/bin/env bash
set -e  # exit immediately if any command fails

echo "=== Load Shedding Tracker: Build & Run ==="

# Detect python command (some systems use python3, others python)
if command -v python3 &> /dev/null; then
    PYTHON=python3
else
    PYTHON=python
fi

# 1. Create venv if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    $PYTHON -m venv .venv
fi

# 2. Activate venv (path differs on Windows Git Bash vs Linux/macOS)
if [ -f ".venv/Scripts/activate" ]; then
    source .venv/Scripts/activate   # Windows Git Bash
else
    source .venv/bin/activate       # Linux/macOS
fi

# 3. Install dependencies
echo "Installing dependencies..."
pip install -q -r requirements.txt

# 4. Syntax check ("compile") all source files
echo "Checking syntax..."
$PYTHON -m py_compile src/*.py config/*.py analysis/*.py

# 5. Run tests
echo "Running tests..."
pytest tests/ -v

# 6. Run the pipeline
echo "Running pipeline..."
$PYTHON -m src.main
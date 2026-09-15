#!/usr/bin/env bash
set -e

echo "=== Load Shedding Tracker: Build & Run ==="

if command -v python3 &> /dev/null; then
    PYTHON=python3
else
    PYTHON=python
fi

if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    $PYTHON -m venv .venv
fi

if [ -f ".venv/Scripts/activate" ]; then
    source .venv/Scripts/activate
else
    source .venv/bin/activate
fi

echo "Installing dependencies..."
pip install -q -r requirements.txt

echo "Checking syntax..."
find src config analysis -name "*.py" -exec $PYTHON -m py_compile {} +

echo "Running tests..."
pytest tests/ -v

echo "Running pipeline..."
if [ "$1" == "--mock" ]; then
    $PYTHON -m src.main --mock
else
    $PYTHON -m src.main
fi

echo "Generating visualization..."
mkdir -p screenshots
$PYTHON -m analysis.visualize
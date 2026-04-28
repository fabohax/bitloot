#!/bin/bash
# This script activates the Python virtual environment and runs main.py

# Activate the virtual environment
source "$(dirname "$0")/.venv/bin/activate"

# Run the main.py script
python main.py --words 12 --no-check-balance --batch 10

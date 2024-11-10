#!/bin/bash

# Check if the virtual environment exists
if [ ! -d "tinyagi-env" ]; then
    echo "Creating virtual environment..."
    python3 -m venv tinyagi-env
fi

# Activate the virtual environment
source tinyagi-env/bin/activate

# Install dependencies from requirements.txt
echo "Installing dependencies..."
pip install -r requirements.txt

# Run the Python script
python start_ui.py

# Deactivate the virtual environment
deactivate

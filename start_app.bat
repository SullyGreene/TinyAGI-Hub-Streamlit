@echo off
REM Check if the virtual environment exists
if not exist "tinyagi-env\Scripts\activate.bat" (
    echo Creating virtual environment...
    python -m venv tinyagi-env
)

REM Activate the virtual environment
call tinyagi-env\Scripts\activate

REM Install dependencies from requirements.txt
echo Installing dependencies...
pip install -r requirements.txt

REM Run the Python script
python start_ui.py

REM Deactivate the virtual environment
deactivate

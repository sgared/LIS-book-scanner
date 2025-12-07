@echo off
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt --quiet
python app.py
pause
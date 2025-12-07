@echo off
echo 🧪 Testing Server-Side App Locally...

cd server-side

echo 📦 Checking Python dependencies...
python -c "import flask, tesseract" 2>nul
if errorlevel 1 (
    echo ⚠️  Installing dependencies...
    pip install -r requirements_minimal.txt
)

echo 🚀 Starting Flask server...
echo 🌐 Server will be available at: http://localhost:5000
echo 📱 Mobile-friendly interface with advanced OCR processing

python app_production.py

pause
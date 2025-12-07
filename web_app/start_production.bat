@echo off
REM ====================================================
REM LIS Book Scanner - Production Startup Script
REM ====================================================

echo.
echo ============================================
echo   LIS Book Scanner - Starting Production
echo ============================================
echo.

echo 🔧 Checking Python installation...
python --version
if errorlevel 1 (
    echo ❌ Python not found! Please install Python 3.8+
    pause
    exit /b 1
)

echo.
echo 📦 Installing/updating dependencies...
pip install flask pillow pytesseract pandas matplotlib requests werkzeug

echo.
echo 🗄️ Ensuring directories exist...
if not exist "uploads" mkdir uploads
if not exist "static\temp_uploads" mkdir static\temp_uploads

echo.
echo 🚀 Starting LIS Book Scanner (Production Mode)...
echo.
echo 📱 Features:
echo    ✅ Mobile-responsive design
echo    ✅ Camera integration
echo    ✅ OCR processing
echo    ✅ Database cataloging
echo    ✅ Analytics dashboard
echo    ✅ Data export
echo.
echo 🔗 Access at: http://localhost:5000
echo 📋 Press Ctrl+C to stop the server
echo.

python app_production.py

echo.
echo 🛑 Server stopped.
pause
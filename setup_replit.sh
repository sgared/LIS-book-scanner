#!/bin/bash

echo "🚀 Setting up LIS Book Scanner for Replit..."

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install basic requirements first
pip install flask werkzeug

# Try to install additional packages
echo "📦 Installing Python packages..."
pip install pillow pandas matplotlib numpy || echo "⚠️ Some packages failed - continuing with basic setup"

# Try to install tesseract python wrapper
pip install pytesseract || echo "⚠️ pytesseract installation failed - will use simulation mode"

# Create required directories
echo "📁 Creating directories..."
mkdir -p server-side/uploads
mkdir -p server-side/static/temp_uploads

# Set permissions
chmod 755 server-side/uploads
chmod 755 server-side/static/temp_uploads

# Check if tesseract is available
echo "🔍 Checking Tesseract installation..."
if command -v tesseract &> /dev/null; then
    echo "✅ Tesseract OCR found: $(tesseract --version | head -1)"
    export TESSDATA_PREFIX="/nix/store/*/share/tessdata"
else
    echo "⚠️ Tesseract not found - will run in simulation mode"
fi

echo "✅ Setup complete! Starting application..."

# Start the application
cd server-side && python app_production.py
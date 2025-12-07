@echo off
echo 🧠 Starting ML Research Environment...

cd ml-research

echo 📦 Checking Jupyter installation...
python -c "import jupyter" 2>nul
if errorlevel 1 (
    echo ⚠️  Installing Jupyter and dependencies...
    pip install jupyter pandas numpy matplotlib opencv-python pillow
)

echo 🚀 Starting Jupyter Lab...
echo 📔 Opening LIS_OCR_Project.ipynb for research and training
echo 🔬 Use this environment for OCR experiments and model training

jupyter lab LIS_OCR_Project.ipynb

pause
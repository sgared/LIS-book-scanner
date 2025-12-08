# 🚀 LIS Book Scanner - Replit Deployment

> **Flask-based OCR application ready for Replit hosting**

## ⚡ Quick Start on Replit

### 1. **Import to Replit**
1. Go to [Replit.com](https://replit.com)
2. Click **"Create Repl"** → **"Import from GitHub"**
3. Enter repository URL: `https://github.com/sgared/LIS-book-scanner`
4. Click **"Import from GitHub"**

### 2. **Alternative: Upload Files**
If GitHub import doesn't work:
1. Create **New Repl** → **Python**
2. Delete default files
3. Upload all files from this project
4. Replit will auto-detect the configuration

### 3. **Run the Application**
```bash
# Replit will automatically run:
cd server-side && python app_production.py
```

## 🔧 **Replit Configuration**

### **Files Created:**
- **`.replit`** - Main configuration file
- **`replit.nix`** - System dependencies (Tesseract OCR)
- **`pyproject.toml`** - Python dependencies

### **Features Enabled:**
- ✅ **Tesseract OCR** - Pre-installed system binary
- ✅ **Flask Web Server** - Auto-configured for Replit
- ✅ **File Uploads** - Persistent storage
- ✅ **SQLite Database** - Data persistence
- ✅ **Mobile Support** - Responsive interface

## 🌐 **Access Your App**

After deployment:
```
https://your-repl-name--yourusername.repl.co
```

## 🔨 **Replit-Specific Features**

### **Environment Variables**
- `TESSDATA_PREFIX` - Tesseract data path
- `PYTHON_LD_LIBRARY_PATH` - System libraries
- Auto-configured for Replit hosting

### **File Structure** 
```
/
├── .replit              # Replit config
├── replit.nix           # System dependencies
├── pyproject.toml       # Python deps
├── server-side/         # Flask application
│   ├── app_production.py # Main app
│   ├── templates/       # HTML templates
│   ├── static/          # CSS/JS assets
│   └── uploads/         # File upload directory
├── client-side/         # Browser-only version
└── ml-research/         # Jupyter notebooks
```

## 🚀 **Deployment Steps**

### **Method 1: GitHub Integration**
1. **Fork Repository** on GitHub
2. **Import to Replit** from your fork
3. **Click Run** - Replit handles everything!

### **Method 2: Direct Upload**
1. **Zip entire project** folder
2. **Create Python Repl** on Replit
3. **Upload zip file** and extract
4. **Click Run** to start

### **Method 3: Git Clone**
```bash
# In Replit shell:
git clone https://github.com/sgared/LIS-book-scanner.git
cd LIS-book-scanner
python server-side/app_production.py
```

## 🎯 **Why Replit?**

### **✅ Advantages**
- **Zero Setup** - Everything pre-configured
- **Free Hosting** - No cost for basic usage
- **Instant Deployment** - One-click hosting
- **Collaborative** - Share and edit with others
- **Mobile Access** - Works on phones/tablets

### **⚠️ Limitations**
- **Sleep Mode** - Free apps sleep when inactive
- **Resource Limits** - CPU/Memory constraints
- **Public URLs** - Apps are publicly accessible

## 🔧 **Troubleshooting**

### **Common Issues:**

**❌ Import Error:**
```
Solution: Use "Import from GitHub" instead of direct upload
```

**❌ Tesseract Not Found:**
```
Solution: Replit.nix should auto-install Tesseract
Check: echo $TESSDATA_PREFIX
```

**❌ Port Issues:**
```python
# In app_production.py, use:
app.run(host='0.0.0.0', port=5000, debug=True)
```

**❌ File Upload Fails:**
```
Solution: Check uploads/ directory permissions
Replit auto-creates required directories
```

## 📱 **Mobile Testing**

Your Replit app will be fully mobile-responsive:
- **Camera Integration** - Take photos directly
- **Touch Interface** - Optimized for mobile
- **Progressive Web App** - Install as native app

## 🎉 **Ready for Deployment!**

Your project now has everything needed for Replit:
1. **System dependencies** (Tesseract OCR)
2. **Python dependencies** (Flask, PIL, etc.)
3. **Auto-run configuration**
4. **Web server setup**

Just import to Replit and click **Run**! 🚀
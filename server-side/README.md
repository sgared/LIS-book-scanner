# 🐍 LIS Book Scanner - Server-Side (Python/Flask)

> **Flask-based web application with advanced OCR and NLP processing**

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager

### Installation
```bash
# Install dependencies
pip install -r requirements.txt

# For minimal deployment (production)
pip install -r requirements_minimal.txt
```

### Run the Application
```bash
# Development mode
python app.py

# Production mode (recommended)
python app_production.py

# Windows batch files
start_production.bat
```

## 📁 File Structure
```
server-side/
├── app.py                    # Original Flask app
├── app_production.py         # Production-ready Flask app (recommended)
├── app_fixed.py             # Fixed version with enhancements
├── requirements.txt         # Full Python dependencies
├── requirements_minimal.txt # Minimal production dependencies
├── test_production.py       # Unit tests
├── Dockerfile              # Docker container configuration
├── docker-compose.yml      # Docker compose setup
├── static/                 # CSS, JS, and static assets
├── templates/              # HTML templates
└── uploads/                # Image upload directory
```

## ⚙️ Features
- **Server-side OCR**: Tesseract + EasyOCR
- **Advanced NLP**: spaCy integration
- **SQLite Database**: Persistent storage
- **RESTful API**: JSON endpoints
- **Docker Support**: Containerized deployment

## 🐳 Docker Deployment
```bash
# Build and run
docker-compose up --build

# Or manually
docker build -t lis-scanner .
docker run -p 5000:5000 lis-scanner
```

## 🧪 Testing
```bash
python test_production.py
```

## 🌐 Endpoints
- `GET /` - Main interface
- `POST /upload` - Process images
- `GET /analytics` - View statistics
- `GET /database` - Browse catalog
- `GET /export` - Download data
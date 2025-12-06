# 🚀 Deployment Guide - LIS Book Scanner

This guide provides comprehensive instructions for deploying the LIS Book Scanner in various environments.

## 📋 Prerequisites

### System Requirements
- Python 3.8 or higher
- Tesseract OCR engine
- 2GB RAM minimum (4GB recommended)
- 10GB disk space for uploads and database
- Modern web browser with JavaScript enabled

### Required Python Packages
All dependencies are listed in `requirements.txt`:
```
Flask>=2.3.0
Pillow>=10.0.0
pytesseract>=0.3.10
easyocr>=1.7.0
spacy>=3.7.0
nltk>=3.8.1
pandas>=2.0.0
matplotlib>=3.7.0
requests>=2.31.0
Werkzeug>=2.3.0
```

## 🏠 Local Development Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/lis-book-scanner.git
cd lis-book-scanner
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux  
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 4. Install Tesseract OCR

#### Windows
1. Download from: https://github.com/tesseract-ocr/tesseract/releases
2. Install and note the installation path
3. Update `app.py` with correct path:
```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

#### macOS
```bash
brew install tesseract
```

#### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr tesseract-ocr-eng
```

### 5. Run the Application
```bash
cd web_app
python app.py
```

Access the application at: http://localhost:5000

## ☁️ Cloud Deployment Options

### 🅰️ Heroku Deployment

#### Prerequisites
- Heroku account
- Heroku CLI installed

#### Setup Steps
1. **Create Heroku App**
```bash
heroku create your-app-name
```

2. **Add Buildpacks**
```bash
heroku buildpacks:add --index 1 https://github.com/heroku/heroku-buildpack-apt
heroku buildpacks:add --index 2 heroku/python
```

3. **Create Aptfile**
```bash
echo "tesseract-ocr" > Aptfile
echo "tesseract-ocr-eng" >> Aptfile
```

4. **Create Procfile**
```bash
echo "web: gunicorn -w 4 -b 0.0.0.0:\$PORT web_app.app:app" > Procfile
```

5. **Set Environment Variables**
```bash
heroku config:set FLASK_ENV=production
heroku config:set SECRET_KEY=your-secret-key
```

6. **Deploy**
```bash
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

### 🐙 GitHub Pages (Static Demo)

For a static demonstration version:

1. **Create gh-pages branch**
```bash
git checkout -b gh-pages
```

2. **Create simple HTML version**
```bash
# This would be a simplified version showing the interface
# See: https://yourusername.github.io/lis-book-scanner
```

### 🔴 DigitalOcean Droplet

#### 1. Create Droplet
- Choose Ubuntu 20.04
- Select appropriate size (2GB RAM minimum)
- Add SSH keys

#### 2. Server Setup
```bash
# Connect to droplet
ssh root@your-droplet-ip

# Update system
apt update && apt upgrade -y

# Install Python and dependencies
apt install -y python3 python3-pip python3-venv nginx tesseract-ocr

# Create application user
adduser bookscanner
su - bookscanner
```

#### 3. Application Setup
```bash
# Clone repository
git clone https://github.com/yourusername/lis-book-scanner.git
cd lis-book-scanner

# Setup virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm

# Install Gunicorn
pip install gunicorn
```

#### 4. Systemd Service
```bash
sudo nano /etc/systemd/system/bookscanner.service
```

```ini
[Unit]
Description=LIS Book Scanner
After=network.target

[Service]
User=bookscanner
Group=www-data
WorkingDirectory=/home/bookscanner/lis-book-scanner
Environment="PATH=/home/bookscanner/lis-book-scanner/venv/bin"
ExecStart=/home/bookscanner/lis-book-scanner/venv/bin/gunicorn --workers 3 --bind unix:bookscanner.sock -m 007 web_app.app:app
Restart=always

[Install]
WantedBy=multi-user.target
```

#### 5. Nginx Configuration
```bash
sudo nano /etc/nginx/sites-available/bookscanner
```

```nginx
server {
    listen 80;
    server_name your-domain.com www.your-domain.com;
    
    location / {
        include proxy_params;
        proxy_pass http://unix:/home/bookscanner/lis-book-scanner/bookscanner.sock;
    }
    
    location /static {
        alias /home/bookscanner/lis-book-scanner/web_app/static;
        expires 30d;
    }
    
    client_max_body_size 16M;
}
```

#### 6. Enable and Start Services
```bash
sudo ln -s /etc/nginx/sites-available/bookscanner /etc/nginx/sites-enabled
sudo systemctl start bookscanner
sudo systemctl enable bookscanner
sudo systemctl restart nginx
```

## 🐳 Docker Deployment

### Build and Run
```bash
# Build image
docker build -t lis-book-scanner .

# Run container
docker run -d \
  --name bookscanner \
  -p 5000:5000 \
  -v $(pwd)/web_app/uploads:/app/web_app/uploads \
  -v $(pwd)/web_app/catalog.db:/app/web_app/catalog.db \
  lis-book-scanner
```

### Docker Compose
```bash
docker-compose up -d
```

## 🔒 Security Considerations

### Production Security Checklist

- [ ] **Environment Variables**: Store secrets in environment variables
- [ ] **HTTPS**: Enable SSL/TLS encryption
- [ ] **File Upload Limits**: Configure appropriate file size limits
- [ ] **Input Validation**: Ensure all user inputs are validated
- [ ] **Database Security**: Use proper database permissions
- [ ] **Rate Limiting**: Implement API rate limiting
- [ ] **Error Handling**: Don't expose system information in errors
- [ ] **Regular Updates**: Keep dependencies updated

### Environment Variables
```bash
# Required
export FLASK_ENV=production
export SECRET_KEY=your-very-secure-secret-key

# Optional
export DATABASE_URL=sqlite:///catalog.db
export MAX_CONTENT_LENGTH=16777216
export TESSERACT_CMD=/usr/bin/tesseract
```

### SSL Certificate (Let's Encrypt)
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com -d www.your-domain.com
```

## 📊 Performance Optimization

### Application Level
- **Gunicorn Workers**: Use 2x CPU cores
- **Database**: Consider PostgreSQL for production
- **File Storage**: Use cloud storage for uploads
- **Caching**: Implement Redis for session storage

### Server Level
- **Nginx**: Configure proper caching headers
- **Gzip**: Enable compression for static files
- **CDN**: Use CloudFlare or AWS CloudFront
- **Monitoring**: Setup application monitoring

## 📱 Mobile Optimization

The application includes:
- ✅ Responsive design with Bootstrap 5
- ✅ Mobile-first CSS approach
- ✅ Touch-friendly interface elements
- ✅ Progressive Web App (PWA) support
- ✅ Camera integration for direct photo capture
- ✅ Offline capability (planned)

### PWA Installation
Users can install the app on mobile devices:
1. Open in mobile browser
2. Tap browser menu
3. Select "Add to Home Screen"
4. Confirm installation

## 🔧 Troubleshooting

### Common Issues

#### Port Already in Use
```bash
# Find process using port 5000
sudo lsof -i :5000

# Kill process
sudo kill -9 <PID>
```

#### Tesseract Not Found
```python
# Update path in app.py
import pytesseract
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'  # Linux
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows
```

#### Permission Errors
```bash
# Fix file permissions
sudo chown -R bookscanner:bookscanner /home/bookscanner/lis-book-scanner
sudo chmod -R 755 /home/bookscanner/lis-book-scanner
```

#### Memory Issues
```python
# Add to app.py for memory management
import gc
gc.collect()  # Force garbage collection after processing
```

## 📈 Monitoring and Maintenance

### Log Files
```bash
# Application logs
tail -f /var/log/bookscanner/app.log

# Nginx logs
tail -f /var/log/nginx/access.log
tail -f /var/log/nginx/error.log

# System logs
journalctl -u bookscanner -f
```

### Health Checks
```bash
# Check application status
curl -f http://localhost:5000/ || echo "App is down"

# Check disk space
df -h

# Check memory usage
free -m

# Check CPU usage
htop
```

### Backup Strategy
```bash
# Database backup
cp web_app/catalog.db backups/catalog_$(date +%Y%m%d_%H%M%S).db

# Upload folder backup
tar -czf backups/uploads_$(date +%Y%m%d_%H%M%S).tar.gz web_app/uploads/
```

### Updates
```bash
# Pull latest code
git pull origin main

# Update dependencies
pip install -r requirements.txt --upgrade

# Restart service
sudo systemctl restart bookscanner
```

## 📞 Support

### Getting Help
- 📖 [Project Wiki](../../wiki)
- 💬 [GitHub Discussions](../../discussions)
- 🐛 [Report Issues](../../issues)
- 📧 Email: support@example.com

### Performance Benchmarks
- **OCR Processing**: 2-5 seconds per image
- **Metadata Extraction**: 0.5-1 second per book
- **Database Operations**: <10ms per query
- **Page Load**: <2 seconds on 3G

---

**🎉 Congratulations! Your LIS Book Scanner is now deployed and ready to digitize library collections!**
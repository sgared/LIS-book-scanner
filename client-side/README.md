# LIS Book Scanner - Client-Side OCR Application

> 🚀 **A fully client-side web application for book cataloging using OCR and NLP**
> 
> **Live Demo:** [https://sgared.github.io/LIS-book-scanner](https://sgared.github.io/LIS-book-scanner)

[![Deploy Status](https://img.shields.io/badge/deploy-GitHub%20Pages-success)](https://sgared.github.io/LIS-book-scanner)
[![JavaScript](https://img.shields.io/badge/JavaScript-Client%20Side-yellow)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Tesseract.js](https://img.shields.io/badge/OCR-Tesseract.js-blue)](https://tesseract.projectnaptha.com/)
[![Bootstrap](https://img.shields.io/badge/UI-Bootstrap%205-purple)](https://getbootstrap.com/)

## ✨ Features

### 🔍 **Advanced OCR Processing**
- **Tesseract.js Integration**: Client-side OCR processing directly in the browser
- **High Accuracy**: Advanced preprocessing and multiple recognition attempts
- **Real-time Progress**: Live progress indicators during OCR processing
- **Batch Processing**: Handle multiple book images simultaneously

### 🤖 **Smart NLP Analysis**
- **Metadata Extraction**: Automatic extraction of title, author, year, ISBN
- **Keyword Analysis**: AI-powered keyword extraction from text content
- **Hugging Face Integration**: Optional cloud-based NLP processing
- **Confidence Scoring**: OCR confidence assessment for quality control

### 📱 **Mobile-First Design**
- **Responsive Interface**: Optimized for desktop, tablet, and mobile devices
- **Camera Integration**: Direct photo capture on mobile devices
- **Touch-Friendly**: Large buttons and intuitive touch interactions
- **Progressive Web App**: Install as a native app on mobile devices

### 💾 **Data Management**
- **Local Storage**: Client-side data persistence using browser storage
- **Export Options**: CSV and JSON export functionality
- **Real-time Analytics**: Interactive charts and statistics
- **Book Catalog**: Comprehensive database view with filtering

## 🎯 Quick Start

### Option 1: Direct GitHub Pages Access
```
https://sgared.github.io/LIS-book-scanner
```
Click the link above and start using immediately! No installation required.

### Option 2: Download and Run Locally
1. **Download the HTML file**:
   ```bash
   # Clone the repository
   git clone https://github.com/sgared/LIS-book-scanner.git
   cd LIS-book-scanner
   
   # Open the application
   open app.html  # macOS
   # or
   start app.html  # Windows
   ```

2. **Open in browser**: Double-click `app.html` or serve via local server

### Option 3: Host on Your Own GitHub Pages
1. Fork this repository
2. Go to Settings → Pages
3. Select "Deploy from a branch" → main branch
4. Your app will be live at `https://yourusername.github.io/LIS-book-scanner`

## 📖 How to Use

### 1. **Upload Book Images**
- **Drag & Drop**: Drag book cover/title page images into the upload area
- **File Browser**: Click "Select Images" to browse your files
- **Mobile Camera**: Tap "Take Photo" to capture images directly (mobile only)
- **Batch Upload**: Select multiple images for bulk processing

### 2. **Process with OCR**
- Click "Start OCR Processing" after uploading images
- Watch real-time progress as Tesseract.js processes each image
- View extracted text and metadata for each book
- See confidence scores to assess OCR quality

### 3. **Review Results**
- **Automatic Metadata**: Title, author, year, ISBN automatically extracted
- **Confidence Indicators**: Color-coded badges show OCR accuracy
- **Text Preview**: View raw OCR text output for verification
- **Keyword Extraction**: AI-generated keywords for better categorization

### 4. **Manage Your Catalog**
- **Analytics Dashboard**: View statistics about your book collection
- **Database View**: Browse all processed books in a sortable table
- **Export Options**: Download your catalog as CSV or JSON
- **Local Persistence**: Data automatically saved to browser storage

## 🛠️ Technical Architecture

### Core Technologies
- **Frontend**: Vanilla JavaScript + Bootstrap 5.3.3
- **OCR Engine**: Tesseract.js 5.x (WebAssembly-based)
- **NLP**: Custom algorithms + optional Hugging Face API
- **Charts**: Chart.js for analytics visualization
- **Storage**: Browser LocalStorage for data persistence

### Key Components

#### OCR Processing Pipeline
```javascript
Image Upload → Tesseract.js Recognition → Text Extraction → Confidence Assessment
```

#### Metadata Extraction Engine
```javascript
Raw OCR Text → Regex Patterns → NLP Analysis → Structured Metadata
```

#### Data Flow
```javascript
Client Upload → Browser Processing → Local Storage → Real-time UI Updates
```

### Browser Compatibility
- **Chrome/Edge**: ✅ Full support (recommended)
- **Firefox**: ✅ Full support
- **Safari**: ✅ Full support
- **Mobile Browsers**: ✅ Optimized experience

## 📊 Performance Optimization

### Image Processing Tips
- **Optimal Image Size**: 800-1600px width for best OCR results
- **File Format**: JPEG or PNG recommended
- **Lighting**: Good contrast between text and background
- **Angle**: Straight-on shots work best

### Browser Performance
- **Memory Usage**: ~50-100MB per processed image
- **Processing Time**: 5-15 seconds per image depending on complexity
- **Storage Limit**: ~5-10MB for LocalStorage (hundreds of books)

## 🚀 Deployment Options

### 1. GitHub Pages (Recommended)
```bash
# Push to GitHub repository with gh-pages branch
git checkout -b gh-pages
git add app.html
git commit -m "Deploy client-side app"
git push origin gh-pages
```

### 2. Netlify
```bash
# Deploy directly from GitHub or upload app.html
netlify deploy --prod --dir .
```

### 3. Vercel
```bash
# Deploy with Vercel CLI
vercel --prod
```

### 4. Local Server
```bash
# Python 3
python -m http.server 8000

# Node.js
npx serve .

# PHP
php -S localhost:8000
```

## 🔐 Data Privacy & Security

- **Client-Side Only**: All processing happens in your browser
- **No Server Communication**: OCR and NLP run locally (except optional Hugging Face API)
- **Local Storage**: Data remains on your device unless you export it
- **No Tracking**: No analytics or tracking scripts included

## 📋 Troubleshooting

### Common Issues

#### OCR Not Working
- Ensure JavaScript is enabled
- Check browser console for WebAssembly errors
- Try refreshing the page
- Use supported image formats (JPG, PNG)

#### Poor OCR Results
- Ensure good image quality and lighting
- Check that text is clearly visible
- Try cropping to focus on title page
- Ensure text is horizontal (not rotated)

#### Data Not Saving
- Check that LocalStorage is enabled
- Clear browser cache if storage is full
- Export data regularly as backup

#### Mobile Issues
- Use "Take Photo" for better camera integration
- Ensure sufficient lighting for camera capture
- Try using browser file upload if camera fails

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make your changes to `app.html`
4. Test thoroughly across browsers
5. Submit a pull request

### Areas for Contribution
- **OCR Improvements**: Better preprocessing algorithms
- **NLP Enhancement**: Advanced metadata extraction
- **UI/UX**: Interface improvements and accessibility
- **Performance**: Optimization and speed improvements
- **Documentation**: Tutorials and guides

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Tesseract.js**: Amazing WebAssembly OCR implementation
- **Bootstrap**: Beautiful responsive UI framework
- **Chart.js**: Excellent charting library
- **Hugging Face**: Powerful NLP APIs and models
- **GitHub Pages**: Free and reliable hosting platform

## 📞 Support

Need help? Here are your options:

- **GitHub Issues**: [Report bugs or request features](https://github.com/sgared/LIS-book-scanner/issues)
- **Documentation**: Check this README for detailed guides
- **Live Demo**: Try the app at [sgared.github.io/LIS-book-scanner](https://sgared.github.io/LIS-book-scanner)

---

**Made with ❤️ for the library and information science community**

> Transform your book collection management with the power of client-side OCR and AI!
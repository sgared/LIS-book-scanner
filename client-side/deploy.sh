#!/bin/bash
# Deploy client-side app to GitHub Pages

echo "🚀 Deploying Client-Side App to GitHub Pages..."

# Copy to gh-pages branch
git checkout gh-pages 2>/dev/null || git checkout -b gh-pages

# Copy client app as index.html
cp client-side/index.html ./index.html

# Commit and push
git add index.html
git commit -m "Deploy client-side OCR application

- Tesseract.js browser-based OCR
- Hugging Face NLP integration  
- Mobile-responsive design
- Local storage data persistence"

git push origin gh-pages

echo "✅ Client-side app deployed to: https://sgared.github.io/LIS-book-scanner"
echo "📱 Mobile-friendly and works offline!"

git checkout main
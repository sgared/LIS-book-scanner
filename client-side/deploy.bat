@echo off
REM Deploy client-side app to GitHub Pages

echo 🚀 Deploying Client-Side App to GitHub Pages...

REM Switch to gh-pages branch
git checkout gh-pages 2>nul || git checkout -b gh-pages

REM Copy client app as index.html
copy client-side\index.html index.html

REM Commit and push
git add index.html
git commit -m "Deploy client-side OCR application - Tesseract.js browser-based OCR - Hugging Face NLP integration - Mobile-responsive design - Local storage data persistence"

git push origin gh-pages

echo ✅ Client-side app deployed to: https://sgared.github.io/LIS-book-scanner
echo 📱 Mobile-friendly and works offline!

git checkout main
pause
@echo off
REM ====================================================
REM GitHub Upload Script for LIS Book Scanner
REM ====================================================

echo.
echo ============================================
echo   LIS Book Scanner - GitHub Upload
echo ============================================
echo.

echo 📋 Instructions:
echo 1. Create a NEW repository on GitHub.com
echo 2. Copy the repository URL (ends with .git)
echo 3. Replace the URL below with your actual GitHub URL
echo 4. Run this script again
echo.

REM ⚠️ REPLACE THIS URL WITH YOUR ACTUAL GITHUB REPOSITORY URL ⚠️
set GITHUB_URL=https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

echo 🔗 Current GitHub URL: %GITHUB_URL%
echo.

if "%GITHUB_URL%"=="https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git" (
    echo ❌ Please edit this file and replace YOUR_USERNAME and YOUR_REPO_NAME
    echo    with your actual GitHub username and repository name.
    echo.
    echo 📝 Edit the file: upload_to_github.bat
    echo.
    pause
    exit /b 1
)

echo 🚀 Uploading to GitHub...
echo.

REM Add GitHub remote
echo ➕ Adding GitHub remote...
git remote add origin %GITHUB_URL%

REM Rename branch to main
echo 🌿 Setting main branch...
git branch -M main

REM Push to GitHub
echo ⬆️ Pushing to GitHub...
git push -u origin main

echo.
echo ✅ SUCCESS! Your LIS Book Scanner is now on GitHub!
echo.
echo 🌐 View your repository at:
echo %GITHUB_URL:~0,-4%
echo.
echo 📱 Your mobile-optimized OCR application is ready for the world!
echo.
pause
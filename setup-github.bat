@echo off
echo ============================================
echo GitHub Repository Setup Helper
echo ============================================
echo.
echo This script will help you connect this project to GitHub.
echo.
echo STEP 1: Create a new repository on GitHub
echo ----------------------------------------------
echo 1. Go to https://github.com/new
echo 2. Repository name: marketing-funnel-project (or your choice)
echo 3. Keep it Private or Public as needed
echo 4. DO NOT initialize with README, .gitignore, or license
echo 5. Click "Create repository"
echo.
echo STEP 2: Copy your repository URL
echo ----------------------------------------------
echo After creating, GitHub will show a URL like:
echo https://github.com/FAJU85/your-repo-name.git
echo.
set /p REPO_URL="Enter your GitHub repository URL: "

echo.
echo Connecting to GitHub...
git remote add origin %REPO_URL%

echo.
echo Pushing to GitHub...
git branch -M main
git push -u origin main

echo.
echo ============================================
echo Setup Complete!
echo ============================================
echo Your project is now on GitHub at: %REPO_URL%
echo.
pause

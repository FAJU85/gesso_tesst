@echo off
echo ============================================
echo HuggingFace Authentication Setup
echo ============================================
echo.
echo STEP 1: Get Your Token
echo ----------------------------------------------
echo 1. Go to: https://huggingface.co/settings/tokens
echo 2. Click "New token"
echo 3. Token type: WRITE
echo 4. Name: gesso_tesst-mcp
echo 5. Click "Generate token"
echo 6. Copy the token (starts with hf_...)
echo.
echo STEP 2: Login with CLI
echo ----------------------------------------------
echo Running HuggingFace login...
echo.

hf auth login

echo.
echo STEP 3: Set Environment Variable
echo ----------------------------------------------
set /p HF_TOKEN="Enter your HuggingFace token (hf_...): "

echo.
echo Saving token permanently...
setx HF_TOKEN "%HF_TOKEN%"

echo.
echo ============================================
echo Testing Connection...
echo ============================================
hf auth whoami

echo.
echo ============================================
echo Setup Complete!
echo ============================================
echo.
echo Your HuggingFace token is now configured.
echo Restart Goose to apply MCP server changes.
echo.
pause

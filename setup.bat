@echo off
setlocal

where uv >nul 2>&1

if %errorlevel% neq 0 (
    echo ERROR: uv is not installed.
    echo Please install uv first:
    echo https://docs.astral.sh/uv/getting-started/installation/
    pause
    exit /b 1
)

echo [1/2] Syncing environment...
uv sync

if %errorlevel% neq 0 (
    echo ERROR: uv sync failed.
    pause
    exit /b 1
)

echo [2/2] Downloading tokenizer...
uv run python tokenizer/download.py

if %errorlevel% neq 0 (
    echo ERROR: Tokenizer download failed.
    pause
    exit /b 1
)

echo.
echo Setup completed successfully!
pause
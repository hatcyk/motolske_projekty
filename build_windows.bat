@echo off
chcp 65001 >nul
REM Build script pro Windows (.exe)

echo [BUILD] Buildovani aplikace pro Windows...
echo.

REM Kontrola PyInstaller
where pyinstaller >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] PyInstaller neni nainstalovany!
    echo Spust: pip install -r requirements.txt
    exit /b 1
)

REM Vycisteni starych buildu
echo [INFO] Cisteni starych buildu...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist "motolske_projekty.spec" del "motolske_projekty.spec"

REM Build s PyInstaller
echo [INFO] Vytvareni .exe souboru...
pyinstaller ^
    --name="motolske_projekty" ^
    --windowed ^
    --onefile ^
    --add-data="ukoly;ukoly" ^
    --add-data="gui;gui" ^
    --add-data="tests;tests" ^
    --add-data="cli_menu.py;." ^
    --collect-all=flet ^
    --exclude-module=flet.testing ^
    --exclude-module=numpy ^
    --noconfirm ^
    main.py

REM Kontrola uspechu
if exist "dist\motolske_projekty.exe" (
    echo.
    echo [SUCCESS] Build uspesny!
    echo [INFO] Aplikace: dist\motolske_projekty.exe
    echo.
    echo Pro spusteni: start "dist\motolske_projekty.exe"
) else (
    echo.
    echo [ERROR] Build selhal!
    exit /b 1
)

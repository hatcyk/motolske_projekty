@echo off
REM Build script pro Windows (.exe)

echo 🔨 Buildování aplikace pro Windows...
echo.

REM Kontrola PyInstaller
where pyinstaller >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ❌ PyInstaller není nainstalován!
    echo Spusť: pip install -r requirements.txt
    exit /b 1
)

REM Vyčištění starých buildů
echo 🧹 Čištění starých buildů...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist "Domácí úkoly.spec" del "Domácí úkoly.spec"

REM Build s PyInstaller
echo 📦 Vytváření .exe souboru...
pyinstaller ^
    --name="Domácí úkoly" ^
    --windowed ^
    --onefile ^
    --add-data="ukoly;ukoly" ^
    --add-data="cli_menu.py;." ^
    --collect-all=flet ^
    --noconfirm ^
    main.py

REM Kontrola úspěchu
if exist "dist\Domácí úkoly.exe" (
    echo.
    echo ✅ Build úspěšný!
    echo 📂 Aplikace: dist\Domácí úkoly.exe
    echo.
    echo 💡 Pro spuštění: start "dist\Domácí úkoly.exe"
) else (
    echo.
    echo ❌ Build selhal!
    exit /b 1
)

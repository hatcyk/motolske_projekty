#!/bin/bash
# Build script pro macOS (.app)

echo "🔨 Buildování aplikace pro macOS..."
echo ""

# Kontrola PyInstaller
if ! command -v pyinstaller &> /dev/null; then
    echo "❌ PyInstaller není nainstalován!"
    echo "Spusť: pip install -r requirements.txt"
    exit 1
fi

# Vyčištění starých buildů
echo "🧹 Čištění starých buildů..."
rm -rf build dist *.spec

# Build s PyInstaller
echo "📦 Vytváření .app souboru..."
pyinstaller \
    --name="Domácí úkoly" \
    --windowed \
    --onedir \
    --add-data="ukoly:ukoly" \
    --add-data="cli_menu.py:." \
    --collect-all=flet \
    --exclude-module=flet.testing \
    --exclude-module=numpy \
    --noconfirm \
    main.py

# Kontrola úspěchu
if [ -d "dist/Domácí úkoly.app" ]; then
    echo ""
    echo "✅ Build úspěšný!"
    echo "📂 Aplikace: dist/Domácí úkoly.app"
    echo ""
    echo "💡 Pro spuštění: open \"dist/Domácí úkoly.app\""
    echo "💡 Pro instalaci: přesuň do /Applications"
else
    echo ""
    echo "❌ Build selhal!"
    exit 1
fi

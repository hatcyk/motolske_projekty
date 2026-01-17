#!/bin/bash
# Build script pro Linux

echo "🔨 Buildování aplikace pro Linux..."
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
echo "📦 Vytváření binárky..."
pyinstaller \
    --name="Domácí úkoly" \
    --windowed \
    --onefile \
    --add-data="ukoly:ukoly" \
    --add-data="gui:gui" \
    --add-data="tests:tests" \
    --add-data="cli_menu.py:." \
    --collect-all=flet \
    --exclude-module=flet.testing \
    --exclude-module=numpy \
    --noconfirm \
    main.py

# Kontrola úspěchu
if [ -f "dist/Domácí úkoly" ]; then
    echo ""
    echo "✅ Build úspěšný!"
    echo "📂 Aplikace: dist/Domácí úkoly"
    echo ""
    echo "💡 Pro spuštění: ./dist/Domácí\ úkoly"
    echo "💡 Nebo: chmod +x dist/Domácí\ úkoly && ./dist/Domácí\ úkoly"
else
    echo ""
    echo "❌ Build selhal!"
    exit 1
fi

# Changelog

Všechny významné změny v tomto projektu budou zdokumentovány v tomto souboru.

## [14. ledna 2026] - Zjednodušení názvů modulů + zvětšení okna

### 🔧 Změněno

- **Přejmenování GUI modulů** - odstraněn prefix `ukol_X_`:
  - `gui/ukol_1_trojuhelnik.py` → `gui/trojuhelnik.py`
  - `gui/ukol_2_pismeno_dne.py` → `gui/pismeno_dne.py`
  - `gui/ukol_3_sety.py` → `gui/sety.py`
  - `gui/ukol_4_data.py` → `gui/data.py`
  - `gui/ukol_5_kalkulacka.py` → `gui/kalkulacka.py`
  - `gui/ukol_6_bulls_cows.py` → `gui/bulls_cows.py`
  - `gui/ukol_7_tic_tac_toe.py` → `gui/tic_tac_toe.py`

- **Zvětšení GUI okna** pro seznam úkolů:
  - Launcher: 650x250 px (beze změny)
  - GUI menu: 700x600 px (bylo stejné jako launcher)
  - Automatické přepínání velikosti při přechodu mezi menu

- **Aktualizace importů** v `main.py`:
  - `from gui import trojuhelnik` místo `from gui import ukol_1_trojuhelnik`
  - Kratší a přehlednější názvy

---

## [Nedatováno] - Modularizace GUI

### ✨ Přidáno

#### 🎮 GUI pro hry
- **Bulls & Cows GUI** (`gui/bulls_cows.py`)
  - TextField pro 4-místné číslo s validací
  - ListView historie všech pokusů s bulls/cows
  - Živé počítadlo pokusů a času
  - České gramatické tvary (býk/býci/býků, kráva/krávy/krav)
  - Hodnocení výsledku (úžasné/průměrné/mohlo být lepší)
  - Tlačítko "Nová hra" pro restart
  - Zvýraznění výherního pokusu zelenou
  
- **Tic-tac-toe GUI** (`gui/tic_tac_toe.py`)
  - Interaktivní 3x3 grid tlačítek
  - Střídání hráčů O (modrá) a X (červená)
  - Detekce výhry (8 možných kombinací)
  - Zvýraznění výherní kombinace zelenou
  - Detekce remízy
  - Tlačítko "Nová hra" pro restart
  - České texty a gratulaice

#### 📁 Modularizace
- Nová složka `gui/` pro GUI moduly
- Separátní moduly pro každý úkol:
  - `gui/trojuhelnik.py` - Výpočet plochy trojúhelníku
  - `gui/pismeno_dne.py` - Hádání písmene
  - `gui/sety.py` - Placeholder
  - `gui/data.py` - Placeholder
  - `gui/kalkulacka.py` - Kalkulačka
  - `gui/bulls_cows.py` - Bulls & Cows hra
  - `gui/tic_tac_toe.py` - Tic-tac-toe hra

### 🔧 Změněno

- **Refaktorace `main.py`**
  - Odstraněny inline funkce `zobraz_ukol_X()`
  - Přidány importy GUI modulů
  - Volání `ukol_X_modul.zobraz_ukol(page, callback)` místo inline kódu
  - Čistší a přehlednější kód (~200 řádků méně)

- **Build skripty**
  - `build_macos.sh` - přidán `--add-data="gui:gui"`
  - `build_windows.bat` - přidán `--add-data="gui;gui"`
  - Nová složka `gui/` se nyní zahrnuje do buildu

- **README.md**
  - Aktualizována struktura projektu
  - Přidána dokumentace GUI her
  - Vylepšený popis funkcí

### 🎯 Technické detaily

**Bulls & Cows GUI**
- Validace vstupu (4 číslice, nezačíná 0, bez duplicit)
- Historie pokusů s číslem pokusu, tipu a výsledku
- Timer měřící čas od startu hry
- Detekce výhry při 4 bulls
- Enter klávesa pro potvrzení tipu

**Tic-tac-toe GUI**
- 3x3 grid Container s TextButton komponenty
- Logika detekce výhry (3x horizontální, 3x vertikální, 2x diagonální)
- Barevné odlišení hráčů (O modrá, X červená)
- Zvýraznění výherních políček zeleným pozadím
- Kontrola plné plochy pro remízu

### 📦 Struktura kódu

```
Před:
main.py (445 řádků)
  └─ inline funkce zobraz_ukol_1() až zobraz_ukol_7()

Po:
main.py (260 řádků)
  └─ importy z gui/*
gui/
  ├── ukol_1_trojuhelnik.py (76 řádků)
  ├── ukol_2_pismeno_dne.py (49 řádků)
  ├── ukol_3_sety.py (23 řádků)
  ├── ukol_4_data.py (23 řádků)
  ├── ukol_5_kalkulacka.py (91 řádků)
  ├── ukol_6_bulls_cows.py (237 řádků) 🎮
  └── ukol_7_tic_tac_toe.py (167 řádků) 🎮
```

### 🚀 Přínosy

1. **Modularita** - Každý úkol má vlastní soubor
2. **Udržitelnost** - Snadnější debugování a úpravy
3. **Rozšiřitelnost** - Přidání nového GUI jen vytvořením modulu
4. **Čistota** - `main.py` je nyní jen router
5. **Testovatelnost** - Moduly lze testovat samostatně

---

## [Starší] - Základní implementace

### ✨ Přidáno

- Základní GUI launcher s Flet
- CLI menu pro všech 7 úkolů
- České texty pro Bulls & Cows a Tic-tac-toe
- Build systém pro macOS (.app) a Windows (.exe)
- Dokumentace (README.md, BUILD.md, QUICKSTART.md)
- MIT licence

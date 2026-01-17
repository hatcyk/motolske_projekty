# Školní projekty - Domácí úkoly z Pythonu

Repositář obsahující různé školní projekty a domácí úkoly implementované v Pythonu s **GUI i CLI rozhraním**.

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![Flet](https://img.shields.io/badge/Flet-0.80+-purple.svg)](https://flet.dev/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Škola

**Střední průmyslová škola dopravní**  
[Oficiální web školy](https://www.sps-dopravni.cz/)

## Autor

**Jméno:** Štefan Barát  
**Email:** barat70671@mot.sps-dopravni.cz  
**Discord:** hatsukooo

## Domácí úkoly

Repositář obsahuje domácí úkoly z předmětu Programování (Python). Jednotlivé úkoly jsou umístěny v balíčku `ukoly/`.

### Dostupné úkoly

1. **Úkol 1** - Výpočet plochy trojúhelníku
2. **Úkol 2** - Hádání prvního písmene dne v týdnu
3. **Úkol 3** - Práce se sety a ověřování hesla
4. **Úkol 4** - Práce s daty (počítání výskytů, analýza textu)
5. **Úkol 5** - Kalkulačka a interaktivní programy
6. **Bulls & Cows** - Hra na hádání čtyřciferného čísla
7. **Tic-tac-toe** - Piškvorky pro dva hráče

### Spuštění

**Instalace závislostí:**
```bash
pip install -r requirements.txt
```

**Spuštění aplikace:**
```bash
python3 main.py
```

Program otevře GUI okno s výběrem rozhraní (bez konzole na pozadí):
- **Rozhraní CLI** - zavře GUI a otevře nový terminál s textovým menu
- **Rozhraní GUI** - zobrazí grafické rozhraní s 7 úkoly
  - ✅ Úkol 1, 2, 5 - plně funkční GUI
  - 🎮 **Bulls & Cows** - kompletní GUI s historií a časem
  - 🎮 **Tic-tac-toe** - interaktivní 3x3 grid s detekcí výhry
  - 📝 Úkol 3, 4 - dostupné pouze v CLI (GUI připravováno)
- **Konec** - ukončí aplikaci

**Alternativně - přímé spuštění CLI:**
```bash
python3 cli_menu.py
```

Po výběru CLI se zobrazí interaktivní menu s výběrem úkolů (1-7).

### Struktura projektu

```
├── main.py                     # GUI launcher (spouští se první)
├── cli_menu.py                 # CLI menu (textové rozhraní)
├── gui/                        # GUI moduly pro jednotlivé úkoly
│   ├── __init__.py
│   ├── trojuhelnik.py         # GUI pro trojúhelník
│   ├── pismeno_dne.py         # GUI pro hádání písmene
│   ├── sety.py                # GUI pro sety (placeholder)
│   ├── data.py                # GUI pro data (placeholder)
│   ├── kalkulacka.py          # GUI pro kalkulačku
│   ├── bulls_cows.py          # GUI pro Bulls & Cows hru 🎮
│   └── tic_tac_toe.py         # GUI pro Tic-tac-toe hru 🎮
├── ukoly/                      # Balíček s jednotlivými úkoly (CLI)
│   ├── __init__.py
│   ├── plocha_trojuhelniku.py # Výpočet plochy trojúhelníku
│   ├── hadani_pismene_dne.py  # Hádání prvního písmene dne
│   ├── prace_se_sety.py       # Práce se sety a ověřování
│   ├── prace_s_daty.py        # Analýza dat
│   ├── kalkulacka.py          # Kalkulačka a interaktivní programy
│   ├── bulls_and_cows.py      # Bulls & Cows hra
│   └── tic_tac_toe.py         # Tic-tac-toe piškvorky
├── requirements.txt
├── README.md
└── LICENSE
```

## Obecné požadavky

- Python 3.6+
- Flet (pro GUI rozhraní) - `pip install flet`
- PyInstaller (pro vytvoření standalone aplikace) - `pip install pyinstaller`

## 🎮 Implementované hry

### Bulls & Cows GUI
- 🎯 Hádání 4-místného čísla
- 📊 Historie všech pokusů
- ⏱️ Měření času
- 🇨🇿 České gramatické tvary
- ✨ Hodnocení výsledku

### Tic-tac-toe GUI
- 🎨 Interaktivní 3x3 grid
- 👥 Dva hráči (O vs X)
- 🏆 Detekce výhry a remízy
- 🎨 Barevné odlišení hráčů
- ✨ Zvýraznění výherní kombinace

## Licence

Tyto projekty jsou licencovány pod MIT licencí. Viz soubor [LICENSE](LICENSE) pro podrobnosti.
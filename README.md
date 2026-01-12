# Školní projekty

Repositář obsahující různé školní projekty a domácí úkoly implementované v Pythonu.

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

```bash
python3 main.py
```

Program zobrazí interaktivní menu s výběrem úkolů.

### Struktura projektu

```
├── main.py                     # Hlavní program s menu
├── ukoly/                      # Balíček s jednotlivými úkoly
│   ├── __init__.py
│   ├── plocha_trojuhelniku.py # Výpočet plochy trojúhelníku
│   ├── hadani_pismene_dne.py  # Hádání prvního písmene dne
│   ├── prace_se_sety.py       # Práce se sety a ověřování
│   ├── prace_s_daty.py        # Analýza dat
│   ├── kalkulacka.py          # Kalkulačka a interaktivní programy
│   ├── bulls_and_cows.py      # Bulls & Cows hra
│   └── tic_tac_toe.py         # Tic-tac-toe piškvorky
├── README.md
└── LICENSE
```

## Obecné požadavky

- Python 3.6+
- Žádné externí knihovny nejsou potřeba

## Licence

Tyto projekty jsou licencovány pod MIT licencí. Viz soubor [LICENSE](LICENSE) pro podrobnosti.
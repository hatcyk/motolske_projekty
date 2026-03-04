#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Úkol 14: Práce s JSON souborem
Autor: Štefan Barát
Škola: Střední průmyslová škola dopravní
"""

import json
import os


def najdi_zadane_klice(jmeno_souboru):
    """Otevře JSON soubor a vrátí list hodnot klíče 'jmeno'."""
    with open(jmeno_souboru, 'r', encoding='utf-8') as f:
        data = json.load(f)

    jmena = []
    for slovnik in data:
        if 'jmeno' in slovnik:
            jmena.append(slovnik['jmeno'])

    return jmena


def main():
    """Hlavní funkce - načte JSON a vypíše nalezená jména."""
    adresar = os.path.dirname(os.path.abspath(__file__))
    cesta = os.path.join(adresar, 'udaje.json')

    jmena = najdi_zadane_klice(cesta)
    print(jmena)


if __name__ == "__main__":
    main()

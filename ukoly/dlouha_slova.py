#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Zobrazení slov se 7 a více znaky ze souboru
Autor: Štefan Barát
Škola: Střední průmyslová škola dopravní
"""

import os


def zobraz_slova(textovy_soubor):
    """Přečte soubor a vrátí list slov obsahujících 7 a více znaků."""
    with open(textovy_soubor, "r", encoding="utf-8") as f:
        obsah = f.read()
    slova = obsah.split()
    return [slovo for slovo in slova if len(slovo) >= 7]


def spocitej_znaky(textovy_soubor):
    """Vrátí slovník {slovo: počet_znaků} pro všechna slova v souboru."""
    with open(textovy_soubor, "r", encoding="utf-8") as f:
        obsah = f.read()
    slova = obsah.split()
    return {slovo: len(slovo) for slovo in slova}


def nejdelsi_slovo(textovy_soubor):
    """Najde a vrátí nejdelší slovo v souboru."""
    with open(textovy_soubor, "r", encoding="utf-8") as f:
        obsah = f.read()
    slova = obsah.split()
    if not slova:
        return None
    return max(slova, key=len)


def prumerna_delka(textovy_soubor):
    """Spočítá průměrnou délku slov v souboru."""
    with open(textovy_soubor, "r", encoding="utf-8") as f:
        obsah = f.read()
    slova = obsah.split()
    if not slova:
        return 0
    return sum(len(s) for s in slova) / len(slova)


if __name__ == "__main__":
    adresar = os.path.dirname(os.path.abspath(__file__))
    cesta = os.path.join(adresar, "slova.txt")
    print(zobraz_slova(cesta))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Úkol 13: Práce s CSV souborem
Autor: Štefan Barát
Škola: Střední průmyslová škola dopravní
"""

import csv
import os


data = [
    [10, 'a1', 1],
    [12, 'a2', 3],
    [14, 'a3', 5],
    [16, 'a4', 7],
    [18, 'a5', 9]
]


def zapis_csv(cesta):
    """Zapíše data do CSV souboru."""
    with open(cesta, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)


def nacti_csv(cesta):
    """Načte obsah CSV souboru a vrátí ho jako string."""
    with open(cesta, 'r', encoding='utf-8') as f:
        csv_data = f.read()
    return csv_data


def main():
    """Hlavní funkce - zapíše a přečte CSV soubor."""
    adresar = os.path.dirname(os.path.abspath(__file__))
    cesta = os.path.join(adresar, 'nove.csv')

    zapis_csv(cesta)

    csv_data = nacti_csv(cesta)
    print(csv_data, end='')


if __name__ == "__main__":
    main()

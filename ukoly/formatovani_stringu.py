#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Formátování stringů a přesnost
Autor: Štefan Barát
Škola: Střední průmyslová škola dopravní
"""

import os


# Proměnné
kombinace = 1.234
presnost_str = "Hello"
presnost_cisla = 123.4567


def formatuj_presnost(cislo):
    """Naformátuje číslo do tvaru |1.23e+02|123.5|123.46|."""
    return f"|{cislo:.2e}|{cislo:.1f}|{cislo:.2f}|"


def formatuj_kombinaci(cislo):
    """Naformátuje číslo do tvaru |1.234$|."""
    return f"|{cislo}$|"


def formatuj_string(text, max_znaku=4):
    """Ořízne string na daný počet znaků ve tvaru |Hell|."""
    return f"|{text[:max_znaku]}|"


def zapis_do_souboru(soubor, formatovana_presnost, formatovana_kombinace, formatovana_presnost_str):
    """Zapíše naformátované hodnoty do textového souboru."""
    with open(soubor, "w", encoding="utf-8") as f:
        f.write(formatovana_presnost + "\n")
        f.write(formatovana_kombinace + "\n")
        f.write(formatovana_presnost_str + "\n")


def main():
    """Hlavní funkce pro formátování stringů."""
    formatovana_presnost = formatuj_presnost(presnost_cisla)
    formatovana_kombinace = formatuj_kombinaci(kombinace)
    formatovana_presnost_str = formatuj_string(presnost_str)

    print(f"Naformátovaná přesnost: {formatovana_presnost},")
    print(f"Naformátovaná kombinace: {formatovana_kombinace},")
    print(f"Naformátovaný string: {formatovana_presnost_str}.")

    # Zápis do souboru vedle tohoto skriptu
    adresar = os.path.dirname(os.path.abspath(__file__))
    cesta = os.path.join(adresar, "vysledek.txt")
    zapis_do_souboru(cesta, formatovana_presnost, formatovana_kombinace, formatovana_presnost_str)
    print("Zapisuji do souboru.")


if __name__ == "__main__":
    main()

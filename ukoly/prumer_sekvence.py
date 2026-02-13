#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Úkol: Výpočet průměru sekvence čísel
Autor: Štefan Barát
"""


def spocitej_prumer(sekvence):
    """Spočítá průměrnou hodnotu pro danou sekvenci číselných hodnot."""
    return sum(sekvence) / len(sekvence)


def main():
    """Hlavní funkce programu."""
    sekvence_cisel = [35, 14, 26, 48, 49, 26, 18, 25, 16, 16, 39, 17, 10, 29, 30]

    vysledek = spocitej_prumer(sekvence_cisel)

    print(vysledek)


if __name__ == "__main__":
    main()

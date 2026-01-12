#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Úkol 1: Výpočet plochy trojúhelníku
Autor: Štefan Barát
"""


def plocha_trojuhelniku():
    """Vypočítá plochu trojúhelníku na základě základny a výšky."""
    print("\n=== VÝPOČET PLOCHY TROJÚHELNÍKU ===")
    try:
        zakladna = float(input("Zadej základnu trojúhelníku: "))
        vyska = float(input("Zadej výšku trojúhelníku: "))
        plocha = (zakladna * vyska) / 2
        print(f"Plocha trojúhelníku je: {plocha}")
    except ValueError:
        print("Chyba: Zadej platné číslo!")


if __name__ == "__main__":
    plocha_trojuhelniku()

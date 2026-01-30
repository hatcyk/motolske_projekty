#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Úkol 8: Házení kostkou - Simulace hodu kostkou
# Autor: Štefan Barát

import random


def hazeni_kostkou():
    """Simuluje hod kostkou. Program hází dokud nepadne jiné číslo než 6."""
    print("\n=== SIMULACE HODU KOSTKOU ===\n")

    min_hodnota = 1
    max_hodnota = 6

    while True:
        print("Házím kostkou..")
        kostka_hodnota = random.randint(min_hodnota, max_hodnota)
        print(f"Na kostce je: {kostka_hodnota}")

        if kostka_hodnota != 6:
            break
        print()  # Prázdný řádek pro lepší čitelnost


if __name__ == "__main__":
    hazeni_kostkou()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Automatické testy pro Tic-tac-toe
"""

import sys
import os
import io

# Nastavení UTF-8 pro výstup (Windows fix)
# Pouze pokud sys.stdout existuje (v GUI buildu může být None)
if sys.platform == 'win32' and sys.stdout is not None and hasattr(sys.stdout, 'buffer'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Přidání parent directory do cesty pro import
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gui.tic_tac_toe import (
    vytvor_hraci_plochu,
    zkontroluj_vitezstvi,
    je_plocha_plna
)


def test_vytvor_hraci_plochu():
    """Test vytvoření hrací plochy."""
    vysledky = []

    # Test 1: Velikost plochy (9 polí)
    plocha = vytvor_hraci_plochu()
    test1 = len(plocha) == 9
    vysledky.append(("Velikost plochy je 9", test1))

    # Test 2: Všechna pole jsou prázdná
    test2 = all(plocha[i] == ' ' for i in range(1, 10))
    vysledky.append(("Všechna pole jsou prázdná", test2))

    # Test 3: Pole mají správné klíče (1-9)
    test3 = all(i in plocha for i in range(1, 10))
    vysledky.append(("Pole mají klíče 1-9", test3))

    return vysledky


def test_zkontroluj_vitezstvi():
    """Test kontroly vítězství."""
    vysledky = []

    # Test 1: Výhra v horní řadě (1, 2, 3)
    plocha = vytvor_hraci_plochu()
    plocha[1] = plocha[2] = plocha[3] = 'X'
    vyhral, kombinace = zkontroluj_vitezstvi(plocha, 'X')
    vysledky.append(("Výhra v horní řadě", vyhral and kombinace == [1, 2, 3]))

    # Test 2: Výhra ve středním řádku (4, 5, 6)
    plocha = vytvor_hraci_plochu()
    plocha[4] = plocha[5] = plocha[6] = 'O'
    vyhral, kombinace = zkontroluj_vitezstvi(plocha, 'O')
    vysledky.append(("Výhra ve středním řádku", vyhral and kombinace == [4, 5, 6]))

    # Test 3: Výhra v dolním řádku (7, 8, 9)
    plocha = vytvor_hraci_plochu()
    plocha[7] = plocha[8] = plocha[9] = 'X'
    vyhral, kombinace = zkontroluj_vitezstvi(plocha, 'X')
    vysledky.append(("Výhra v dolním řádku", vyhral and kombinace == [7, 8, 9]))

    # Test 4: Výhra v levém sloupci (1, 4, 7)
    plocha = vytvor_hraci_plochu()
    plocha[1] = plocha[4] = plocha[7] = 'O'
    vyhral, kombinace = zkontroluj_vitezstvi(plocha, 'O')
    vysledky.append(("Výhra v levém sloupci", vyhral and kombinace == [1, 4, 7]))

    # Test 5: Výhra ve středním sloupci (2, 5, 8)
    plocha = vytvor_hraci_plochu()
    plocha[2] = plocha[5] = plocha[8] = 'X'
    vyhral, kombinace = zkontroluj_vitezstvi(plocha, 'X')
    vysledky.append(("Výhra ve středním sloupci", vyhral and kombinace == [2, 5, 8]))

    # Test 6: Výhra v pravém sloupci (3, 6, 9)
    plocha = vytvor_hraci_plochu()
    plocha[3] = plocha[6] = plocha[9] = 'O'
    vyhral, kombinace = zkontroluj_vitezstvi(plocha, 'O')
    vysledky.append(("Výhra v pravém sloupci", vyhral and kombinace == [3, 6, 9]))

    # Test 7: Výhra na diagonále \ (1, 5, 9)
    plocha = vytvor_hraci_plochu()
    plocha[1] = plocha[5] = plocha[9] = 'X'
    vyhral, kombinace = zkontroluj_vitezstvi(plocha, 'X')
    vysledky.append(("Výhra na diagonále \\ (1, 5, 9)", vyhral and kombinace == [1, 5, 9]))

    # Test 8: Výhra na diagonále / (3, 5, 7)
    plocha = vytvor_hraci_plochu()
    plocha[3] = plocha[5] = plocha[7] = 'O'
    vyhral, kombinace = zkontroluj_vitezstvi(plocha, 'O')
    vysledky.append(("Výhra na diagonále / (3, 5, 7)", vyhral and kombinace == [3, 5, 7]))

    # Test 9: Žádná výhra - prázdná plocha
    plocha = vytvor_hraci_plochu()
    vyhral, kombinace = zkontroluj_vitezstvi(plocha, 'X')
    vysledky.append(("Žádná výhra - prázdná plocha", not vyhral and kombinace == []))

    # Test 10: Žádná výhra - částečně vyplněná plocha bez vítěze
    plocha = vytvor_hraci_plochu()
    plocha[1] = 'X'
    plocha[2] = 'O'
    plocha[5] = 'X'
    vyhral, kombinace = zkontroluj_vitezstvi(plocha, 'X')
    vysledky.append(("Žádná výhra - částečně vyplněná plocha", not vyhral and kombinace == []))

    # Test 11: Nesprávný hráč nevyhrává
    plocha = vytvor_hraci_plochu()
    plocha[1] = plocha[2] = plocha[3] = 'X'
    vyhral, _ = zkontroluj_vitezstvi(plocha, 'O')  # Kontrolujeme O, ale X má výhru
    vysledky.append(("Nesprávný hráč nevyhrává", not vyhral))

    return vysledky


def test_je_plocha_plna():
    """Test kontroly, zda je plocha plná (remíza)."""
    vysledky = []

    # Test 1: Prázdná plocha
    plocha = vytvor_hraci_plochu()
    test1 = not je_plocha_plna(plocha)
    vysledky.append(("Prázdná plocha není plná", test1))

    # Test 2: Částečně vyplněná plocha
    plocha = vytvor_hraci_plochu()
    plocha[1] = 'X'
    plocha[5] = 'O'
    test2 = not je_plocha_plna(plocha)
    vysledky.append(("Částečně vyplněná plocha není plná", test2))

    # Test 3: Plná plocha
    plocha = vytvor_hraci_plochu()
    for i in range(1, 10):
        plocha[i] = 'X' if i % 2 == 1 else 'O'
    test3 = je_plocha_plna(plocha)
    vysledky.append(("Plná plocha je plná", test3))

    # Test 4: Plná plocha s výhrou
    plocha = vytvor_hraci_plochu()
    # X X X
    # O O X
    # X O O
    plocha[1] = plocha[2] = plocha[3] = 'X'  # X vyhrává
    plocha[4] = plocha[5] = 'O'
    plocha[6] = plocha[7] = 'X'
    plocha[8] = plocha[9] = 'O'
    test4 = je_plocha_plna(plocha)
    vysledky.append(("Plná plocha s výhrou je stále plná", test4))

    return vysledky


def test_remiza_bez_viteze():
    """Test remízy - plná plocha bez vítěze."""
    vysledky = []

    # Test 1: Remíza - plná plocha bez vítěze
    # X O X
    # X O O
    # O X X
    plocha = vytvor_hraci_plochu()
    plocha[1] = 'X'
    plocha[2] = 'O'
    plocha[3] = 'X'
    plocha[4] = 'X'
    plocha[5] = 'O'
    plocha[6] = 'O'
    plocha[7] = 'O'
    plocha[8] = 'X'
    plocha[9] = 'X'

    je_plna = je_plocha_plna(plocha)
    x_vyhral, _ = zkontroluj_vitezstvi(plocha, 'X')
    o_vyhral, _ = zkontroluj_vitezstvi(plocha, 'O')

    test1 = je_plna and not x_vyhral and not o_vyhral
    vysledky.append(("Remíza - plná plocha bez vítěze", test1))

    return vysledky


def spust_vsechny_testy():
    """Spustí všechny testy a vrátí výsledky."""
    vsechny_vysledky = {}

    testy = [
        ("Vytvoření hrací plochy", test_vytvor_hraci_plochu),
        ("Kontrola vítězství", test_zkontroluj_vitezstvi),
        ("Kontrola plné plochy", test_je_plocha_plna),
        ("Remíza bez vítěze", test_remiza_bez_viteze),
    ]

    for nazev, test_funkce in testy:
        vsechny_vysledky[nazev] = test_funkce()

    return vsechny_vysledky


if __name__ == "__main__":
    print("=" * 60)
    print("Tic-tac-toe - Automatické testy")
    print("=" * 60)
    print()

    vysledky = spust_vsechny_testy()

    celkovy_uspech = 0
    celkovy_pocet = 0

    for kategorie, testy in vysledky.items():
        print(f"\n{kategorie}:")
        print("-" * 60)

        for nazev, uspech in testy:
            celkovy_pocet += 1
            if uspech:
                celkovy_uspech += 1
                print(f"  ✓ {nazev}")
            else:
                print(f"  ✗ {nazev}")

    print()
    print("=" * 60)
    print(f"Výsledek: {celkovy_uspech}/{celkovy_pocet} testů prošlo")

    if celkovy_uspech == celkovy_pocet:
        print("✓ VŠECHNY TESTY PROŠLY!")
    else:
        print(f"✗ {celkovy_pocet - celkovy_uspech} testů selhalo")

    print("=" * 60)

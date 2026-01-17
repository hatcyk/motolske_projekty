#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Automatické testy pro Bulls & Cows
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

from gui.bulls_cows import (
    generuj_tajne_cislo,
    validuj_vstup,
    vyhodnot_tip,
    formatuj_vysledek,
    hodnoceni_vysledku
)


def test_generuj_tajne_cislo():
    """Test generování tajného čísla."""
    vysledky = []

    # Test 1: Délka čísla
    cislo = generuj_tajne_cislo()
    test1 = len(cislo) == 4
    vysledky.append(("Délka čísla je 4", test1))

    # Test 2: Pouze číslice
    test2 = cislo.isdigit()
    vysledky.append(("Pouze číslice", test2))

    # Test 3: Nezačíná nulou
    test3 = cislo[0] != '0'
    vysledky.append(("Nezačíná nulou", test3))

    # Test 4: Všechny číslice jsou unikátní
    test4 = len(set(cislo)) == 4
    vysledky.append(("Unikátní číslice", test4))

    # Test 5: Generování více čísel (kontrola náhodnosti)
    cisla = [generuj_tajne_cislo() for _ in range(10)]
    test5 = len(set(cisla)) > 1  # Měla by být různá
    vysledky.append(("Různá čísla při opakovaném generování", test5))

    return vysledky


def test_validuj_vstup():
    """Test validace vstupu."""
    vysledky = []

    # Test 1: Platný vstup
    platny, _ = validuj_vstup("1234")
    vysledky.append(("Platný vstup '1234'", platny))

    # Test 2: Krátký vstup
    platny, _ = validuj_vstup("123")
    vysledky.append(("Odmítnutí krátkého vstupu", not platny))

    # Test 3: Dlouhý vstup
    platny, _ = validuj_vstup("12345")
    vysledky.append(("Odmítnutí dlouhého vstupu", not platny))

    # Test 4: Nečíselný vstup
    platny, _ = validuj_vstup("abcd")
    vysledky.append(("Odmítnutí nečíselného vstupu", not platny))

    # Test 5: Začíná nulou
    platny, _ = validuj_vstup("0123")
    vysledky.append(("Odmítnutí čísla začínajícího nulou", not platny))

    # Test 6: Duplicitní číslice
    platny, _ = validuj_vstup("1123")
    vysledky.append(("Odmítnutí duplicitních číslic", not platny))

    # Test 7: Číslo s nulou (ale nezačíná nulou)
    platny, _ = validuj_vstup("1023")
    vysledky.append(("Platné číslo s nulou (nezačíná nulou)", platny))

    return vysledky


def test_vyhodnot_tip():
    """Test vyhodnocení tipu."""
    vysledky = []

    tajne = "1234"

    # Test 1: Přesná shoda (4 bulls, 0 cows)
    bulls, cows = vyhodnot_tip(tajne, "1234")
    vysledky.append(("Přesná shoda (4 bulls, 0 cows)", bulls == 4 and cows == 0))

    # Test 2: Všechny špatně (0 bulls, 0 cows)
    bulls, cows = vyhodnot_tip(tajne, "5678")
    vysledky.append(("Všechny špatně (0 bulls, 0 cows)", bulls == 0 and cows == 0))

    # Test 3: Všechny správné číslice, špatné pozice (0 bulls, 4 cows)
    bulls, cows = vyhodnot_tip(tajne, "4321")
    vysledky.append(("Všechny správné číslice, špatné pozice (0 bulls, 4 cows)", bulls == 0 and cows == 4))

    # Test 4: Částečná shoda (2 bulls, 0 cows)
    bulls, cows = vyhodnot_tip(tajne, "1256")
    vysledky.append(("Částečná shoda (2 bulls, 0 cows)", bulls == 2 and cows == 0))

    # Test 5: Mix bulls a cows (1 bull, 2 cows)
    bulls, cows = vyhodnot_tip(tajne, "1425")
    vysledky.append(("Mix bulls a cows (1 bull, 2 cows)", bulls == 1 and cows == 2))

    # Test 6: Pouze cows (0 bulls, 2 cows)
    bulls, cows = vyhodnot_tip(tajne, "5612")
    vysledky.append(("Pouze cows (0 bulls, 2 cows)", bulls == 0 and cows == 2))

    return vysledky


def test_formatuj_vysledek():
    """Test formátování výsledku."""
    vysledky = []

    # Test 1: Jednotné číslo (1 býk, 1 kráva)
    vysledek = formatuj_vysledek(1, 1)
    vysledky.append(("Formátování '1 býk, 1 kráva'", vysledek == "1 býk, 1 kráva"))

    # Test 2: Množné číslo 2-4 (2 býci, 3 krávy)
    vysledek = formatuj_vysledek(2, 3)
    vysledky.append(("Formátování '2 býci, 3 krávy'", vysledek == "2 býci, 3 krávy"))

    # Test 3: Množné číslo 5+ (0 býků, 0 krav)
    vysledek = formatuj_vysledek(0, 0)
    vysledky.append(("Formátování '0 býků, 0 krav'", vysledek == "0 býků, 0 krav"))

    # Test 4: Maximální hodnota (4 býci, 0 krav) - výhra
    vysledek = formatuj_vysledek(4, 0)
    vysledky.append(("Formátování '4 býci, 0 krav'", vysledek == "4 býci, 0 krav"))

    return vysledky


def test_hodnoceni_vysledku():
    """Test hodnocení výsledku."""
    vysledky = []

    # Test 1: Výborné (≤4 pokusů)
    hodnoceni = hodnoceni_vysledku(4)
    vysledky.append(("Hodnocení pro 4 pokusy", hodnoceni == "úžasné"))

    # Test 2: Průměrné (5-7 pokusů)
    hodnoceni = hodnoceni_vysledku(6)
    vysledky.append(("Hodnocení pro 6 pokusů", hodnoceni == "průměrné"))

    # Test 3: Mohlo být lepší (8-10 pokusů)
    hodnoceni = hodnoceni_vysledku(9)
    vysledky.append(("Hodnocení pro 9 pokusů", hodnoceni == "mohlo být lepší"))

    # Test 4: Špatné (>10 pokusů)
    hodnoceni = hodnoceni_vysledku(15)
    vysledky.append(("Hodnocení pro 15 pokusů", hodnoceni == "zkus to příště lépe"))

    return vysledky


def spust_vsechny_testy():
    """Spustí všechny testy a vrátí výsledky."""
    vsechny_vysledky = {}

    testy = [
        ("Generování tajného čísla", test_generuj_tajne_cislo),
        ("Validace vstupu", test_validuj_vstup),
        ("Vyhodnocení tipu", test_vyhodnot_tip),
        ("Formátování výsledku", test_formatuj_vysledek),
        ("Hodnocení výsledku", test_hodnoceni_vysledku),
    ]

    for nazev, test_funkce in testy:
        vsechny_vysledky[nazev] = test_funkce()

    return vsechny_vysledky


if __name__ == "__main__":
    print("=" * 60)
    print("Bulls & Cows - Automatické testy")
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

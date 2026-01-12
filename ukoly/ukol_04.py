#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Úkol 4: Práce s daty - počítání výskytů a zpracování textu
Autor: Štefan Barát
"""


def pocitani_vyskytu():
    """Počítá výskyty prvků v seznamu a zobrazuje jejich frekvenci."""
    print("\n=== POČÍTÁNÍ VÝSKYTŮ V SEZNAMU ===")
    
    sequence = [1, 21, 5, 3, 5, 8, 321, 1, 2, 2, 32, 6, 9, 1, 4, 6, 3, 1, 2]
    print(f"Vstupní seznam: {sequence}")
    
    counts = {}
    
    for cislo in sequence:
        if cislo not in counts:
            counts[cislo] = 1
        else:
            counts[cislo] += 1
    
    print("\nVýsledky (seřazeno):")
    for key in sorted(counts.keys()):
        print(f"  {key}: {counts[key]}x")


def pocitani_samohlasek():
    """Počítá samohlásky a souhlásky v textu."""
    print("\n=== POČÍTÁNÍ SAMOHLÁSEK A SOUHLÁSEK ===")
    
    veta = 'Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu'
    print(f"Věta: {veta}")
    
    samohlasky = "aeiouyáěíóů"
    vysledek = {"souhlasky": 0, "samohlasky": 0}
    
    for znak in veta.lower():
        if not znak.isalpha():
            continue
        
        if znak in samohlasky:
            vysledek["samohlasky"] += 1
        else:
            vysledek["souhlasky"] += 1
    
    print(f"\nSouhlásky: {vysledek['souhlasky']}")
    print(f"Samohlásky: {vysledek['samohlasky']}")


def main():
    """Menu pro výběr úkolu."""
    while True:
        print("\n" + "="*50)
        print("ÚKOL 4: PRÁCE S DATY")
        print("="*50)
        print("1. Počítání výskytů v seznamu")
        print("2. Počítání samohlásek a souhlásek")
        print("0. Zpět")
        print("="*50)
        
        volba = input("\nVyberte (0-2): ")
        
        if volba == "1":
            pocitani_vyskytu()
        elif volba == "2":
            pocitani_samohlasek()
        elif volba == "0":
            break
        else:
            print("Neplatná volba!")
        
        if volba in ["1", "2"]:
            input("\nStiskni Enter pro pokračování...")


if __name__ == "__main__":
    main()

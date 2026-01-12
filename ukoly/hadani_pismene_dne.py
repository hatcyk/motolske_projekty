#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Úkol 2: Hádání prvního písmene dne v týdnu
Autor: Štefan Barát
"""


def hadani_pismene_dne():
    """Hádá první písmeno vybraného dne v týdnu."""
    tyden = ('pondělí', 'úterý', 'středa', 'čtvrtek', 'pátek', 'sobota', 'neděle')
    
    print("\n=== HÁDÁNÍ PRVNÍHO PÍSMENE DNE ===")
    print("Dny v týdnu:")
    for i, den in enumerate(tyden, 1):
        print(f"{i} - {den}")
    
    cislo_dne = input("\nVyber den v týdnu (1-7): ")

    if cislo_dne.isdigit() and 1 <= int(cislo_dne) <= 7:
        cislo_dne = int(cislo_dne)
        den = tyden[cislo_dne - 1]
        prvni_pismeno_dne = den[0]
        
        print(f'\nDen: {cislo_dne} --> "{den}"')
        
        tip_prvniho_pismena = input("Jaké je první písmeno tohoto dne?: ")
        
        if prvni_pismeno_dne == tip_prvniho_pismena:
            print(f"✓ Správně! Písmeno je '{prvni_pismeno_dne}'")
        else:
            print(f"✗ Špatně! Správné písmeno je '{prvni_pismeno_dne}', ty jsi zadal '{tip_prvniho_pismena}'")
    else:
        print("\n✗ Chyba: Zadej číslo od 1 do 7!")


if __name__ == "__main__":
    hadani_pismene_dne()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Úkol 3: Práce se sety - rozdíl, sjednocení a ověřování hesla
Autor: Štefan Barát
"""


def rozdil_setu():
    """Vypočítá rozdíl mezi dvěma sety."""
    print("\n=== ÚLOHA 1: ROZDÍL SETŮ ===")
    
    numbers_1 = {1, 2, 3, 4}
    numbers_2 = {3, 4, 5, 6}
    
    nums_1_differences = numbers_1 - numbers_2
    
    print(f"Set 1: {numbers_1}")
    print(f"Set 2: {numbers_2}")
    print(f"Rozdílné hodnoty Set 1 vs Set 2: {nums_1_differences}")


def sjednoceni_setu():
    """Sjednocuje dva sety."""
    print("\n=== ÚLOHA 2: SJEDNOCENÍ SETŮ ===")
    
    numbers_1 = {1, 2, 3, 4}
    numbers_2 = {3, 4, 5, 6}
    
    all_numbers = numbers_1 | numbers_2
    
    print(f"Set 1: {numbers_1}")
    print(f"Set 2: {numbers_2}")
    print(f"Sjednocené hodnoty: {all_numbers}")


def overeni_hesla():
    """Ověřuje přihlašovací údaje."""
    print("\n=== ÚLOHA 3: OVĚŘENÍ HESLA ===")
    
    spravne_heslo = "tajne123"
    pokus = 3
    
    while pokus > 0:
        heslo = input("Zadej heslo: ")
        
        if heslo == spravne_heslo:
            print("✓ Heslo je správné! Jsi přihlášen/a.")
            return
        else:
            pokus -= 1
            if pokus > 0:
                print(f"✗ Špatné heslo! Zbývá {pokus} pokus/pokusů.")
            else:
                print("✗ Vyčerpali jsi všechny pokusy!")


def main():
    """Spustí všechny úlohy."""
    rozdil_setu()
    sjednoceni_setu()
    overeni_hesla()


if __name__ == "__main__":
    main()

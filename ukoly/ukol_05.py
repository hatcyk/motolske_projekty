#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Úkol 5: Kalkulačka, výběr ovoce a slova se čtyřmi znaky
Autor: Štefan Barát
"""


def kalkulacka():
    """Jednoduchá kalkulačka pro základní operace."""
    print("\n=== KALKULAČKA ===")
    while True:
        print("\nOperace: +, -, *, /")
        operace = input("Vyber si operaci: ").strip()
        
        if operace not in ["+", "-", "*", "/"]:
            print("Neplatný operátor!")
            continue
        
        try:
            number_1 = float(input("Zadej první číslo: "))
            number_2 = float(input("Zadej druhé číslo: "))
            
            if operace == "+":
                vysledek = number_1 + number_2
            elif operace == "-":
                vysledek = number_1 - number_2
            elif operace == "*":
                vysledek = number_1 * number_2
            elif operace == "/":
                if number_2 == 0:
                    print("Chyba: Dělení nulou!")
                    continue
                vysledek = number_1 / number_2
            
            print(f"\n{number_1} {operace} {number_2} = {vysledek}")
            
        except ValueError:
            print("Chyba: Zadej platné číslo!")
            continue
        
        dalsi = input("\nChceš provést další operaci? (a/n): ")
        if dalsi.lower() != 'a':
            break


def vyber_ovoce():
    """Umožňuje vybrat ovoce z dostupné nabídky."""
    print("\n=== VÝBĚR OVOCE ===")
    ovoce = ["jablko", "banán", "citron", "pomeranč"]
    
    print("Dostupné ovoce: " + ", ".join(ovoce))
    
    while True:
        vyber = input("\nVyber ovoce: ").lower().strip()
        
        if vyber not in ovoce:
            print("Toto ovoce není v nabídce!")
        else:
            print(f"✓ Bezva! Vybral/a sis '{vyber}'.")
            break


def slova_ctyrznaky():
    """Sbírá slova se čtyřmi znaky, maximálně 3 slova."""
    print("\n=== SBÍRÁNÍ SLOV SE ČTYŘMI ZNAKY ===")
    print("Zadej 3 slova dlouhá přesně 4 znaky.")
    
    slova = []
    
    while len(slova) < 3:
        vstup = input(f"\nSlovo {len(slova) + 1}/3: ").strip()
        
        if len(vstup) != 4:
            print(f"✗ Slovo '{vstup}' nemá 4 znaky (má {len(vstup)})!")
            continue
        
        if vstup in slova:
            print(f"✗ Slovo '{vstup}' už je uložené!")
            continue
        
        slova.append(vstup)
        print(f"✓ Slovo '{vstup}' uloženo!")
    
    print(f"\n✓ Hotovo! Uložená slova: {', '.join(slova)}")


def main():
    """Hlavní menu pro výběr úkolu."""
    while True:
        print("\n" + "="*50)
        print("ÚKOL 5: INTERAKTIVNÍ PROGRAMY")
        print("="*50)
        print("1. Kalkulačka")
        print("2. Výběr ovoce")
        print("3. Sbírání slov")
        print("0. Zpět")
        print("="*50)
        
        volba = input("\nVyberte (0-3): ")
        
        if volba == "1":
            kalkulacka()
        elif volba == "2":
            vyber_ovoce()
        elif volba == "3":
            slova_ctyrznaky()
        elif volba == "0":
            break
        else:
            print("Neplatná volba!")


if __name__ == "__main__":
    main()

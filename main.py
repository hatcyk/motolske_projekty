#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Domácí úkoly z Pythonu - Hlavní menu
Autor: Štefan Barát
Škola: Střední průmyslová škola dopravní
"""

from ukoly import ukol_01, ukol_02, ukol_03, ukol_04, ukol_05


def vypis_header():
    """Zobrazí úvodní zprávu."""
    print("\n" + "="*60)
    print(" "*15 + "DOMÁCÍ ÚKOLY Z PYTHONU")
    print("="*60)
    print("Autor: Štefan Barát")
    print("Škola: Střední průmyslová škola dopravní")
    print("="*60 + "\n")


def hlavni_menu():
    """Hlavní menu pro výběr úkolu."""
    while True:
        print("\n" + "="*60)
        print("SEZNAM ÚKOLŮ")
        print("="*60)
        print("1. Výpočet plochy trojúhelníku")
        print("2. Hádání prvního písmene dne v týdnu")
        print("3. Práce se sety a ověřování hesla")
        print("4. Práce s daty - počítání výskytů")
        print("5. Kalkulačka a interaktivní programy")
        print("-"*60)
        print("0. Konec")
        print("="*60)
        
        volba = input("\nVyberte úkol (0-5): ").strip()
        
        if volba == "1":
            ukol_01.plocha_trojuhelniku()
        elif volba == "2":
            ukol_02.hadani_pismene_dne()
        elif volba == "3":
            ukol_03.main()
        elif volba == "4":
            ukol_04.main()
        elif volba == "5":
            ukol_05.main()
        elif volba == "0":
            print("\n" + "="*60)
            print("Děkuji za použití! Na shledanou! 👋")
            print("="*60 + "\n")
            break
        else:
            print("\n✗ Neplatná volba! Zkus znovu.")
        
        if volba in ["1", "2"]:
            input("\nStiskni Enter pro návrat do menu...")


def main():
    """Spuštění programu."""
    vypis_header()
    hlavni_menu()


if __name__ == "__main__":
    main()

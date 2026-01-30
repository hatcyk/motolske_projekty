#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# CLI rozhraní pro domácí úkoly

import os
import sys
from ukoly import plocha_trojuhelniku, hadani_pismene_dne, prace_se_sety, prace_s_daty, kalkulacka, bulls_and_cows, tic_tac_toe, hazeni_kostkou


def vycisti_terminal():
    # Vyčistí terminál.
    os.system('cls' if sys.platform == 'win32' else 'clear')


def vypis_header():
    # Zobrazí úvodní zprávu.
    print("\n" + "="*60)
    print(" "*15 + "DOMÁCÍ ÚKOLY Z PYTHONU")
    print("="*60)
    print("Autor: Štefan Barát")
    print("Škola: Střední průmyslová škola dopravní")
    print("="*60 + "\n")


def hlavni_menu():
    # Hlavní menu pro výběr úkolu.
    while True:
        print("\n" + "="*60)
        print("SEZNAM ÚKOLŮ")
        print("="*60)
        print("1. Výpočet plochy trojúhelníku")
        print("2. Hádání prvního písmene dne v týdnu")
        print("3. Práce se sety a ověřování hesla")
        print("4. Práce s daty - počítání výskytů")
        print("5. Kalkulačka a interaktivní programy")
        print("6. Bulls & Cows - hádání čísla")
        print("7. Tic-tac-toe - piškvorky")
        print("8. Házení kostkou - simulace hodu")
        print("-"*60)
        print("0. Konec")
        print("="*60)

        volba = input("\nVyberte úkol (0-8): ").strip()
        
        if volba == "1":
            vycisti_terminal()
            plocha_trojuhelniku.plocha_trojuhelniku()
            input("\nStiskni Enter pro návrat do menu...")
            vycisti_terminal()
        elif volba == "2":
            vycisti_terminal()
            hadani_pismene_dne.hadani_pismene_dne()
            input("\nStiskni Enter pro návrat do menu...")
            vycisti_terminal()
        elif volba == "3":
            vycisti_terminal()
            prace_se_sety.main()
            input("\nStiskni Enter pro návrat do menu...")
            vycisti_terminal()
        elif volba == "4":
            vycisti_terminal()
            prace_s_daty.main()
            input("\nStiskni Enter pro návrat do menu...")
            vycisti_terminal()
        elif volba == "5":
            vycisti_terminal()
            kalkulacka.main()
            input("\nStiskni Enter pro návrat do menu...")
            vycisti_terminal()
        elif volba == "6":
            vycisti_terminal()
            bulls_and_cows.main()
            input("\nStiskni Enter pro návrat do menu...")
            vycisti_terminal()
        elif volba == "7":
            vycisti_terminal()
            tic_tac_toe.main()
            input("\nStiskni Enter pro návrat do menu...")
            vycisti_terminal()
        elif volba == "8":
            vycisti_terminal()
            hazeni_kostkou.hazeni_kostkou()
            input("\nStiskni Enter pro návrat do menu...")
            vycisti_terminal()
        elif volba == "0":
            print("\n" + "="*60)
            print("Děkuji za použití! Na shledanou! 👋")
            print("="*60 + "\n")
            break
        else:
            print("\n✗ Neplatná volba! Zkus znovu.")


if __name__ == "__main__":
    vypis_header()
    hlavni_menu()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CLI rozhraní pro domácí úkoly
"""

from ukoly import plocha_trojuhelniku, hadani_pismene_dne, prace_se_sety, prace_s_daty, kalkulacka, bulls_and_cows, tic_tac_toe, prumer_sekvence, overeni_os, extrakce_emailu, formatovani_stringu, dlouha_slova, csv_soubor, json_soubor


def vypis_header():
    """Zobrazí úvodní zprávu."""
    print("\n" + "="*60)
    print(" "*15 + "DOMÁCÍ ÚKOLY Z PYTHONU")
    print("="*60)
    print("Autor: Štefan Barát Prezident")
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
        print("6. Bulls & Cows - hádání čísla")
        print("7. Tic-tac-toe - piškvorky")
        print("8. Průměr sekvence čísel")
        print("9. Ověření operačního systému")
        print("10. Extrakce emailů z textu")
        print("11. Formátování stringů a přesnost")
        print("12. Dlouhá slova ze souboru")
        print("13. Práce s CSV souborem")
        print("14. Práce s JSON souborem")
        print("-"*60)
        print("0. Konec")
        print("="*60)

        volba = input("\nVyberte úkol (0-14): ").strip()
        
        if volba == "1":
            plocha_trojuhelniku.plocha_trojuhelniku()
        elif volba == "2":
            hadani_pismene_dne.hadani_pismene_dne()
        elif volba == "3":
            prace_se_sety.main()
        elif volba == "4":
            prace_s_daty.main()
        elif volba == "5":
            kalkulacka.main()
        elif volba == "6":
            bulls_and_cows.main()
        elif volba == "7":
            tic_tac_toe.main()
        elif volba == "8":
            prumer_sekvence.main()
        elif volba == "9":
            overeni_os.main()
        elif volba == "10":
            extrakce_emailu.main()
        elif volba == "11":
            formatovani_stringu.main()
        elif volba == "12":
            import os
            cesta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ukoly", "slova.txt")
            print(dlouha_slova.zobraz_slova(cesta))
        elif volba == "13":
            csv_soubor.main()
        elif volba == "14":
            json_soubor.main()
        elif volba == "0":
            print("\n" + "="*60)
            print("Děkuji za použití! Na shledanou! 👋")
            print("="*60 + "\n")
            break
        else:
            print("\n✗ Neplatná volba! Zkus znovu.")
        
        if volba in ["1", "2", "8", "9", "10", "11", "12", "13", "14"]:
            input("\nStiskni Enter pro návrat do menu...")


if __name__ == "__main__":
    vypis_header()
    hlavni_menu()

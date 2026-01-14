#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tic-tac-toe - Piškvorky pro dva hráče
Autor: Štefan Barát
Email: barat70671@mot.sps-dopravni.cz
Discord: hatsukooo
"""


def zobraz_uvod():
    """Zobrazí úvodní text a pravidla hry."""
    print("\nVítej ve hře Piškvorky (Tic Tac Toe)")
    print("=" * 44)
    print("PRAVIDLA HRY:")
    print("Každý hráč může umístit jednu značku")
    print("(O nebo X) na hrací plochu 3x3.")
    print("VÍTĚZ je ten, kdo jako první umístí")
    print("tři své značky do:")
    print("* horizontální řady,")
    print("* vertikální řady nebo")
    print("* diagonální řady")
    print("=" * 44)
    print("Začínáme hru")
    print("-" * 44)


def vytvor_hraci_plochu():
    """Vytvoří prázdnou hrací plochu 3x3."""
    return {i: ' ' for i in range(1, 10)}


def zobraz_plochu(plocha):
    """Zobrazí aktuální stav hrací plochy."""
    print("+---+---+---+")
    print(f"| {plocha[1]} | {plocha[2]} | {plocha[3]} |")
    print("+---+---+---+")
    print(f"| {plocha[4]} | {plocha[5]} | {plocha[6]} |")
    print("+---+---+---+")
    print(f"| {plocha[7]} | {plocha[8]} | {plocha[9]} |")
    print("+---+---+---+")


def zkontroluj_vitezstvi(plocha, hrac):
    """Zkontroluje, jestli hráč vyhrál."""
    # Všechny možné výherní kombinace
    vyherni_kombinace = [
        [1, 2, 3],  # horní řada
        [4, 5, 6],  # střední řada
        [7, 8, 9],  # dolní řada
        [1, 4, 7],  # levý sloupec
        [2, 5, 8],  # střední sloupec
        [3, 6, 9],  # pravý sloupec
        [1, 5, 9],  # diagonála \
        [3, 5, 7]   # diagonála /
    ]
    
    for kombinace in vyherni_kombinace:
        if all(plocha[pos] == hrac for pos in kombinace):
            return True
    return False


def je_plocha_plna(plocha):
    """Zkontroluje, jestli je plocha plná (remíza)."""
    return all(plocha[i] != ' ' for i in range(1, 10))


def validuj_tah(plocha, vstup):
    """Validuje tah hráče."""
    # Kontrola, jestli je vstup číslo
    if not vstup.isdigit():
        return False, "Zadej platné číslo!"
    
    pozice = int(vstup)
    
    # Kontrola rozsahu
    if pozice < 1 or pozice > 9:
        return False, "Zadej číslo od 1 do 9!"
    
    # Kontrola, jestli je pole volné
    if plocha[pozice] != ' ':
        return False, "Toto pole je již obsazené!"
    
    return True, ""


def hraj_tic_tac_toe():
    """Hlavní herní smyčka."""
    zobraz_uvod()
    
    plocha = vytvor_hraci_plochu()
    aktualni_hrac = 'O'
    
    zobraz_plochu(plocha)
    
    while True:
        print("=" * 44)
        vstup = input(f"Hráč {aktualni_hrac} | Zadej číslo pole (1-9): ").strip()
        print("=" * 44)
        
        # Validace tahu
        platny, chyba = validuj_tah(plocha, vstup)
        if not platny:
            print(f"✗ {chyba}")
            continue
        
        # Provedení tahu
        pozice = int(vstup)
        plocha[pozice] = aktualni_hrac
        
        # Zobrazení nového stavu
        zobraz_plochu(plocha)
        
        # Kontrola výhry
        if zkontroluj_vitezstvi(plocha, aktualni_hrac):
            print("=" * 44)
            print(f"Gratulujeme, hráč {aktualni_hrac} VYHRÁL!")
            print("=" * 44)
            break
        
        # Kontrola remízy
        if je_plocha_plna(plocha):
            print("=" * 44)
            print("Remíza! Hra skončila nerozhodně!")
            print("=" * 44)
            break
        
        # Přepnutí hráče
        aktualni_hrac = 'X' if aktualni_hrac == 'O' else 'O'


def main():
    """Hlavní funkce s možností opakování hry."""
    while True:
        hraj_tic_tac_toe()
        
        opakovat = input("\nChceš hrát znovu? (a/n): ").strip().lower()
        if opakovat != 'a':
            print("\nDíky za hru! 🎮")
            break


if __name__ == "__main__":
    main()

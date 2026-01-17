#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GUI modul - Úkol 7: Tic-tac-toe (Piškvorky)
"""

import flet as ft


def vytvor_hraci_plochu():
    """Vytvoří prázdnou hrací plochu 3x3."""
    return {i: ' ' for i in range(1, 10)}


def zkontroluj_vitezstvi(plocha, hrac):
    """Zkontroluje, jestli hráč vyhrál. Vrátí (vyhrál, výherní kombinace)."""
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
            return True, kombinace
    return False, []


def je_plocha_plna(plocha):
    """Zkontroluje, jestli je plocha plná (remíza)."""
    return all(plocha[i] != ' ' for i in range(1, 10))


def zobraz_ukol(page: ft.Page, zpet_callback):
    """
    Zobrazí GUI pro hru Tic-tac-toe.
    
    Args:
        page: Flet Page objekt
        zpet_callback: Funkce pro návrat zpět
    """
    # Herní stav
    plocha = vytvor_hraci_plochu()
    aktualni_hrac = 'O'
    hra_aktivni = True
    vyherni_pozice = []
    
    # GUI komponenty
    stav_text = ft.Text(
        "Hráč O - Tvůj tah!",
        size=18,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE_700
    )
    
    # Slovník pro tlačítka (mapování pozice -> tlačítko)
    tlacitka = {}
    
    def klik_na_pole(pozice):
        """Handler pro kliknutí na pole."""
        nonlocal aktualni_hrac, hra_aktivni, vyherni_pozice
        
        if not hra_aktivni or plocha[pozice] != ' ':
            return
        
        # Provedení tahu
        plocha[pozice] = aktualni_hrac

        # Aktualizace textu v tlačítku
        tlacitka[pozice].value = aktualni_hrac
        tlacitka[pozice].color = ft.Colors.BLUE if aktualni_hrac == 'O' else ft.Colors.RED
        page.update()
        
        # Kontrola výhry
        vyhrál, vyherni_pozice = zkontroluj_vitezstvi(plocha, aktualni_hrac)
        if vyhrál:
            # Zvýraznění výherní kombinace zelenou barvou textu
            for pos in vyherni_pozice:
                tlacitka[pos].color = ft.Colors.GREEN
            
            stav_text.value = f"Gratulujeme, hráč {aktualni_hrac} VYHRÁL!"
            stav_text.color = ft.Colors.GREEN
            hra_aktivni = False
            page.update()
            return
        
        # Kontrola remízy
        if je_plocha_plna(plocha):
            stav_text.value = "Remíza! Hra skončila nerozhodně!"
            stav_text.color = ft.Colors.ORANGE
            hra_aktivni = False
            page.update()
            return
        
        # Přepnutí hráče
        aktualni_hrac = 'X' if aktualni_hrac == 'O' else 'O'
        stav_text.value = f"Hráč {aktualni_hrac} - Tvůj tah!"
        stav_text.color = ft.Colors.BLUE_700 if aktualni_hrac == 'O' else ft.Colors.RED_700
        
        page.update()
    
    def nova_hra(e):
        """Reset hry."""
        nonlocal plocha, aktualni_hrac, hra_aktivni, vyherni_pozice
        
        plocha = vytvor_hraci_plochu()
        aktualni_hrac = 'O'
        hra_aktivni = True
        vyherni_pozice = []
        
        # Reset všech tlačítek
        for pozice in range(1, 10):
            tlacitka[pozice].value = ""
            tlacitka[pozice].color = None
        
        stav_text.value = "Hráč O - Tvůj tah!"
        stav_text.color = ft.Colors.BLUE_700
        
        page.update()
    
    # Vytvoření 3x3 gridu tlačítek
    def vytvor_tlacitko(pozice):
        """Vytvoří tlačítko pro pozici."""
        text_control = ft.Text("", size=32, weight=ft.FontWeight.BOLD)

        btn = ft.ElevatedButton(
            content=text_control,
            on_click=lambda e: klik_na_pole(pozice),
            width=90,
            height=90,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
                padding=ft.padding.all(0),
            ),
        )

        # Uložení reference
        tlacitka[pozice] = text_control
        return btn
    
    # Vytvoření gridu
    grid = ft.Column([
        ft.Row([
            vytvor_tlacitko(1),
            vytvor_tlacitko(2),
            vytvor_tlacitko(3),
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            vytvor_tlacitko(4),
            vytvor_tlacitko(5),
            vytvor_tlacitko(6),
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            vytvor_tlacitko(7),
            vytvor_tlacitko(8),
            vytvor_tlacitko(9),
        ], alignment=ft.MainAxisAlignment.CENTER),
    ], spacing=5)
    
    # Zvětšení okna pro lepší zobrazení
    page.window.height = 700
    page.update()

    # Hlavní layout
    page.add(
        ft.Container(height=10),
        ft.Row([
            ft.Icon(ft.Icons.GRID_3X3, size=32, color=ft.Colors.PURPLE),
            ft.Text("Piškvorky (Tic-tac-toe)", size=24, weight=ft.FontWeight.BOLD),
        ], spacing=10),
        ft.Container(height=10),
        stav_text,
        ft.Container(height=20),
        grid,
        ft.Container(height=20),
        ft.Row([
            ft.Text("Hráč O:", size=14, color=ft.Colors.BLUE, weight=ft.FontWeight.BOLD),
            ft.Text("modrá", size=14, color=ft.Colors.BLUE),
            ft.Text(" | ", size=14),
            ft.Text("Hráč X:", size=14, color=ft.Colors.RED, weight=ft.FontWeight.BOLD),
            ft.Text("červená", size=14, color=ft.Colors.RED),
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Container(height=10),
        ft.Row([
            ft.Button("Nová hra", on_click=nova_hra, width=150, icon=ft.Icons.REFRESH),
            ft.Button("Zpět", on_click=lambda e: zpet_callback(), width=150, icon=ft.Icons.ARROW_BACK),
        ], spacing=10, alignment=ft.MainAxisAlignment.CENTER)
    )

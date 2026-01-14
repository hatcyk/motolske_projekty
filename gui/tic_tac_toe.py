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
        tlacitka[pozice].text = aktualni_hrac
        tlacitka[pozice].style = ft.ButtonStyle(
            color=ft.Colors.BLUE if aktualni_hrac == 'O' else ft.Colors.RED
        )
        
        # Kontrola výhry
        vyhrál, vyherni_pozice = zkontroluj_vitezstvi(plocha, aktualni_hrac)
        if vyhrál:
            # Zvýraznění výherní kombinace
            for pos in vyherni_pozice:
                tlacitka[pos].bgcolor = ft.Colors.GREEN_100
            
            stav_text.value = f"🎉 Gratulujeme, hráč {aktualni_hrac} VYHRÁL!"
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
            tlacitka[pozice].text = ""
            tlacitka[pozice].bgcolor = None
            tlacitka[pozice].style = None
        
        stav_text.value = "Hráč O - Tvůj tah!"
        stav_text.color = ft.Colors.BLUE_700
        
        page.update()
    
    # Vytvoření 3x3 gridu tlačítek
    def vytvor_tlacitko(pozice):
        """Vytvoří tlačítko pro pozici."""
        btn = ft.Container(
            content=ft.TextButton(
                text="",
                on_click=lambda e: klik_na_pole(pozice),
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=5),
                ),
                width=80,
                height=80,
            ),
            width=90,
            height=90,
            alignment=ft.alignment.center
        )
        # Uložení reference na vnitřní TextButton
        tlacitka[pozice] = btn.content
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
    
    # Hlavní layout
    page.add(
        ft.Container(height=10),
        ft.Text("Piškvorky (Tic-tac-toe) ⭕❌", size=24, weight=ft.FontWeight.BOLD),
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
            ft.Button("🔄 Nová hra", on_click=nova_hra, width=150),
            ft.Button("← Zpět", on_click=lambda e: zpet_callback(), width=150),
        ], spacing=10, alignment=ft.MainAxisAlignment.CENTER)
    )

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GUI modul - Úkol 6: Bulls & Cows
"""

import flet as ft
import random
import time


def generuj_tajne_cislo():
    """Vygeneruje náhodné 4-místné číslo s unikátními číslicemi (nezačíná 0)."""
    cislice = list(range(10))
    
    # První číslo nesmí být 0
    prvni = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
    cislice.remove(prvni)
    
    # Zbývající tři číslice
    zbytek = random.sample(cislice, 3)
    
    return str(prvni) + ''.join(map(str, zbytek))


def validuj_vstup(tip):
    """Zkontroluje, jestli je zadaný tip platný."""
    # Kontrola délky
    if len(tip) != 4:
        return False, "Zadej přesně 4 číslice!"
    
    # Kontrola, jestli jsou všechny znaky číslice
    if not tip.isdigit():
        return False, "Zadej pouze čísla!"
    
    # Kontrola, jestli nezačíná nulou
    if tip[0] == '0':
        return False, "Číslo nesmí začínat nulou!"
    
    # Kontrola duplicit
    if len(set(tip)) != 4:
        return False, "Číslo nesmí obsahovat duplicity!"
    
    return True, ""


def vyhodnot_tip(tajne_cislo, tip):
    """Vyhodnotí tip a vrátí počet bulls a cows."""
    bulls = 0
    cows = 0
    
    for i in range(4):
        if tip[i] == tajne_cislo[i]:
            bulls += 1
        elif tip[i] in tajne_cislo:
            cows += 1
    
    return bulls, cows


def formatuj_vysledek(bulls, cows):
    """Naformátuje výsledek s gramaticky správným tvarem."""
    # České gramatické tvary
    if bulls == 1:
        bull_text = "býk"
    elif 2 <= bulls <= 4:
        bull_text = "býci"
    else:
        bull_text = "býků"
    
    if cows == 1:
        cow_text = "kráva"
    elif 2 <= cows <= 4:
        cow_text = "krávy"
    else:
        cow_text = "krav"
    
    return f"{bulls} {bull_text}, {cows} {cow_text}"


def hodnoceni_vysledku(pokusy):
    """Vrátí hodnocení na základě počtu pokusů."""
    if pokusy <= 4:
        return "úžasné"
    elif pokusy <= 7:
        return "průměrné"
    elif pokusy <= 10:
        return "mohlo být lepší"
    else:
        return "zkus to příště lépe"


def zobraz_ukol(page: ft.Page, zpet_callback):
    """
    Zobrazí GUI pro hru Bulls & Cows.
    
    Args:
        page: Flet Page objekt
        zpet_callback: Funkce pro návrat zpět
    """
    # Herní stav
    tajne_cislo = generuj_tajne_cislo()
    pokusy = 0
    start_cas = time.time()
    historie = []
    
    # GUI komponenty
    tip_input = ft.TextField(
        label="Zadej 4-místné číslo",
        width=250,
        keyboard_type=ft.KeyboardType.NUMBER,
        max_length=4,
        autofocus=True
    )
    
    stav_text = ft.Text(
        "Vygeneroval jsem náhodné 4-místné číslo. Zkus ho uhodnout!",
        size=14,
        color=ft.Colors.BLUE_700
    )
    
    pokusy_text = ft.Text("Pokusů: 0", size=14, weight=ft.FontWeight.BOLD)
    cas_text = ft.Text("Čas: 0s", size=14, weight=ft.FontWeight.BOLD)
    
    chyba_text = ft.Text("", size=14, color=ft.Colors.RED)
    
    # ListView pro historii pokusů
    historie_list = ft.ListView(
        expand=True,
        spacing=5,
        padding=10,
        height=200
    )
    
    def aktualizuj_cas():
        """Aktualizuje zobrazený čas."""
        if stav_text.value != "Gratulujeme! Uhodl jsi číslo! 🎉":
            cas = int(time.time() - start_cas)
            cas_text.value = f"Čas: {cas}s"
            page.update()
    
    def nova_hra(e):
        """Reset hry."""
        nonlocal tajne_cislo, pokusy, start_cas, historie
        tajne_cislo = generuj_tajne_cislo()
        pokusy = 0
        start_cas = time.time()
        historie = []
        
        tip_input.value = ""
        tip_input.disabled = False
        stav_text.value = "Vygeneroval jsem nové číslo. Zkus ho uhodnout!"
        stav_text.color = ft.Colors.BLUE_700
        pokusy_text.value = "Pokusů: 0"
        cas_text.value = "Čas: 0s"
        chyba_text.value = ""
        historie_list.controls.clear()
        page.update()
    
    def over_tip(e):
        """Ověří tip uživatele."""
        nonlocal pokusy
        
        tip = tip_input.value.strip()
        
        # Validace vstupu
        platny, chyba = validuj_vstup(tip)
        if not platny:
            chyba_text.value = f"❌ {chyba}"
            page.update()
            return
        
        chyba_text.value = ""
        pokusy += 1
        
        # Vyhodnocení
        bulls, cows = vyhodnot_tip(tajne_cislo, tip)
        vysledek = formatuj_vysledek(bulls, cows)
        
        # Přidání do historie
        historie_item = ft.Container(
            content=ft.Row([
                ft.Text(f"#{pokusy}", size=14, weight=ft.FontWeight.BOLD, width=40),
                ft.Text(tip, size=16, weight=ft.FontWeight.BOLD, width=80),
                ft.Text("→", size=14, width=30),
                ft.Text(vysledek, size=14, color=ft.Colors.GREEN if bulls == 4 else ft.Colors.ORANGE),
            ]),
            bgcolor=ft.Colors.GREEN_50 if bulls == 4 else ft.Colors.GREY_100,
            border_radius=5,
            padding=10
        )
        historie_list.controls.insert(0, historie_item)
        
        # Aktualizace stavu
        pokusy_text.value = f"Pokusů: {pokusy}"
        aktualizuj_cas()
        
        if bulls == 4:
            # Výhra!
            konec_cas = time.time()
            cas_hry = int(konec_cas - start_cas)
            
            stav_text.value = "Gratulujeme! Uhodl jsi číslo! 🎉"
            stav_text.color = ft.Colors.GREEN
            tip_input.disabled = True
            
            # Zobrazení detailů výhry
            chyba_text.value = f"✓ Správně na {pokusy} pokusů! To je {hodnoceni_vysledku(pokusy)}!"
            chyba_text.color = ft.Colors.GREEN
            cas_text.value = f"Čas: {cas_hry}s"
        else:
            tip_input.value = ""
        
        page.update()
    
    # Event handler pro Enter v TextField
    tip_input.on_submit = over_tip
    
    # Hlavní layout
    page.add(
        ft.Container(height=10),
        ft.Text("Bulls & Cows 🐮", size=24, weight=ft.FontWeight.BOLD),
        ft.Container(height=10),
        stav_text,
        ft.Container(height=10),
        ft.Row([pokusy_text, cas_text], spacing=20),
        ft.Container(height=10),
        ft.Row([
            tip_input,
            ft.Button("Zkontrolovat", on_click=over_tip, width=150),
        ], spacing=10),
        chyba_text,
        ft.Container(height=10),
        ft.Text("Historie pokusů:", size=16, weight=ft.FontWeight.BOLD),
        ft.Container(
            content=historie_list,
            border=ft.border.all(1, ft.Colors.GREY_300),
            border_radius=5,
            height=200
        ),
        ft.Container(height=10),
        ft.Row([
            ft.Button("🔄 Nová hra", on_click=nova_hra, width=150),
            ft.Button("← Zpět", on_click=lambda e: zpet_callback(), width=150),
        ], spacing=10)
    )

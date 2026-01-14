#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GUI modul - Úkol 2: Hádání prvního písmene dne
"""

import flet as ft
import datetime


def zobraz_ukol(page: ft.Page, zpet_callback):
    """
    Zobrazí GUI pro hádání prvního písmene dne.
    
    Args:
        page: Flet Page objekt
        zpet_callback: Funkce pro návrat zpět
    """
    vysledek = ft.Text("Zkus uhodnout první písmeno dnešního dne!", size=16)
    pismeno_input = ft.TextField(label="Zadej písmeno", width=200, max_length=1)
    
    def kontrola(e):
        """Kontrola správnosti hádu."""
        dny = ["pondělí", "úterý", "středa", "čtvrtek", "pátek", "sobota", "neděle"]
        dnesni_den = dny[datetime.datetime.now().weekday()]
        prvni_pismeno = dnesni_den[0].lower()
        
        if pismeno_input.value and pismeno_input.value.lower() == prvni_pismeno:
            vysledek.value = f"✓ Správně! Dnes je {dnesni_den}."
            vysledek.color = ft.Colors.GREEN
        else:
            vysledek.value = "❌ Zkus to znovu!"
            vysledek.color = ft.Colors.RED
        page.update()
    
    page.add(
        ft.Container(height=10),
        ft.Text("Hádání prvního písmene dne", size=24, weight=ft.FontWeight.BOLD),
        ft.Container(height=10),
        vysledek,
        ft.Container(height=10),
        pismeno_input,
        ft.Button("Zkontrolovat", on_click=kontrola, width=200),
        ft.Container(height=20),
        ft.Button("← Zpět", on_click=lambda e: zpet_callback(), width=200)
    )

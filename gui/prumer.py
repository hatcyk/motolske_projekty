#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GUI modul - Průměr sekvence čísel
"""

import flet as ft
import random


def zobraz_ukol(page: ft.Page, zpet_callback):
    """
    Zobrazí GUI pro výpočet průměru sekvence.

    Args:
        page: Flet Page objekt
        zpet_callback: Funkce pro návrat zpět
    """
    from ukoly.prumer_sekvence import spocitej_prumer

    # Výchozí sekvence
    sekvence_cisel = [35, 14, 26, 48, 49, 26, 18, 25, 16, 16, 39, 17, 10, 29, 30]

    # UI komponenty
    sekvence_text = ft.Text(str(sekvence_cisel), size=14, color=ft.Colors.GREY_700)
    vysledek_text = ft.Text(
        f"Průměr: {spocitej_prumer(sekvence_cisel)}",
        size=18,
        color=ft.Colors.GREEN,
        weight=ft.FontWeight.BOLD
    )

    # Input pro vlastní sekvenci
    vlastni_input = ft.TextField(
        label="Vlastní čísla (oddělená čárkou)",
        hint_text="např. 10, 20, 30, 40",
        width=400
    )
    chyba_text = ft.Text("", color=ft.Colors.RED, size=14)

    def nova_nahodna_sekvence(e):
        """Vygeneruje novou náhodnou sekvenci."""
        nonlocal sekvence_cisel
        pocet = random.randint(10, 20)
        sekvence_cisel = [random.randint(1, 100) for _ in range(pocet)]
        sekvence_text.value = str(sekvence_cisel)
        vysledek_text.value = f"Průměr: {spocitej_prumer(sekvence_cisel)}"
        chyba_text.value = ""
        page.update()

    def pouzit_vlastni(e):
        """Použije vlastní sekvenci z inputu."""
        nonlocal sekvence_cisel
        try:
            vstup = vlastni_input.value.strip()
            if not vstup:
                chyba_text.value = "Zadej nějaká čísla!"
                page.update()
                return
            sekvence_cisel = [int(x.strip()) for x in vstup.split(",")]
            if len(sekvence_cisel) == 0:
                chyba_text.value = "Zadej alespoň jedno číslo!"
                page.update()
                return
            sekvence_text.value = str(sekvence_cisel)
            vysledek_text.value = f"Průměr: {spocitej_prumer(sekvence_cisel)}"
            chyba_text.value = ""
        except ValueError:
            chyba_text.value = "Neplatný formát! Použij čísla oddělená čárkou."
        page.update()

    page.add(
        ft.Container(height=10),
        ft.Text("Průměr sekvence čísel", size=24, weight=ft.FontWeight.BOLD),
        ft.Container(height=20),
        ft.Text("Sekvence čísel:", size=16),
        sekvence_text,
        ft.Container(height=10),
        vysledek_text,
        ft.Container(height=20),
        ft.Divider(),
        ft.Container(height=10),
        ft.Text("Vytvořit novou sekvenci:", size=16, weight=ft.FontWeight.BOLD),
        ft.Container(height=10),
        ft.Button("Generovat náhodnou sekvenci", on_click=nova_nahodna_sekvence, width=300),
        ft.Container(height=15),
        vlastni_input,
        ft.Button("Použít vlastní sekvenci", on_click=pouzit_vlastni, width=300),
        chyba_text,
        ft.Container(height=20),
        ft.Button("← Zpět", on_click=lambda e: zpet_callback(), width=200)
    )

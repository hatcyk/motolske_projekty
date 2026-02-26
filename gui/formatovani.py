#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GUI modul pro formátování stringů a přesnost
Autor: Štefan Barát
"""

import os
import flet as ft
from ukoly.formatovani_stringu import (
    formatuj_presnost, formatuj_kombinaci, formatuj_string,
    zapis_do_souboru, kombinace, presnost_str, presnost_cisla
)


def zobraz_ukol(page: ft.Page, zpet_callback):
    """Zobrazí GUI pro formátování stringů."""

    # Inputy s výchozími hodnotami
    input_cislo = ft.TextField(label="Číslo pro přesnost", value=str(presnost_cisla), width=300)
    input_kombinace = ft.TextField(label="Číslo pro kombinaci", value=str(kombinace), width=300)
    input_string = ft.TextField(label="String k oříznutí", value=presnost_str, width=300)
    input_max_znaku = ft.TextField(label="Max znaků (oříznutí)", value="4", width=150)

    vysledek_presnost = ft.Text("", size=16, selectable=True)
    vysledek_kombinace = ft.Text("", size=16, selectable=True)
    vysledek_string = ft.Text("", size=16, selectable=True)
    status_text = ft.Text("", size=14, color=ft.Colors.GREEN)

    def formatuj(e):
        """Naformátuje všechny hodnoty."""
        try:
            cislo = float(input_cislo.value)
            komb = float(input_kombinace.value)
            text = input_string.value
            max_z = int(input_max_znaku.value)

            fp = formatuj_presnost(cislo)
            fk = formatuj_kombinaci(komb)
            fs = formatuj_string(text, max_z)

            vysledek_presnost.value = f"Naformátovaná přesnost: {fp},"
            vysledek_presnost.color = None
            vysledek_kombinace.value = f"Naformátovaná kombinace: {fk},"
            vysledek_kombinace.color = None
            vysledek_string.value = f"Naformátovaný string: {fs}."
            vysledek_string.color = None
            status_text.value = ""
        except ValueError:
            vysledek_presnost.value = "Chyba: Zadej platná čísla!"
            vysledek_presnost.color = ft.Colors.RED
            vysledek_kombinace.value = ""
            vysledek_string.value = ""
            status_text.value = ""
        page.update()

    def zapis(e):
        """Zapíše výsledky do souboru vysledek.txt."""
        try:
            cislo = float(input_cislo.value)
            komb = float(input_kombinace.value)
            text = input_string.value
            max_z = int(input_max_znaku.value)

            fp = formatuj_presnost(cislo)
            fk = formatuj_kombinaci(komb)
            fs = formatuj_string(text, max_z)

            adresar = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            cesta = os.path.join(adresar, "ukoly", "vysledek.txt")
            zapis_do_souboru(cesta, fp, fk, fs)
            status_text.value = f"Zapisuji do souboru. ({cesta})"
            status_text.color = ft.Colors.GREEN
        except ValueError:
            status_text.value = "Chyba: Zadej platná čísla!"
            status_text.color = ft.Colors.RED
        page.update()

    def pouzit_vychozi(e):
        """Obnoví výchozí hodnoty ze zadání."""
        input_cislo.value = str(presnost_cisla)
        input_kombinace.value = str(kombinace)
        input_string.value = presnost_str
        input_max_znaku.value = "4"
        vysledek_presnost.value = ""
        vysledek_kombinace.value = ""
        vysledek_string.value = ""
        status_text.value = ""
        page.update()

    page.add(
        ft.Text("Formátování stringů a přesnost", size=24, weight=ft.FontWeight.BOLD),
        ft.Container(height=10),
        ft.Row([input_cislo, input_kombinace], spacing=10),
        ft.Row([input_string, input_max_znaku], spacing=10),
        ft.Container(height=10),
        ft.Row([
            ft.Button("Formátovat", on_click=formatuj, icon=ft.Icons.FORMAT_SHAPES),
            ft.Button("Zapsat do souboru", on_click=zapis, icon=ft.Icons.SAVE),
            ft.Button("Výchozí hodnoty", on_click=pouzit_vychozi, icon=ft.Icons.RESTORE),
        ], spacing=10),
        ft.Container(height=10),
        ft.Container(
            content=ft.Column([vysledek_presnost, vysledek_kombinace, vysledek_string]),
            bgcolor=ft.Colors.GREY_900,
            padding=15,
            border_radius=8,
        ),
        status_text,
        ft.Container(height=10),
        ft.Button("← Zpět", on_click=lambda e: zpet_callback()),
    )

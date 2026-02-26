#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GUI modul pro zobrazení dlouhých slov ze souboru
Autor: Štefan Barát
"""

import os
import flet as ft
from ukoly.dlouha_slova import zobraz_slova, spocitej_znaky, nejdelsi_slovo, prumerna_delka


def zobraz_ukol(page: ft.Page, zpet_callback):
    """Zobrazí GUI pro filtrování slov ze souboru."""

    vychozi_cesta = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "ukoly", "slova.txt")
    soubor_existuje = os.path.exists(vychozi_cesta)

    input_min_delka = ft.TextField(label="Minimální délka slova", value="7", width=200)
    vysledek_text = ft.Text("", size=14, selectable=True)
    statistiky_text = ft.Text("", size=14, selectable=True)
    status_text = ft.Text("", size=14)

    # Seznam slov z vlastního vstupu
    input_vlastni_slova = ft.TextField(
        label="Vlastní slova (oddělená čárkou nebo novým řádkem)",
        width=500, multiline=True, min_lines=3, max_lines=6
    )

    def nacti_soubor(e):
        """Načte slova ze souboru slova.txt a zobrazí výsledky."""
        try:
            min_delka = int(input_min_delka.value)
        except ValueError:
            status_text.value = "Chyba: Minimální délka musí být číslo!"
            status_text.color = ft.Colors.RED
            page.update()
            return

        if not os.path.exists(vychozi_cesta):
            status_text.value = f"Soubor nenalezen: {vychozi_cesta}"
            status_text.color = ft.Colors.RED
            page.update()
            return

        # Načtení slov
        with open(vychozi_cesta, "r", encoding="utf-8") as f:
            obsah = f.read()
        vsechna_slova = obsah.split()
        filtrovana = [s for s in vsechna_slova if len(s) >= min_delka]

        vysledek_text.value = str(filtrovana)
        vysledek_text.color = ft.Colors.GREEN if filtrovana else ft.Colors.ORANGE

        # Statistiky
        nejdelsi = nejdelsi_slovo(vychozi_cesta)
        prumer = prumerna_delka(vychozi_cesta)
        statistiky_text.value = (
            f"Celkem slov: {len(vsechna_slova)} | "
            f"Filtrováno ({min_delka}+ znaků): {len(filtrovana)} | "
            f"Nejdelší: {nejdelsi} ({len(nejdelsi)} zn.) | "
            f"Průměrná délka: {prumer:.1f}"
        )
        status_text.value = f"Načteno ze souboru: {vychozi_cesta}"
        status_text.color = ft.Colors.GREEN
        page.update()

    def filtruj_vlastni(e):
        """Filtruje vlastní zadaná slova."""
        try:
            min_delka = int(input_min_delka.value)
        except ValueError:
            status_text.value = "Chyba: Minimální délka musí být číslo!"
            status_text.color = ft.Colors.RED
            page.update()
            return

        text = input_vlastni_slova.value.strip()
        if not text:
            status_text.value = "Zadej vlastní slova!"
            status_text.color = ft.Colors.ORANGE
            page.update()
            return

        # Rozděl podle čárek nebo nových řádků
        if "," in text:
            slova = [s.strip() for s in text.split(",") if s.strip()]
        else:
            slova = [s.strip() for s in text.split() if s.strip()]

        filtrovana = [s for s in slova if len(s) >= min_delka]

        vysledek_text.value = str(filtrovana)
        vysledek_text.color = ft.Colors.GREEN if filtrovana else ft.Colors.ORANGE

        # Statistiky
        if slova:
            nejdelsi = max(slova, key=len)
            prumer = sum(len(s) for s in slova) / len(slova)
            statistiky_text.value = (
                f"Celkem slov: {len(slova)} | "
                f"Filtrováno ({min_delka}+ znaků): {len(filtrovana)} | "
                f"Nejdelší: {nejdelsi} ({len(nejdelsi)} zn.) | "
                f"Průměrná délka: {prumer:.1f}"
            )
        status_text.value = "Filtrováno z vlastního vstupu"
        status_text.color = ft.Colors.GREEN
        page.update()

    page.add(
        ft.Text("Dlouhá slova ze souboru", size=24, weight=ft.FontWeight.BOLD),
        ft.Container(height=10),
        ft.Row([
            input_min_delka,
            ft.Button("Načíst ze souboru slova.txt", on_click=nacti_soubor, icon=ft.Icons.FILE_OPEN,
                       visible=soubor_existuje),
        ], spacing=10),
        ft.Container(height=10),
        input_vlastni_slova,
        ft.Button("Filtrovat vlastní slova", on_click=filtruj_vlastni, icon=ft.Icons.FILTER_LIST),
        ft.Container(height=10),
        ft.Text("Výsledek:", size=16, weight=ft.FontWeight.BOLD),
        ft.Container(
            content=vysledek_text,
            bgcolor=ft.Colors.GREY_200,
            padding=15,
            border_radius=8,
            width=600,
        ),
        statistiky_text,
        status_text,
        ft.Container(height=10),
        ft.Button("← Zpět", on_click=lambda e: zpet_callback()),
    )

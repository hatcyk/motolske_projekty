#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GUI modul - Úkol 13: Práce s CSV souborem
Autor: Štefan Barát
"""

import os
import flet as ft
from ukoly.csv_soubor import zapis_csv, nacti_csv


def zobraz_ukol(page: ft.Page, zpet_callback):
    """Zobrazí GUI pro práci s CSV souborem."""

    vystup = ft.Text("", size=15, selectable=True, font_family="monospace")
    status_text = ft.Text("", size=13, color=ft.Colors.GREEN)

    def spustit(e):
        adresar = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ukoly')
        cesta = os.path.join(adresar, 'nove.csv')

        zapis_csv(cesta)
        csv_data = nacti_csv(cesta)

        vystup.value = csv_data.strip()
        status_text.value = f"Soubor uložen: {cesta}"
        status_text.color = ft.Colors.GREEN
        page.update()

    page.add(
        ft.Text("Práce s CSV souborem", size=24, weight=ft.FontWeight.BOLD),
        ft.Container(height=10),
        ft.Button("Spustit úkol", on_click=spustit, icon=ft.Icons.PLAY_ARROW),
        ft.Container(height=10),
        ft.Container(
            content=vystup,
            bgcolor=ft.Colors.GREY_200,
            padding=15,
            border_radius=8,
        ),
        status_text,
        ft.Container(height=10),
        ft.Button("← Zpět", on_click=lambda e: zpet_callback()),
    )

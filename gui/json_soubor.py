#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GUI modul - Úkol 14: Práce s JSON souborem
Autor: Štefan Barát
"""

import os
import flet as ft
from ukoly.json_soubor import najdi_zadane_klice


def zobraz_ukol(page: ft.Page, zpet_callback):
    """Zobrazí GUI pro práci s JSON souborem."""

    vystup = ft.Text("", size=15, selectable=True)
    status_text = ft.Text("", size=13, color=ft.Colors.RED)

    def spustit(e):
        adresar = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ukoly')
        cesta = os.path.join(adresar, 'udaje.json')

        if not os.path.exists(cesta):
            status_text.value = f"Soubor nenalezen: {cesta}"
            status_text.color = ft.Colors.RED
            page.update()
            return

        jmena = najdi_zadane_klice(cesta)
        vystup.value = str(jmena)
        status_text.value = ""
        page.update()

    page.add(
        ft.Text("Práce s JSON souborem", size=24, weight=ft.FontWeight.BOLD),
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

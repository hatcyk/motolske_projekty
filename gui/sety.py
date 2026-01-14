#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GUI modul - Úkol 3: Práce se sety
"""

import flet as ft


def zobraz_ukol(page: ft.Page, zpet_callback):
    """
    Zobrazí GUI pro práci se sety.
    
    Args:
        page: Flet Page objekt
        zpet_callback: Funkce pro návrat zpět
    """
    page.add(
        ft.Container(height=10),
        ft.Text("Práce se sety", size=24, weight=ft.FontWeight.BOLD),
        ft.Container(height=10),
        ft.Text("Tento úkol je dostupný pouze v CLI režimu.", size=16),
        ft.Text("(GUI implementace bude přidána později)", size=14, color=ft.Colors.GREY),
        ft.Container(height=20),
        ft.Button("← Zpět", on_click=lambda e: zpet_callback(), width=200)
    )

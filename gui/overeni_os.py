#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GUI modul - Ověření operačního systému
"""

import flet as ft


def zobraz_ukol(page: ft.Page, zpet_callback):
    """
    Zobrazí GUI pro ověření operačního systému.

    Args:
        page: Flet Page objekt
        zpet_callback: Funkce pro návrat zpět
    """
    from ukoly.overeni_os import je_os_windows
    import sys

    je_windows = je_os_windows()
    platforma = sys.platform

    if je_windows:
        status_text = "Ano, toto je Windows"
        status_color = ft.Colors.GREEN
        icon = ft.Icons.CHECK_CIRCLE
    else:
        status_text = "Ne, toto není Windows"
        status_color = ft.Colors.ORANGE
        icon = ft.Icons.INFO

    page.add(
        ft.Container(height=10),
        ft.Text("Ověření operačního systému", size=24, weight=ft.FontWeight.BOLD),
        ft.Container(height=20),
        ft.Row([
            ft.Icon(icon, color=status_color, size=40),
            ft.Text(status_text, size=18, color=status_color, weight=ft.FontWeight.BOLD)
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Container(height=10),
        ft.Text(f"Platforma: {platforma}", size=14, color=ft.Colors.GREY_700),
        ft.Text(f"je_os_windows() = {je_windows}", size=14, color=ft.Colors.GREY_700),
        ft.Container(height=30),
        ft.Button("← Zpět", on_click=lambda e: zpet_callback(), width=200)
    )

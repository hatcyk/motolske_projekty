#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GUI modul - Extrakce emailů z textu
"""

import flet as ft


def zobraz_ukol(page: ft.Page, zpet_callback):
    """
    Zobrazí GUI pro extrakci emailů z textu.

    Args:
        page: Flet Page objekt
        zpet_callback: Funkce pro návrat zpět
    """
    from ukoly.extrakce_emailu import uloz_emailove_adresy

    text = """Lorem ipsum dolor sit amet, consectetur adipiscing
elit. Mauris vulputate lacus id eros consequat tempus.
Nam viverra velit sit amet lorem lobortis, at tincidunt
nunc ultricies. Duis facilisis ultrices lacus, id
tiger123@email.cz auctor massa molestie at. Nunc tristique
fringilla congue. Donec ante diam cnn@info.com, dapibus
lacinia vulputate vitae, ullamcorper in justo. Maecenas
massa purus, ultricies a dictum ut, dapibus vitae massa.
Cras abc@gmail.com vel libero felis. In augue elit, porttitor
nec molestie quis, auctor a quam. Quisque b2b@money.fr
pretium dolor et tempor feugiat. Morbi libero lectus,
porttitor eu mi sed, luctus lacinia risus. Maecenas posuere
leo sit amet spam@info.cz. elit tincidunt maximus. Aliquam
erat volutpat. Donec eleifend felis at leo ullamcorper cursus.
Pellentesque id dui viverra, auctor enim ut, fringilla est.
Maecenas gravida turpis nec ultrices aliquet."""

    emaily = uloz_emailove_adresy(text)

    email_list = ft.Column([
        ft.Text(f"• {email}", size=14) for email in emaily
    ])

    page.add(
        ft.Container(height=10),
        ft.Text("Extrakce emailů z textu", size=24, weight=ft.FontWeight.BOLD),
        ft.Container(height=20),
        ft.Text(f"Nalezeno {len(emaily)} emailů:", size=16, weight=ft.FontWeight.BOLD),
        ft.Container(height=10),
        email_list,
        ft.Container(height=20),
        ft.Text("Výstup funkce:", size=14, color=ft.Colors.GREY_700),
        ft.Text(str(emaily), size=12, color=ft.Colors.GREEN),
        ft.Container(height=30),
        ft.Button("← Zpět", on_click=lambda e: zpet_callback(), width=200)
    )

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# GUI modul - Úkol 8: Házení kostkou - Simulace hodu kostkou

import flet as ft
import random
import time
import asyncio


def zobraz_ukol(page: ft.Page, zpet_callback):
    """Zobrazí GUI pro simulaci hodu kostkou.

    Args:
        page: Flet Page objekt
        zpet_callback: Funkce pro návrat zpět
    """
    # Historie hodů
    historie = []

    # UI elementy
    vysledek_text = ft.Text("", size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)
    kostka_text = ft.Text("🎲", size=80, text_align=ft.TextAlign.CENTER)
    historie_list = ft.Column([], scroll=ft.ScrollMode.AUTO, height=200)
    pocet_hodu_text = ft.Text("Počet hodů: 0", size=14, color=ft.Colors.GREY_700)

    btn_hazet = ft.Button(
        "🎲 Hodit kostkou",
        on_click=lambda e: asyncio.create_task(hazej_kostkou()),
        width=200,
        height=50,
        disabled=False
    )

    async def hazej_kostkou():
        """Simuluje hod kostkou s animací."""
        nonlocal historie

        # Disable tlačítko během házení
        btn_hazet.disabled = True
        page.update()

        # Vyčistí předchozí výsledek
        vysledek_text.value = "Házím kostkou.."
        vysledek_text.color = ft.Colors.BLUE
        kostka_text.value = "🎲"
        page.update()

        min_hodnota = 1
        max_hodnota = 6
        hody_serie = []

        while True:
            # Animace házení (3 rychlé změny)
            for _ in range(3):
                kostka_text.value = f"🎲 {random.randint(1, 6)}"
                page.update()
                await asyncio.sleep(0.1)

            # Finální hod
            kostka_hodnota = random.randint(min_hodnota, max_hodnota)
            kostka_text.value = f"🎲 {kostka_hodnota}"

            # Emoji podle hodnoty
            emoji_kostka = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"][kostka_hodnota - 1]
            kostka_text.value = f"{emoji_kostka} {kostka_hodnota}"

            hody_serie.append(kostka_hodnota)

            # Přidá do historie
            if kostka_hodnota == 6:
                vysledek_text.value = f"Na kostce je: {kostka_hodnota} - Házím znovu!"
                vysledek_text.color = ft.Colors.ORANGE
            else:
                vysledek_text.value = f"Na kostce je: {kostka_hodnota} - Konec!"
                vysledek_text.color = ft.Colors.GREEN

            page.update()

            if kostka_hodnota != 6:
                break

            await asyncio.sleep(0.8)

        # Aktualizace historie
        historie.append(hody_serie)
        pocet_hodu_text.value = f"Počet sérií: {len(historie)}"

        # Zobrazení série v historii
        serie_text = " → ".join(str(h) for h in hody_serie)
        historie_list.controls.insert(0,
            ft.Container(
                content=ft.Text(f"Serie #{len(historie)}: {serie_text}", size=12),
                padding=5,
                bgcolor=ft.Colors.GREY_900 if len(historie) % 2 == 0 else ft.Colors.GREY_800,
                border_radius=5
            )
        )

        # Enable tlačítko
        btn_hazet.disabled = False
        page.update()

    def vymazat_historii(e):
        """Vymaže historii hodů."""
        nonlocal historie
        historie = []
        historie_list.controls.clear()
        pocet_hodu_text.value = "Počet sérií: 0"
        vysledek_text.value = ""
        kostka_text.value = "🎲"
        page.update()

    page.add(
        ft.Container(height=10),
        ft.Text("🎲 Házení kostkou", size=24, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
        ft.Container(height=10),
        ft.Text("Program hází dokud nepadne jiné číslo než 6", size=12, color=ft.Colors.GREY_600, text_align=ft.TextAlign.CENTER),
        ft.Container(height=20),
        kostka_text,
        ft.Container(height=10),
        vysledek_text,
        ft.Container(height=20),
        btn_hazet,
        ft.Container(height=10),
        ft.Row([
            pocet_hodu_text,
            ft.Button("🗑 Vymazat historii", on_click=vymazat_historii, height=35)
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Container(height=10),
        ft.Text("📊 Historie sérií:", size=14, weight=ft.FontWeight.BOLD),
        ft.Container(height=5),
        historie_list,
        ft.Container(height=20),
        ft.Button("← Zpět", on_click=lambda e: zpet_callback(), width=200)
    )

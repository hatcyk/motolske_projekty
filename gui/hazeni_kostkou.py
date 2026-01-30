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
    # Nastavení okna a zabránění scrollování
    page.window.width = 750
    page.window.height = 720
    page.scroll = None
    page.padding = 20
    page.update()

    # Historie hodů
    historie = []

    # UI elementy
    vysledek_text = ft.Text("", size=18, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)
    kostka_icon = ft.Icon(ft.Icons.CASINO, size=80, color=ft.Colors.WHITE)
    kostka_hodnota_text = ft.Text("", size=48, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)

    # Historie s viditelným scrollbarem a borderem - roztažená na celou šířku
    historie_list = ft.Column([], scroll=ft.ScrollMode.ADAPTIVE, spacing=5)
    historie_container = ft.Container(
        content=historie_list,
        height=235,
        width=710,  # Šířka okna (750) - padding (20*2)
        border=ft.border.all(1, ft.Colors.GREY_700),
        border_radius=8,
        padding=10,
        bgcolor=ft.Colors.with_opacity(0.02, ft.Colors.WHITE)
    )

    pocet_hodu_text = ft.Text("Počet sérií: 0", size=13, color=ft.Colors.GREY_600)

    btn_hazet = ft.Button(
        "Hodit kostkou",
        icon=ft.Icons.CASINO,
        on_click=lambda e: asyncio.create_task(hazej_kostkou()),
        width=180,
        height=50,
        disabled=False
    )

    btn_vymazat = ft.Button(
        "Vymazat",
        icon=ft.Icons.DELETE_OUTLINE,
        on_click=lambda e: vymazat_historii(e),
        width=130,
        height=50,
        color=ft.Colors.RED_400,
        disabled=False
    )

    btn_zpet = ft.Button(
        "Zpět",
        icon=ft.Icons.ARROW_BACK,
        on_click=lambda e: zpet_callback(),
        width=130,
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
        kostka_icon.color = ft.Colors.BLUE_400
        kostka_hodnota_text.value = ""
        page.update()

        min_hodnota = 1
        max_hodnota = 6
        hody_serie = []

        while True:
            # Animace házení (5 rychlých změn)
            for _ in range(5):
                random_num = random.randint(1, 6)
                kostka_hodnota_text.value = str(random_num)
                kostka_icon.color = ft.Colors.BLUE_400
                page.update()
                await asyncio.sleep(0.1)

            # Finální hod
            kostka_hodnota = random.randint(min_hodnota, max_hodnota)
            kostka_hodnota_text.value = str(kostka_hodnota)

            # Barva ikony podle hodnoty
            if kostka_hodnota == 6:
                kostka_icon.color = ft.Colors.ORANGE
            else:
                kostka_icon.color = ft.Colors.GREEN

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
        pocet_hodu = len(hody_serie)

        # Barva podle výsledku
        if kostka_hodnota == 1:
            result_color = ft.Colors.GREEN_400
        elif kostka_hodnota <= 3:
            result_color = ft.Colors.LIGHT_BLUE_400
        else:
            result_color = ft.Colors.ORANGE_400

        historie_list.controls.insert(0,
            ft.Container(
                content=ft.Row([
                    ft.Icon(ft.Icons.CASINO, size=18, color=result_color),
                    ft.Text(
                        f"#{len(historie)}",
                        size=12,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.GREY_500,
                        width=35
                    ),
                    ft.Text(serie_text, size=13, weight=ft.FontWeight.W_500),
                    ft.Container(expand=True),
                    ft.Text(
                        f"{pocet_hodu} {'hod' if pocet_hodu == 1 else 'hody' if pocet_hodu < 5 else 'hodů'}",
                        size=11,
                        color=ft.Colors.GREY_600
                    ),
                ], spacing=8),
                padding=12,
                bgcolor=ft.Colors.with_opacity(0.4, ft.Colors.GREY_900) if len(historie) % 2 == 0 else ft.Colors.with_opacity(0.2, ft.Colors.GREY_900),
                border_radius=8,
                border=ft.border.all(1, ft.Colors.with_opacity(0.1, result_color))
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
        kostka_hodnota_text.value = ""
        kostka_icon.color = ft.Colors.WHITE
        page.update()

    # Vytvoření hlavního sloupce s plnou šířkou
    main_column = ft.Column([
        ft.Container(height=10),
        # Hlavička - vycentrovaná
        ft.Row([
            ft.Icon(ft.Icons.CASINO, size=32, color=ft.Colors.BLUE_400),
            ft.Text("Házení kostkou", size=26, weight=ft.FontWeight.BOLD),
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=10),

        ft.Container(height=5),
        # Popisek - vycentrovaný
        ft.Row([
            ft.Text(
                "Program hází dokud nepadne jiné číslo než 6",
                size=12,
                color=ft.Colors.GREY_600,
            ),
        ], alignment=ft.MainAxisAlignment.CENTER),

        ft.Container(height=15),

        # Zobrazení kostky - vycentrované
        ft.Row([
            ft.Container(
                content=ft.Column([
                    kostka_icon,
                    kostka_hodnota_text,
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                padding=15,
                border_radius=12,
                bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
            ),
        ], alignment=ft.MainAxisAlignment.CENTER),

        ft.Container(height=8),
        # Výsledek - vycentrovaný
        ft.Row([
            vysledek_text,
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Container(height=15),

        # Všechna 3 tlačítka vedle sebe
        ft.Row([
            btn_hazet,
            btn_vymazat,
            btn_zpet,
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=12),

        ft.Container(height=15),
        ft.Divider(height=1, color=ft.Colors.GREY_800),
        ft.Container(height=10),

        # Hlavička historie
        ft.Row([
            ft.Icon(ft.Icons.HISTORY, size=22, color=ft.Colors.BLUE_400),
            ft.Text("Historie sérií", size=16, weight=ft.FontWeight.BOLD),
            ft.Container(expand=True),
            pocet_hodu_text,
        ], spacing=8),

        ft.Container(height=8),

        # Historie v kontejneru se scrollováním
        historie_container,

        ft.Container(height=10),
    ], expand=True, spacing=0)

    page.add(main_column)

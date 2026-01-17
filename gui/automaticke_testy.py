#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GUI modul - Automatické testování her
"""

import flet as ft
import sys
import os

# Přidání parent directory do cesty pro import testů
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests.test_bulls_cows import spust_vsechny_testy as testy_bulls_cows
from tests.test_tic_tac_toe import spust_vsechny_testy as testy_tic_tac_toe


def zobraz_ukol(page: ft.Page, zpet_callback):
    """
    Zobrazí GUI pro výběr automatických testů.

    Args:
        page: Flet Page objekt
        zpet_callback: Funkce pro návrat zpět
    """

    def spust_testy_hry(hra_nazev):
        """Spustí testy pro vybranou hru a zobrazí výsledky."""
        page.controls.clear()

        # Zvětšení okna pro zobrazení výsledků
        page.window.height = 700
        page.update()

        # Nadpis
        page.add(
            ft.Container(height=10),
            ft.Text(f"Automatické testy - {hra_nazev}", size=24, weight=ft.FontWeight.BOLD),
            ft.Container(height=10)
        )

        # Indikátor načítání
        loading_text = ft.Text("Spouštím testy...", size=16, color=ft.Colors.BLUE_700)
        page.add(loading_text)
        page.update()

        # Spuštění testů
        try:
            if hra_nazev == "Bulls & Cows":
                vysledky = testy_bulls_cows()
            elif hra_nazev == "Tic-tac-toe":
                vysledky = testy_tic_tac_toe()
            else:
                page.add(ft.Text("Neznámá hra!", color=ft.Colors.RED))
                page.update()
                return

            # Vymazání loading textu
            page.controls.clear()

            # Zobrazení výsledků
            page.add(
                ft.Container(height=10),
                ft.Text(f"Automatické testy - {hra_nazev}", size=24, weight=ft.FontWeight.BOLD),
                ft.Container(height=10)
            )

            # Výpočet celkové úspěšnosti
            celkovy_uspech = 0
            celkovy_pocet = 0

            # ListView pro výsledky
            vysledky_list = ft.ListView(
                expand=True,
                spacing=10,
                padding=10,
                height=350
            )

            for kategorie, testy in vysledky.items():
                # Kategorie nadpis
                vysledky_list.controls.append(
                    ft.Container(
                        content=ft.Text(kategorie, size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_400),
                        padding=ft.padding.only(top=10, bottom=5)
                    )
                )

                # Testy v kategorii
                for nazev, uspech in testy:
                    celkovy_pocet += 1
                    if uspech:
                        celkovy_uspech += 1
                        ikona = "✓"
                        barva = ft.Colors.GREEN
                        bg_barva = ft.Colors.GREEN_50
                    else:
                        ikona = "✗"
                        barva = ft.Colors.RED
                        bg_barva = ft.Colors.RED_50

                    vysledky_list.controls.append(
                        ft.Container(
                            content=ft.Row([
                                ft.Text(ikona, size=16, weight=ft.FontWeight.BOLD, color=barva, width=30),
                                ft.Text(nazev, size=14, color=ft.Colors.WHITE if uspech else ft.Colors.RED_200),
                            ]),
                            bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.GREEN if uspech else ft.Colors.RED),
                            border=ft.border.all(1, ft.Colors.GREEN_700 if uspech else ft.Colors.RED_700),
                            border_radius=5,
                            padding=10
                        )
                    )

            # Přidání výsledků na stránku
            page.add(
                ft.Container(
                    content=vysledky_list,
                    border=ft.border.all(1, ft.Colors.GREY_700),
                    border_radius=5,
                    height=350
                )
            )

            # Souhrn
            uspesnost_procenta = int((celkovy_uspech / celkovy_pocet) * 100) if celkovy_pocet > 0 else 0

            if celkovy_uspech == celkovy_pocet:
                souhrn_barva = ft.Colors.GREEN
                souhrn_text = "✓ VŠECHNY TESTY PROŠLY!"
            else:
                souhrn_barva = ft.Colors.ORANGE
                souhrn_text = f"✗ {celkovy_pocet - celkovy_uspech} testů selhalo"

            page.add(
                ft.Container(height=10),
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            f"Výsledek: {celkovy_uspech}/{celkovy_pocet} testů prošlo ({uspesnost_procenta}%)",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            text_align=ft.TextAlign.CENTER,
                            color=ft.Colors.WHITE
                        ),
                        ft.Text(
                            souhrn_text,
                            size=18,
                            weight=ft.FontWeight.BOLD,
                            color=souhrn_barva,
                            text_align=ft.TextAlign.CENTER
                        )
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.BLUE),
                    border=ft.border.all(1, ft.Colors.BLUE_700),
                    border_radius=10,
                    padding=15
                ),
                ft.Container(height=10),
                ft.Row([
                    ft.Button("← Zpět na výběr testů", on_click=lambda e: zobraz_vyber_testu(), width=200),
                ], alignment=ft.MainAxisAlignment.CENTER)
            )

        except Exception as e:
            page.controls.clear()
            page.add(
                ft.Container(height=10),
                ft.Text("Chyba při spouštění testů", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.RED),
                ft.Container(height=10),
                ft.Text(f"Detaily: {str(e)}", size=14, color=ft.Colors.RED),
                ft.Container(height=20),
                ft.Button("← Zpět", on_click=lambda e: zobraz_vyber_testu(), width=150)
            )

        page.update()

    def zobraz_vyber_testu():
        """Zobrazí výběr testů."""
        page.controls.clear()

        # Reset velikosti okna
        page.window.height = 600
        page.update()

        page.add(
            ft.Container(height=10),
            ft.Text("Automatické testování her", size=24, weight=ft.FontWeight.BOLD),
            ft.Container(height=10),
            ft.Text("Vyber hru, kterou chceš otestovat:", size=16),
            ft.Container(height=20),
            ft.Column([
                ft.Container(
                    content=ft.TextButton(
                        content=ft.Row([
                            ft.Icon(ft.Icons.GAMES, size=40, color=ft.Colors.BLUE_400),
                            ft.Column([
                                ft.Text("Bulls & Cows", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                                ft.Text("Otestuje generování čísel, validaci a vyhodnocování", size=12, color=ft.Colors.GREY_400)
                            ], spacing=2)
                        ], spacing=15),
                        on_click=lambda e: spust_testy_hry("Bulls & Cows"),
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                        ),
                        width=500,
                        height=80,
                    ),
                    bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.BLUE),
                    border_radius=10,
                    border=ft.border.all(2, ft.Colors.BLUE_700),
                    padding=5
                ),
                ft.Container(height=10),
                ft.Container(
                    content=ft.TextButton(
                        content=ft.Row([
                            ft.Icon(ft.Icons.GRID_3X3, size=40, color=ft.Colors.GREEN_400),
                            ft.Column([
                                ft.Text("Tic-tac-toe", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                                ft.Text("Otestuje vytvoření plochy, kontrolu vítězství a remíz", size=12, color=ft.Colors.GREY_400)
                            ], spacing=2)
                        ], spacing=15),
                        on_click=lambda e: spust_testy_hry("Tic-tac-toe"),
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                        ),
                        width=500,
                        height=80,
                    ),
                    bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.GREEN),
                    border_radius=10,
                    border=ft.border.all(2, ft.Colors.GREEN_700),
                    padding=5
                ),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            ft.Container(height=20),
            ft.Button("← Zpět do hlavního menu", on_click=lambda e: zpet_callback(), width=250)
        )
        page.update()

    # Zobrazení výběru testů
    zobraz_vyber_testu()

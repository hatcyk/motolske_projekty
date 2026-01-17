#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Domácí úkoly z Pythonu - Hlavní menu (GUI launcher)
# Autor: Štefan Barát
# Škola: Střední průmyslová škola dopravní

import sys
import os
import subprocess
import flet as ft
import tracemalloc

# Spuštění tracemalloc pro sledování alokace paměti
tracemalloc.start()

# Potlač deprecated warnings z Flet (musí být před importem flet funkcí)
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Import GUI modulů
from gui import trojuhelnik
from gui import pismeno_dne
from gui import sety
from gui import data
from gui import kalkulacka
from gui import bulls_cows
from gui import tic_tac_toe
from gui import automaticke_testy


def main():
    # Spuštění programu - zobrazí GUI volbu.
    
    # Vytvoření Flet aplikace
    def gui_app(page: ft.Page):
        page.title = "Domácí úkoly z Pythonu"
        page.window.width = 700
        page.window.height = 350
        page.window.resizable = True
        page.padding = 20
        
        # Proměnná pro uložení PID terminálu
        terminal_process = None
        
        def window_event_handler(e):
            # Zachytí event zavření okna a ukončí terminál.
            if e.data == "close":
                # Ukončí CLI terminál pokud běží
                if terminal_process is not None:
                    try:
                        terminal_process.terminate()
                    except:
                        pass
                # Ukončí aplikaci
                os._exit(0)
        
        # Nastavení event handleru pro zavření okna
        page.window.on_event = window_event_handler
        
        def spustit_cli(e):
            # Otevře CLI rozhraní v novém terminálu.
            nonlocal terminal_process
            
            # Pokud je terminál už otevřený, jen zobrazí zprávu
            if terminal_process is not None:
                page.controls.clear()
                page.add(
                    ft.Container(height=10),
                    ft.Text("CLI terminál je již otevřen", size=24, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                    ft.Container(height=10),
                    ft.Text("✓ Terminál běží na pozadí", size=16, text_align=ft.TextAlign.CENTER, color=ft.Colors.GREEN),
                    ft.Container(height=10),
                    ft.Text("Můžeš pokračovat v GUI nebo zavřít okno", size=14, text_align=ft.TextAlign.CENTER),
                    ft.Container(height=20),
                    ft.Button("← Zpět do menu", on_click=lambda e: obnovit_menu(), width=200, height=50)
                )
                page.update()
                return
            
            # Cesta ke CLI skriptu
            cli_script = os.path.join(os.path.dirname(__file__), 'cli_menu.py')
            project_dir = os.path.dirname(os.path.abspath(__file__))
            
            # Spustí nový terminál s CLI podle OS a uloží proces
            if sys.platform == "darwin":  # macOS
                # Spustí Python přímo v novém okně Terminálu (bez prázdného okna)
                terminal_process = subprocess.Popen([
                    'osascript', '-e',
                    f'tell application "Terminal" to do script "cd \\"{project_dir}\\" && python3 \\"{cli_script}\\" && exit"'
                ])
            elif sys.platform == "win32":  # Windows
                terminal_process = subprocess.Popen(['start', 'cmd', '/k', 'python', cli_script], shell=True)
            else:  # Linux
                terminal_process = subprocess.Popen(['x-terminal-emulator', '-e', 'python3', cli_script])
            
            # Zobrazí zprávu že terminál byl otevřen
            page.controls.clear()
            page.add(
                ft.Container(height=10),
                ft.Text("✓ CLI terminál otevřen", size=24, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER, color=ft.Colors.GREEN),
                ft.Container(height=10),
                ft.Text("Terminál běží na pozadí", size=16, text_align=ft.TextAlign.CENTER),
                ft.Container(height=10),
                ft.Text("Můžeš zavřít toto okno nebo pokračovat v GUI", size=14, text_align=ft.TextAlign.CENTER),
                ft.Container(height=20),
                ft.Button("← Zpět do menu", on_click=lambda e: obnovit_menu(), width=200, height=50)
            )
            page.update()
        
        def obnovit_menu():
            # Obnoví hlavní menu.
            page.window.width = 700
            page.window.height = 350
            page.controls.clear()
            page.add(
                ft.Container(height=10),
                nadpis,
                autor,
                ft.Container(height=20),
                ft.Row(
                    [btn_cli, btn_gui],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10
                ),
                ft.Container(height=10),
                ft.Row(
                    [btn_testy, btn_konec],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10
                )
            )
            page.update()
        
        def spustit_testy(e):
            # Spustí automatické testování.
            page.controls.clear()

            # Zvětšení okna pro testy
            page.window.width = 700
            page.window.height = 600
            page.update()

            # Zobrazení testovacího rozhraní
            automaticke_testy.zobraz_ukol(page, obnovit_menu)

        def spustit_gui(e):
            # Spustí GUI rozhraní.
            page.controls.clear()
            
            # Zvětšení okna pro GUI menu
            page.window.width = 700
            page.window.height = 600
            page.update()
            
            def zpet_do_menu(e):
                # Vrátí se zpět do hlavního menu.
                # Vrácení původní velikosti okna
                page.window.width = 700
                page.window.height = 350
                page.controls.clear()
                page.add(
                    ft.Container(height=10),
                    nadpis,
                    autor,
                    ft.Container(height=20),
                    ft.Row(
                        [btn_cli, btn_gui],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10
                    ),
                    ft.Container(height=10),
                    ft.Row(
                        [btn_testy, btn_konec],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10
                    )
                )
                page.update()
            
            def spustit_ukol_gui(ukol_cislo):
                # Spustí konkrétní úkol v GUI.
                page.controls.clear()
                
                if ukol_cislo == 1:
                    trojuhelnik.zobraz_ukol(page, zpet_do_gui_menu)
                elif ukol_cislo == 2:
                    pismeno_dne.zobraz_ukol(page, zpet_do_gui_menu)
                elif ukol_cislo == 3:
                    sety.zobraz_ukol(page, zpet_do_gui_menu)
                elif ukol_cislo == 4:
                    data.zobraz_ukol(page, zpet_do_gui_menu)
                elif ukol_cislo == 5:
                    kalkulacka.zobraz_ukol(page, zpet_do_gui_menu)
                elif ukol_cislo == 6:
                    bulls_cows.zobraz_ukol(page, zpet_do_gui_menu)
                elif ukol_cislo == 7:
                    tic_tac_toe.zobraz_ukol(page, zpet_do_gui_menu)
                
                page.update()
            
            def zpet_do_gui_menu():
                # Vrátí se do GUI menu úkolů.
                page.controls.clear()
                page.add(
                    ft.Container(height=10),
                    ft.Text("GUI - Seznam úkolů", size=24, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                    ft.Container(height=10),
                    ft.Column([
                        ft.Button("1. Výpočet plochy trojúhelníku", on_click=lambda e: spustit_ukol_gui(1), width=400),
                        ft.Button("2. Hádání prvního písmene dne", on_click=lambda e: spustit_ukol_gui(2), width=400),
                        ft.Button("3. Práce se sety", on_click=lambda e: spustit_ukol_gui(3), width=400),
                        ft.Button("4. Práce s daty", on_click=lambda e: spustit_ukol_gui(4), width=400),
                        ft.Button("5. Kalkulačka", on_click=lambda e: spustit_ukol_gui(5), width=400),
                        ft.Button("6. Bulls & Cows", on_click=lambda e: spustit_ukol_gui(6), width=400),
                        ft.Button("7. Tic-tac-toe", on_click=lambda e: spustit_ukol_gui(7), width=400),
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                    ft.Container(height=10),
                    ft.Button("← Zpět do hlavního menu", on_click=zpet_do_menu, width=250)
                )
                page.update()
            
            # Zobraz GUI menu
            zpet_do_gui_menu()
        
        async def ukoncit(e):
            # Ukončí aplikaci - zavře okno.
            # Zobrazení loading obrazovky
            page.controls.clear()
            page.add(
                ft.Container(height=100),
                ft.Column([
                    ft.ProgressRing(),
                    ft.Container(height=20),
                    ft.Text("Ukončuji aplikaci...", size=20, weight=ft.FontWeight.BOLD),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            )
            page.update()

            # Krátké čekání pro zobrazení zprávy
            import asyncio
            await asyncio.sleep(0.5)

            # Zavření aplikace
            await page.window.destroy()

        # Nadpis
        nadpis = ft.Text(
            "Domácí úkoly z Pythonu",
            size=24,
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER
        )
        
        # Podnadpis
        autor = ft.Text(
            "Autor: Štefan Barát",
            size=14,
            text_align=ft.TextAlign.CENTER,
            color=ft.Colors.GREY_700
        )
        
        # Tlačítka
        btn_cli = ft.Button(
            "Rozhraní CLI",
            on_click=spustit_cli,
            width=180,
            height=60,
            icon=ft.Icons.TERMINAL,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8))
        )

        btn_gui = ft.Button(
            "Rozhraní GUI",
            on_click=spustit_gui,
            width=180,
            height=60,
            icon=ft.Icons.WINDOW,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8))
        )

        btn_testy = ft.Button(
            "Automatické testování",
            on_click=spustit_testy,
            width=180,
            height=60,
            icon=ft.Icons.KEY,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8))
        )

        btn_konec = ft.Button(
            "Konec",
            on_click=ukoncit,
            width=180,
            height=60,
            icon=ft.Icons.EXIT_TO_APP,
            color=ft.Colors.RED_400,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8))
        )
        
        # Přidání všech prvků na stránku
        page.add(
            ft.Container(height=10),
            nadpis,
            autor,
            ft.Container(height=20),
            ft.Row(
                [btn_cli, btn_gui],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10
            ),
            ft.Container(height=10),
            ft.Row(
                [btn_testy, btn_konec],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10
            )
        )
    
    # Spuštění Flet aplikace
    ft.app(gui_app)


if __name__ == "__main__":
    main()

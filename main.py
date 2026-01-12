#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Domácí úkoly z Pythonu - Hlavní menu (GUI launcher)
Autor: Štefan Barát
Škola: Střední průmyslová škola dopravní
"""

import sys
import os
import subprocess
import flet as ft


def main():
    """Spuštění programu - zobrazí GUI volbu."""
    # Vytvoření Flet aplikace
    def gui_app(page: ft.Page):
        page.title = "Domácí úkoly z Pythonu"
        page.window.width = 400
        page.window.height = 300
        page.window.resizable = False
        page.padding = 20
        
        def spustit_cli(e):
            """Zavře GUI a spustí CLI rozhraní v novém terminálu."""
            # Cesta ke CLI skriptu
            cli_script = os.path.join(os.path.dirname(__file__), 'cli_menu.py')
            project_dir = os.path.dirname(os.path.abspath(__file__))
            
            # Spustí nový terminál s CLI podle OS
            if sys.platform == "darwin":  # macOS
                # AppleScript pro spuštění nového okna Terminálu
                subprocess.Popen([
                    'osascript', '-e',
                    f'tell app "Terminal" to do script "cd \\"{project_dir}\\" && python3 \\"{cli_script}\\""'
                ])
            elif sys.platform == "win32":  # Windows
                subprocess.Popen(['start', 'cmd', '/k', 'python', cli_script], shell=True)
            else:  # Linux
                subprocess.Popen(['x-terminal-emulator', '-e', 'python3', cli_script])
            
            # Zavře GUI okno
            page.window.close()
        
        def spustit_gui(e):
            """Spustí GUI rozhraní (zatím prázdné)."""
            page.controls.clear()
            page.add(
                ft.Text("GUI rozhraní", size=30, weight=ft.FontWeight.BOLD),
                ft.Text("Funkce bude doplněna...", size=16),
                ft.Button("Zpět", on_click=lambda e: page.window.close())
            )
            page.update()
        
        def ukoncit(e):
            """Ukončí aplikaci."""
            page.window.close()
        
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
            width=200,
            height=50,
            icon=ft.Icons.TERMINAL,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8))
        )
        
        btn_gui = ft.Button(
            "Rozhraní GUI",
            on_click=spustit_gui,
            width=200,
            height=50,
            icon=ft.Icons.WINDOW,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8))
        )
        
        btn_konec = ft.Button(
            "Konec",
            on_click=ukoncit,
            width=200,
            height=50,
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
            ft.Column(
                [btn_cli, btn_gui, btn_konec],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            )
        )
    
    # Spuštění Flet aplikace
    ft.run(target=gui_app)


if __name__ == "__main__":
    main()

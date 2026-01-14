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

# Potlač deprecated warnings z Flet (musí být před importem flet funkcí)
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


def main():
    """Spuštění programu - zobrazí GUI volbu."""
    # Vytvoření Flet aplikace
    def gui_app(page: ft.Page):
        page.title = "Domácí úkoly z Pythonu"
        page.window.width = 650
        page.window.height = 250
        page.window.resizable = False
        page.padding = 20
        
        # Proměnná pro uložení PID terminálu
        terminal_process = None
        
        def window_event_handler(e):
            """Zachytí event zavření okna a ukončí terminál."""
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
            """Otevře CLI rozhraní v novém terminálu."""
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
            """Obnoví hlavní menu."""
            page.controls.clear()
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
            page.update()
        
        def spustit_gui(e):
            """Spustí GUI rozhraní (zatím prázdné)."""
            page.controls.clear()
            
            def zpet_do_menu(e):
                """Vrátí se zpět do hlavního menu."""
                page.controls.clear()
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
                page.update()
            
            page.add(
                ft.Container(height=10),
                ft.Text("GUI rozhraní", size=30, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                ft.Container(height=10),
                ft.Text("Funkce bude doplněna...", size=16, text_align=ft.TextAlign.CENTER),
                ft.Container(height=20),
                ft.Button("← Zpět", on_click=zpet_do_menu, width=200, height=50)
            )
            page.update()
        
        def ukoncit(e):
            """Ukončí aplikaci - zavře okno."""
            # Uživatel zavře okno ručně kliknutím na X
            # Flet nemá synchronní způsob jak zavřít okno z event handleru
            page.controls.clear()
            page.add(
                ft.Container(height=50),
                ft.Text("Zavírání aplikace...", size=20, text_align=ft.TextAlign.CENTER),
                ft.Container(height=10),
                ft.Text("Prosím zavři toto okno kliknutím na ×", size=14, text_align=ft.TextAlign.CENTER, color=ft.Colors.GREY),
            )
            page.update()
            # Automatické zavření po 1 sekundě pomocí threadu
            import threading
            import time
            def auto_close():
                time.sleep(1)
                import os
                os._exit(0)
            threading.Thread(target=auto_close, daemon=True).start()
        
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
                [btn_cli, btn_gui, btn_konec],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10
            )
        )
    
    # Spuštění Flet aplikace
    ft.app(gui_app)


if __name__ == "__main__":
    main()

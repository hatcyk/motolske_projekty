#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GUI modul - Úkol 5: Kalkulačka
"""

import flet as ft


def zobraz_ukol(page: ft.Page, zpet_callback):
    """
    Zobrazí GUI pro kalkulačku.
    
    Args:
        page: Flet Page objekt
        zpet_callback: Funkce pro návrat zpět
    """
    cislo1 = ft.TextField(
        label="Číslo 1", 
        width=200, 
        keyboard_type=ft.KeyboardType.NUMBER
    )
    cislo2 = ft.TextField(
        label="Číslo 2", 
        width=200, 
        keyboard_type=ft.KeyboardType.NUMBER
    )
    operace = ft.Dropdown(
        label="Operace",
        width=200,
        options=[
            ft.dropdown.Option("+", "Sčítání"),
            ft.dropdown.Option("-", "Odčítání"),
            ft.dropdown.Option("*", "Násobení"),
            ft.dropdown.Option("/", "Dělení"),
        ]
    )
    vysledek = ft.Text("", size=20, weight=ft.FontWeight.BOLD)
    
    def vypocitej(e):
        """Provede výpočet podle zvolené operace."""
        try:
            a = float(cislo1.value)
            b = float(cislo2.value)
            op = operace.value
            
            if op == "+":
                result = a + b
            elif op == "-":
                result = a - b
            elif op == "*":
                result = a * b
            elif op == "/":
                if b == 0:
                    vysledek.value = "❌ Nelze dělit nulou!"
                    vysledek.color = ft.Colors.RED
                    page.update()
                    return
                result = a / b
            else:
                vysledek.value = "❌ Vyber operaci!"
                vysledek.color = ft.Colors.RED
                page.update()
                return
            
            vysledek.value = f"= {result}"
            vysledek.color = ft.Colors.GREEN
        except:
            vysledek.value = "❌ Zadej platná čísla!"
            vysledek.color = ft.Colors.RED
        page.update()
    
    page.add(
        ft.Container(height=10),
        ft.Text("Kalkulačka", size=24, weight=ft.FontWeight.BOLD),
        ft.Container(height=10),
        cislo1, 
        cislo2, 
        operace,
        ft.Container(height=10),
        ft.Button("Vypočítat", on_click=vypocitej, width=200),
        vysledek,
        ft.Container(height=20),
        ft.Button("← Zpět", on_click=lambda e: zpet_callback(), width=200)
    )

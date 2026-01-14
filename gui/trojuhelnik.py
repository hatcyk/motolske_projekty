#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GUI modul - Úkol 1: Výpočet plochy trojúhelníku
"""

import flet as ft


def zobraz_ukol(page: ft.Page, zpet_callback):
    """
    Zobrazí GUI pro výpočet plochy trojúhelníku.
    
    Args:
        page: Flet Page objekt
        zpet_callback: Funkce pro návrat zpět
    """
    strana_a = ft.TextField(
        label="Strana a", 
        width=200, 
        keyboard_type=ft.KeyboardType.NUMBER
    )
    strana_b = ft.TextField(
        label="Strana b", 
        width=200, 
        keyboard_type=ft.KeyboardType.NUMBER
    )
    strana_c = ft.TextField(
        label="Strana c", 
        width=200, 
        keyboard_type=ft.KeyboardType.NUMBER
    )
    vysledek = ft.Text("", size=16, color=ft.Colors.GREEN)
    
    def vypocitej(e):
        """Výpočet plochy trojúhelníku."""
        try:
            a = float(strana_a.value)
            b = float(strana_b.value)
            c = float(strana_c.value)
            
            if a <= 0 or b <= 0 or c <= 0:
                vysledek.value = "❌ Strany musí být kladné čísla!"
                vysledek.color = ft.Colors.RED
            elif a + b <= c or a + c <= b or b + c <= a:
                vysledek.value = "❌ Trojúhelník s těmito stranami neexistuje!"
                vysledek.color = ft.Colors.RED
            else:
                s = (a + b + c) / 2
                plocha = (s * (s - a) * (s - b) * (s - c)) ** 0.5
                vysledek.value = f"✓ Plocha trojúhelníku: {plocha:.2f}"
                vysledek.color = ft.Colors.GREEN
        except:
            vysledek.value = "❌ Zadej platná čísla!"
            vysledek.color = ft.Colors.RED
        page.update()
    
    page.add(
        ft.Container(height=10),
        ft.Text("Výpočet plochy trojúhelníku", size=24, weight=ft.FontWeight.BOLD),
        ft.Container(height=10),
        strana_a, 
        strana_b, 
        strana_c,
        ft.Container(height=10),
        ft.Button("Vypočítat", on_click=vypocitej, width=200),
        ft.Container(height=10),
        vysledek,
        ft.Container(height=20),
        ft.Button("← Zpět", on_click=lambda e: zpet_callback(), width=200)
    )

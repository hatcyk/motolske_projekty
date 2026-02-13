#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Úkol: Ověření operačního systému Windows
Autor: Štefan Barát
"""

import sys


def je_os_windows():
    """Ověří, zda operační systém je Windows."""
    return sys.platform == "win32"


def main():
    """Hlavní funkce programu."""
    vysledek = je_os_windows()
    print(vysledek)


if __name__ == "__main__":
    main()

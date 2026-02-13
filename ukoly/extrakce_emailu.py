#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Úkol: Extrakce emailových adres z textu
Autor: Štefan Barát
"""

import re


def uloz_emailove_adresy(text):
    """Vytáhne všechny emailové adresy z daného textu."""
    vzor = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(vzor, text)


def main():
    """Hlavní funkce programu."""
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

    vysledek = uloz_emailove_adresy(text)

    print(vysledek)


if __name__ == "__main__":
    main()

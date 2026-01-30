# Projektové úkoly - Python

## Volitelné projekty

### Co ti vyhovuje víc

Máš na výběr ze dvou projektů. Vyber si ten, který se ti líbí nejvíc:

| Projekt | Popis |
|---------|-------|
| **Bull & Cows** | Hra postavená na hádání 4ciferného čísla |
| **Tic-tac-toe** | Hra na poli 3x3, kde dva hráči střídavě umisťují X a O |

Podrobné zadání obou úloh najdeš níže. Můžeš vyzkoušet oba projekty!

---

## Projekt: Bulls & Cows

Vytvoř program, který simuluje hru **Bulls and Cows**.

### Požadavky:

1. **Hlavička souboru:**
    ```python
    """
    projekt_2.py: druhý projekt do Engeto Online Python Akademie
    author: Petr Svetr
    email: petr.svetr@gmail.com
    discord: Petr Svetr#4490
    """
    ```

2. Program pozdraví uživatele a vypíše úvodní text
3. Vytvoří tajné 4místné číslo (unikátní cifry, nesmí začínat 0)
4. Ověří vstup uživatele (délka, duplikáty, nula na začátku, číselné znaky)
5. Vyhodnotí tip a vypíše počet bulls/cows (včetně správného jednotného/množného čísla)

### Úvodní text:
```
Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------
```

### Příklad hry (číslo 2017):
```
>>> 1234
0 bulls, 2 cows
>>> 6147
1 bull, 1 cow
>>> 2417
3 bulls, 0 cows
>>> 2017
Correct, you've guessed the right number in 4 guesses!
-----------------------------------------------
That's amazing!
```

### Rozšíření (nepovinné):
- Měření času hry
- Statistika počtu odhadů

---

## Projekt: Tic-tac-toe

Vytvoř hru pro dva hráče, kde cílem je umístit 3 svojí kameny v řadě (horizontálně, vertikálně nebo diagonálně).

### Požadavky:

1. Hlavička souboru se jménem autora
2. Pozdrav a vypsání pravidel
3. Zobrazení hrací plochy
4. Dotaz na pozici pro hracího kamene
5. Ověření vstupu (validní čísla, číselný formát)
6. Kontrola obsazenosti pole
7. Aktualizace hrací plochy
8. Vyhodnocení výhry (tři kameny v řadě)
9. Detekce remízy

### Úvodní text:
```
Welcome to Tic Tac Toe
=========================================
GAME RULES:
Each player can place one mark (or stone) per turn on the 3x3 grid.
The WINNER is who succeeds in placing three of their marks in a:
* horizontal row
* vertical row or
* diagonal row
=========================================
Let's start the game
```

### Příklad hry:
```
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
Player o | Please enter your move number: 5
+---+---+---+
|   |   |   |
+---+---+---+
|   | O |   |
+---+---+---+
|   |   |   |
+---+---+---+
Player x | Please enter your move number: 1
+---+---+---+
| X |   |   |
+---+---+---+
|   | O |   |
+---+---+---+
|   |   |   |
+---+---+---+
Congratulations, player o WON!
```

---

## Další úkoly

### 1. Plocha trojúhelníku
- Vypočítej plochu trojúhelníku podle zadané výšky a základny

### 2. Kalendář
- Vytvořte program zobrazující kalendář

### 3. Prohození proměnných
- Prohoď hodnoty dvou proměnných s dočasnou proměnnou
- Prohoď hodnoty dvou proměnných bez dočasné proměnné

### 4. Kontrola sudosti/lichosti
- Vyhodnoť, zda je číslo sudé nebo liché

### 5. Házení kostkou (Simulace hodu kostkou)

Pro tuto úlohu budeš potřebovat nahrát knihovnu `random`. Tvým úkolem bude simulovat hod kostkou.

Program musí obsahovat:

1. Naimportuj knihovnu `random`
2. vytvoř proměnnou `min_hodnota` a ulož do ní `int 1`
3. vytvoř proměnnou `max_hodnota` a ulož do ní `int 6`
4. vytvoř řízenou nekonečnou smyčku
5. nejprve vypíš: `"Házím kostkou.."`
6. vytvoř proměnnou `kostka_hodnota`, které bude náhodně přiřazeno `int` od `min_hodnota` do `max_hodnota`
7. následně doplň oznámení: `"Na kostce je: <hodnota>"`
8. pokud `kostka_hodnota` bude obsahovat hodnotu 6, hod se provede znovu
9. pokud padne jiné číslo, než 6 program se ukončí

**Ukázka možných běhů programu:**

```
Házím kostkou..
Na kostce je: 2
```

```
Házím kostkou..
Na kostce je: 6
Házím kostkou..
Na kostce je: 5
```

---

## Úkoly se slovníky a kolekcemi

### 1. Počítání výskytů
Vytvoř program, který spočítá výskyt každého prvku v sekvenci.

**Sekvence:** `[1, 21, 5, 3, 5, 8, 321, 1, 2, 2, 32, 6, 9, 1, 4, 6, 3, 1, 2]`

**Výstup:**
```
key: 1 value: 4
key: 2 value: 3
key: 3 value: 2
key: 4 value: 1
key: 5 value: 2
key: 6 value: 2
key: 8 value: 1
key: 9 value: 1
key: 21 value: 1
key: 32 value: 1
key: 321 value: 1
```

### 2. Ověření uživatele
Vytvoř program na ověření hesla uživatele.

**Příklad:**
```python
jmeno = 'Marek'
heslo = '1234'
uzivatel = {'Marek': '1234'}
```

**Výstup:**
- Správné údaje: `Ahoj Marek vítej v aplikaci! Pokračuj...`
- Chybné údaje: `Uživatelské jméno nebo heslo nejsou v pořádku!`

### 3. Aritmetický operátor
Vytvoř kalkulator s operacemi sčítání a odčítání.

**Postup:**
1. Uživatel zvolí operátor (`"+"` nebo `"-"`)
2. Zadá dvě čísla
3. Program zobrazí výsledek
4. Zeptá se, zda pokračovat

**Příklad:**
```
Sčítání:   "+"
Odčítání:  "-"
------------------
Vyber si operaci: +
Zadej první číslo: 1
Zadej druhé číslo: 1
1 + 1 = 2
Chcete provést další operaci? ('a' pro ano, jinak ne):
```

### 4. Slova o délce 4 znaky
Sbírej slova dlouhá přesně 4 znaky, dokud nezískáš 3 unikátní slova.

**Validace:**
- Delka musí být přesně 4 znaky
- Slovo už uložené: `"Slovo <slovo> už je uložené"`
- Špatná délka: `"Slovo není dlouhé čtyři znaky"`

### 5. Výběr ovoce
Uživatel si vybere ovoce z nabídky: `"jablko"`, `"banan"`, `"citron"`, `"pomeranc"`

**Příklad:**
```
Dostupné ovoce: citron, banan, pomeranc, jablko
VYBER Z DOSTUPNÉHO OVOCE: citron
Bezva, toto ovoce je v nabídce
```

### 6. Počítání samohlásek a souhlásek
Spočítej počet samohlásek (`"aeiouy"`) a souhlásek v textu.

**Příklad:**
```python
veta = 'Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu'
```

**Výstup:**
```
Počet souhlásek: 41 | Počet samohlásek: 21
```

### 7. Sjednocení setů
Vytvoř sjednocení dvou setů.

**Výstup:**
```
Sjednocené hodnoty ze zadání: {1, 2, 3, 4, 5, 6, 7, 8}
```

### 8. Rozdíl setů
Najdi prvky, které jsou v prvním setu, ale ne v druhém.

**Příklad:**
```python
numbers_1 = {1, 2, 3, 4}
numbers_2 = {3, 4, 5, 6}
```

**Výstup:**
```
Rozdílné hodnoty prvního setu oproti druhému: {1, 2}
```

### 9. Kontrola dne v týdnu
Ověř první písmeno zvoleného dne v týdnu.

**Příklad:**
```
Číslo dne: 3 (středa, první písmeno: s)
Tip: s
Správné písmeno!
```

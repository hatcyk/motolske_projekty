"""
bulls_and_cows.py: Implementace hry Bulls & Cows

author: Štefan Barát
email: barat70671@mot.sps-dopravni.cz
discord: hatsukooo
"""

import random
from utils.timer import start_timer, stop_timer, format_time
from utils.statistics import add_bulls_cows_result


def generate_secret_number():
    """
    Vygeneruje tajné 4-místné číslo s unikátními číslicemi.
    První číslice nesmí být 0.

    Returns:
        str: 4-místné číslo jako string
    """
    # První číslice: 1-9 (ne nula)
    first_digit = random.choice('123456789')

    # Zbývající číslice: 0-9 kromě první číslice
    remaining_digits = [d for d in '0123456789' if d != first_digit]
    other_digits = random.sample(remaining_digits, 3)

    # Spojit do jednoho čísla
    secret = first_digit + ''.join(other_digits)
    return secret


def display_welcome():
    """Zobrazí uvítací zprávu hry."""
    print("Ahoj!")
    print("-----------------------------------------------")
    print("Vygeneroval jsem pro tebe náhodné 4-místné číslo.")
    print("Pojďme si zahrát hru Bulls & Cows.")
    print("-----------------------------------------------")


def validate_input(guess):
    """
    Validuje vstup hráče.

    Args:
        guess (str): Hráčův tip

    Returns:
        tuple: (is_valid, error_message)
               is_valid je True pokud je vstup platný, False jinak
               error_message obsahuje chybovou zprávu nebo None
    """
    # Kontrola že je vstup text
    if not isinstance(guess, str):
        return False, "Vstup musí být text!"

    # Kontrola délky
    if len(guess) != 4:
        return False, "Číslo musí mít přesně 4 číslice!"

    # Kontrola že jsou všechny znaky číslice
    if not guess.isdigit():
        return False, "Vstup musí obsahovat pouze číslice!"

    # Kontrola že nezačíná nulou
    if guess[0] == '0':
        return False, "Číslo nesmí začínat nulou!"

    # Kontrola duplicit
    if len(set(guess)) != 4:
        return False, "Číslice musí být unikátní (žádné duplicity)!"

    return True, None


def calculate_bulls_cows(secret, guess):
    """
    Vypočítá počet bulls a cows.

    Bulls = správná číslice na správné pozici
    Cows = správná číslice na špatné pozici

    Args:
        secret (str): Tajné číslo
        guess (str): Hráčův tip

    Returns:
        tuple: (bulls, cows)
    """
    bulls = 0
    cows = 0

    # Počítání bulls - správná pozice
    for i in range(4):
        if secret[i] == guess[i]:
            bulls += 1

    # Počítání cows - špatná pozice
    for i in range(4):
        if guess[i] in secret and secret[i] != guess[i]:
            cows += 1

    return bulls, cows


def format_result(bulls, cows):
    """
    Formátuje výsledek sCorrectnou gramatikou (jednotné/množné číslo).

    Args:
        bulls (int): Počet bulls
        cows (int): Počet cows

    Returns:
        str: Formátovaný výsledek (např. "1 bull, 2 cows")
    """
    # Formátování bulls
    if bulls == 1:
        bulls_str = "1 bull"
    else:
        bulls_str = f"{bulls} bulls"

    # Formátování cows
    if cows == 1:
        cows_str = "1 cow"
    else:
        cows_str = f"{cows} cows"

    return f"{bulls_str}, {cows_str}"


def get_performance_message(guesses):
    """
    Vrátí hodnocení výkonu na základě počtu pokusů.

    Args:
        guesses (int): Počet pokusů

    Returns:
        str: Hodnocení výkonu
    """
    if guesses <= 3:
        return "úžasné"
    elif guesses <= 6:
        return "průměrné"
    elif guesses <= 10:
        return "mohlo být lepší"
    else:
        return "příště to půjde lépe"


def play_bulls_and_cows():
    """Hlavní funkce pro hraní Bulls & Cows."""
    # Spustit časovač
    start_time = start_timer()

    # Zobrazit uvítací zprávu
    display_welcome()

    # Vygenerovat tajné číslo
    secret = generate_secret_number()
    # DEBUG: print(f"DEBUG: Tajné číslo je {secret}")

    # Inicializovat počítadlo pokusů
    guesses = 0

    # Herní smyčka
    while True:
        # Získat vstup od hráče
        print("Zadej číslo:")
        print("-----------------------------------------------")
        guess = input(">>> ").strip()
        guesses += 1

        # Validovat vstup
        is_valid, error = validate_input(guess)
        if not is_valid:
            print(f"Chyba: {error}")
            print("-----------------------------------------------")
            guesses -= 1  # Neplatný pokus se nepočítá
            continue

        # Vypočítat bulls a cows
        bulls, cows = calculate_bulls_cows(secret, guess)

        # Zkontrolovat výhru
        if bulls == 4:
            # Zastavit časovač
            elapsed_time = stop_timer(start_time)
            print("Správně! Uhodl jsi správné číslo")
            print(f"na {guesses} pokusů!")
            print("-----------------------------------------------")
            # Zobrazit hodnocení výkonu
            performance = get_performance_message(guesses)
            print(f"To je {performance}!")
            # Zobrazit čas
            print(f"Čas: {format_time(elapsed_time)}")
            # Uložit statistiky
            add_bulls_cows_result(guesses, elapsed_time)
            break

        # Zobrazit výsledek
        print(format_result(bulls, cows))
        print("-----------------------------------------------")

"""
main.py: Hlavní vstupní bod pro projekt her

author: Štefan Barát
email: barat70671@mot.sps-dopravni.cz
discord: hatsukooo
"""


def display_menu():
    """Zobrazí hlavní menu."""
    print("\n" + "=" * 50)
    print("MENU - Výběr hry")
    print("=" * 50)
    print("1. Bulls & Cows")
    print("2. Tic-tac-toe")
    print("3. Konec")
    print("=" * 50)


def main():
    """Hlavní funkce programu."""
    while True:
        display_menu()
        choice = input("\nZadej svou volbu (1-3): ").strip()

        if choice == "1":
            from games.bulls_and_cows import play_bulls_and_cows
            play_bulls_and_cows()
        elif choice == "2":
            from games.tic_tac_toe import play_tic_tac_toe
            play_tic_tac_toe()
        elif choice == "3":
            print("\nDěkuji za hru! Nashledanou!")
            break
        else:
            print("\nNeplatná volba! Zadej číslo 1-3.")


if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("Vítej v herním programu!")
    print("=" * 50)
    main()

"""
tic_tac_toe.py: CLI implementace hry Tic-tac-toe

author: Štefan Barát
email: barat70671@mot.sps-dopravni.cz
discord: hatsukooo
"""

from games.tic_tac_toe_logic import (
    initialize_board,
    validate_move,
    check_winner,
    check_draw
)
from utils.timer import start_timer, stop_timer, format_time
from utils.statistics import add_tic_tac_toe_result


def display_welcome_and_rules():
    """Zobrazí uvítací zprávu a pravidla hry."""
    print("Vítej ve hře Piškvorky (Tic Tac Toe)")
    print("=" * 40)
    print("PRAVIDLA HRY:")
    print("Každý hráč může umístit jednu značku (kámen)")
    print("za tah na hrací pole 3x3. VÍTĚZ je ten,")
    print("kdo dokáže umístit tři své značky v řadě:")
    print("* horizontálně,")
    print("* vertikálně nebo")
    print("* diagonálně")
    print("=" * 40)
    print("Začínáme hru!")


def display_board(board):
    """
    Zobrazí hrací pole v pěkném formátu.

    Args:
        board (list): Hrací pole (9 prvků)
    """
    print("--------------------------------------------")
    print("+---+---+---+")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print("+---+---+---+")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("+---+---+---+")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print("+---+---+---+")


def play_tic_tac_toe():
    """Hlavní funkce pro hraní Tic-tac-toe."""
    # Spustit časovač
    start_time = start_timer()

    # Zobrazit uvítání a pravidla
    display_welcome_and_rules()

    # Inicializovat board
    board = initialize_board()

    # Začíná hráč O (podle zadání)
    current_player = 'O'

    # Herní smyčka
    while True:
        # Zobrazit board
        display_board(board)

        # Oddělovač
        print("=" * 40)

        # Vyzvat hráče k tahu
        move_input = input(f"Hráč {current_player} | Zadej číslo pole (1-9): ").strip()

        # Validovat tah
        is_valid, position, error = validate_move(move_input, board)
        if not is_valid:
            print(f"Chyba: {error}")
            continue

        # Umístit značku
        board[position] = current_player

        # Kontrola výhry
        winner = check_winner(board)
        if winner:
            elapsed_time = stop_timer(start_time)
            display_board(board)
            print("=" * 40)
            print(f"Gratulujeme! Hráč {winner} VYHRÁL!")
            print(f"Čas: {format_time(elapsed_time)}")
            print("=" * 40)
            # Uložit statistiky
            add_tic_tac_toe_result(winner, elapsed_time)
            break

        # Kontrola remízy
        if check_draw(board):
            elapsed_time = stop_timer(start_time)
            display_board(board)
            print("=" * 40)
            print("Remíza! Nikdo nevyhrál.")
            print(f"Čas: {format_time(elapsed_time)}")
            print("=" * 40)
            # Uložit statistiky
            add_tic_tac_toe_result('draw', elapsed_time)
            break

        # Přepnout hráče
        current_player = 'X' if current_player == 'O' else 'O'

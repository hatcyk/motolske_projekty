"""
tic_tac_toe.py: Implementace hry Tic-tac-toe

author: Štefan Barát
email: barat70671@mot.sps-dopravni.cz
discord: hatsukooo
"""

from utils.timer import start_timer, stop_timer, format_time


def display_welcome_and_rules():
    """Zobrazí uvítací zprávu a pravidla hry."""
    print("Welcome to Tic Tac Toe")
    print("=" * 40)
    print("GAME RULES:")
    print("Each player can place one mark (or stone)")
    print("per turn on the 3x3 grid. The WINNER is")
    print("who succeeds in placing three of their")
    print("marks in a:")
    print("* horizontal,")
    print("* vertical or")
    print("* diagonal row")
    print("=" * 40)
    print("Let's start the game")


def initialize_board():
    """
    Inicializuje prázdné hrací pole.

    Returns:
        list: List 9 mezer reprezentující hrací pole (indexy 0-8)
    """
    return [' '] * 9


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


def validate_move(move_input, board):
    """
    Validuje tah hráče.

    Args:
        move_input (str): Vstup od hráče
        board (list): Aktuální stav hrací plochy

    Returns:
        tuple: (is_valid, position, error_message)
               position je index 0-8 pokud je tah platný
    """
    # Kontrola že je vstup číselný
    if not move_input.isdigit():
        return False, None, "Vstup musí být číslo!"

    position = int(move_input)

    # Kontrola rozsahu 1-9
    if position < 1 or position > 9:
        return False, None, "Číslo musí být mezi 1 a 9!"

    # Konverze na index 0-8
    index = position - 1

    # Kontrola že pole je volné
    if board[index] != ' ':
        return False, None, "Toto pole je již obsazené!"

    return True, index, None


def check_horizontal_win(board):
    """
    Kontroluje horizontální výhru.

    Args:
        board (list): Hrací pole

    Returns:
        str or None: 'X', 'O', nebo None
    """
    # Kontrola řádků
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] and board[i] != ' ':
            return board[i]
    return None


def check_vertical_win(board):
    """
    Kontroluje vertikální výhru.

    Args:
        board (list): Hrací pole

    Returns:
        str or None: 'X', 'O', nebo None
    """
    # Kontrola sloupců
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] != ' ':
            return board[i]
    return None


def check_diagonal_win(board):
    """
    Kontroluje diagonální výhru.

    Args:
        board (list): Hrací pole

    Returns:
        str or None: 'X', 'O', nebo None
    """
    # Hlavní diagonála (0, 4, 8)
    if board[0] == board[4] == board[8] and board[0] != ' ':
        return board[0]

    # Vedlejší diagonála (2, 4, 6)
    if board[2] == board[4] == board[6] and board[2] != ' ':
        return board[2]

    return None


def check_winner(board):
    """
    Kontroluje jestli někdo vyhrál.

    Args:
        board (list): Hrací pole

    Returns:
        str or None: 'X', 'O', nebo None
    """
    # Zkontrolovat všechny možné způsoby výhry
    winner = check_horizontal_win(board)
    if winner:
        return winner

    winner = check_vertical_win(board)
    if winner:
        return winner

    winner = check_diagonal_win(board)
    if winner:
        return winner

    return None


def check_draw(board):
    """
    Kontroluje jestli je remíza.

    Args:
        board (list): Hrací pole

    Returns:
        bool: True pokud je remíza, False jinak
    """
    return ' ' not in board


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
        move_input = input(f"Player {current_player.lower()} | Please enter your move number: ").strip()

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
            print(f"Congratulations, the player {winner.lower()} WON!")
            print(f"Time: {format_time(elapsed_time)}")
            print("=" * 40)
            break

        # Kontrola remízy
        if check_draw(board):
            elapsed_time = stop_timer(start_time)
            display_board(board)
            print("=" * 40)
            print("It's a draw!")
            print(f"Time: {format_time(elapsed_time)}")
            print("=" * 40)
            break

        # Přepnout hráče
        current_player = 'X' if current_player == 'O' else 'O'

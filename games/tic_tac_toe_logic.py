"""
tic_tac_toe_logic.py: Sdílená herní logika pro Tic-Tac-Toe

author: Štefan Barát
email: barat70671@mot.sps-dopravni.cz
discord: hatsukooo
"""


def initialize_board():
    """
    Inicializuje prázdné hrací pole.

    Returns:
        list: List 9 mezer reprezentující hrací pole (indexy 0-8)
    """
    return [' '] * 9


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

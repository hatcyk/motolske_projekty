"""
tic_tac_toe_gui.py: GUI implementace hry Tic-Tac-Toe pomocí tkinter

author: Štefan Barát
email: barat70671@mot.sps-dopravni.cz
discord: hatsukooo
"""

import tkinter as tk
from tkinter import messagebox
import time
from games.tic_tac_toe_logic import (
    initialize_board,
    check_winner,
    check_draw
)
from utils.timer import start_timer, stop_timer, format_time
from utils.statistics import add_tic_tac_toe_result


class TicTacToeGUI:
    """GUI třída pro hru Tic-Tac-Toe."""

    def __init__(self, root):
        """
        Inicializace GUI.

        Args:
            root: Hlavní tkinter okno
        """
        self.root = root
        self.root.title("Piškvorky (Tic-Tac-Toe)")
        self.root.geometry("450x550")
        self.root.resizable(False, False)

        # Herní stav
        self.board = None
        self.current_player = None
        self.start_time = None
        self.game_ended = False
        self.buttons = []

        # Vytvoření widgetů
        self.create_widgets()

        # Start hry
        self.start_game()

    def create_widgets(self):
        """Vytvoří všechny GUI komponenty."""
        # Nadpis
        title_label = tk.Label(
            self.root,
            text="Piškvorky (Tic-Tac-Toe)",
            font=("Arial", 20, "bold"),
            pady=15
        )
        title_label.pack()

        # Frame pro informace
        info_frame = tk.Frame(self.root)
        info_frame.pack(pady=10)

        # Status hráče
        self.player_label = tk.Label(
            info_frame,
            text="Hráč na tahu: O",
            font=("Arial", 14, "bold"),
            fg="#2196F3"
        )
        self.player_label.grid(row=0, column=0, padx=20)

        # Časovač
        self.timer_label = tk.Label(
            info_frame,
            text="Čas: 0s",
            font=("Arial", 14)
        )
        self.timer_label.grid(row=0, column=1, padx=20)

        # Oddělovač
        separator = tk.Frame(self.root, height=2, bg="gray")
        separator.pack(fill="x", padx=20, pady=10)

        # Pravidla
        rules_label = tk.Label(
            self.root,
            text="Umísti 3 značky v řadě (horizontálně, vertikálně, diagonálně)",
            font=("Arial", 10),
            fg="gray"
        )
        rules_label.pack(pady=5)

        # Frame pro hrací pole
        board_frame = tk.Frame(self.root)
        board_frame.pack(pady=15)

        # Vytvoření 3x3 gridu tlačítek
        self.buttons = []
        for i in range(9):
            row = i // 3
            col = i % 3

            button = tk.Button(
                board_frame,
                text=" ",
                font=("Arial", 32, "bold"),
                width=5,
                height=2,
                command=lambda pos=i: self.make_move(pos),
                bg="#f0f0f0",
                relief="raised",
                bd=3
            )
            button.grid(row=row, column=col, padx=5, pady=5)
            self.buttons.append(button)

        # Tlačítko Nová hra
        new_game_button = tk.Button(
            self.root,
            text="Nová hra",
            font=("Arial", 12),
            command=self.start_game,
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=8
        )
        new_game_button.pack(pady=15)

    def start_game(self):
        """Začne novou hru."""
        self.board = initialize_board()
        self.current_player = 'O'  # O začíná (podle zadání)
        self.start_time = start_timer()
        self.game_ended = False

        # Aktualizace UI
        self.player_label.config(
            text="Hráč na tahu: O",
            fg="#2196F3"
        )
        self.timer_label.config(text="Čas: 0s")

        # Vymazat všechna tlačítka
        for i, button in enumerate(self.buttons):
            button.config(
                text=" ",
                state="normal",
                bg="#f0f0f0"
            )

        # Spustit aktualizaci časovače
        self.update_timer()

    def make_move(self, position):
        """
        Zpracuje tah hráče.

        Args:
            position (int): Index pole (0-8)
        """
        if self.game_ended or self.board[position] != ' ':
            return

        # Umístit značku
        self.board[position] = self.current_player

        # Aktualizovat tlačítko
        button = self.buttons[position]
        button.config(
            text=self.current_player,
            state="disabled",
            disabledforeground="black",
            bg="#e0e0e0"
        )

        # Zvýraznit X a O různými barvami
        if self.current_player == 'O':
            button.config(fg="#2196F3")  # Modrá pro O
        else:
            button.config(fg="#f44336")  # Červená pro X

        # Kontrola výhry
        winner = check_winner(self.board)
        if winner:
            self.handle_game_end(winner)
            return

        # Kontrola remízy
        if check_draw(self.board):
            self.handle_game_end('draw')
            return

        # Přepnout hráče
        self.current_player = 'X' if self.current_player == 'O' else 'O'

        # Aktualizovat label
        color = "#2196F3" if self.current_player == 'O' else "#f44336"
        self.player_label.config(
            text=f"Hráč na tahu: {self.current_player}",
            fg=color
        )

    def handle_game_end(self, result):
        """
        Zpracuje konec hry (výhra nebo remíza).

        Args:
            result (str): 'X', 'O', nebo 'draw'
        """
        self.game_ended = True

        # Zastavit časovač
        elapsed_time = stop_timer(self.start_time)

        # Uložit statistiky
        add_tic_tac_toe_result(result, elapsed_time)

        # Deaktivovat všechna tlačítka
        for button in self.buttons:
            button.config(state="disabled")

        # Zobrazit výsledkový dialog
        if result == 'draw':
            message = (
                f"Remíza! Nikdo nevyhrál.\n\n"
                f"Čas: {format_time(elapsed_time)}"
            )
            title = "Remíza!"
        else:
            message = (
                f"Gratulujeme! Hráč {result} VYHRÁL!\n\n"
                f"Čas: {format_time(elapsed_time)}"
            )
            title = f"Výhra hráče {result}!"

        response = messagebox.askquestion(
            title,
            message + "\n\nChceš hrát znovu?",
            icon='info'
        )

        if response == 'yes':
            self.start_game()
        else:
            self.root.destroy()

    def update_timer(self):
        """Aktualizuje časovač každou sekundu."""
        if not self.game_ended:
            elapsed = time.time() - self.start_time
            self.timer_label.config(text=f"Čas: {format_time(elapsed)}")
            self.root.after(1000, self.update_timer)


def play_tic_tac_toe_gui():
    """Spustí GUI verzi Tic-Tac-Toe."""
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()


if __name__ == "__main__":
    play_tic_tac_toe_gui()

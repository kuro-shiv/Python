import tkinter as tk
from tkinter import messagebox
import random2
import time

# Constants
MAX_LINES = 3
MAX_BET = 10000
MIN_BET = 10

ROWS = 3
COLS = 3

symbol_count = {
    "😁": 2,
    "😎": 4,
    "😚": 6,
    "😂": 8
}

symbol_value = {
    "😁": 5,
    "😎": 4,
    "😚": 3,
    "😂": 2
}

# Global Variables
balance = 0
lines = 0
bet = 0

# Functions
def initialize_game():
    global balance
    balance = int(balance_var.get())
    balance_label.config(text=f"Balance: Rs {balance}")
    balance_entry.config(state="disabled")
    enter_button.pack_forget()
    play_button.pack()
    quit_button.pack()

def play_game():
    play_button.pack_forget()
    quit_button.pack_forget()
    lines_label.pack()
    lines_entry.pack()
    bet_label.pack()
    bet_entry.pack()
    spin_button.pack()
    spin_result_label.config(text="")
    result_label.config(text="")

def spin():
    global lines, bet, balance
    lines = int(lines_var.get())
    bet = int(bet_var.get())
    total_bet = lines * bet

    if total_bet > balance:
        messagebox.showerror("Error", "Insufficient balance!")
        return

    result = get_spin_result()
    display_spin_result(result)

    winnings, winnings_lines = check_winnings(result, lines, bet, symbol_value)
    result_message = f"You won Rs {winnings}.\n"
    if winnings_lines:
        result_message += f"You won on lines: {', '.join(map(str, winnings_lines))}\n"
    else:
        result_message += "No winning lines.\n"

    balance += winnings - total_bet  # Update balance by adding winnings
    balance_label.config(text=f"Balance: Rs {balance}")

    result_message += f"New Balance: Rs {balance}"
    result_label.config(text=result_message)

    # Clear input sections
    lines_entry.delete(0, tk.END)
    bet_entry.delete(0, tk.END)

def display_spin_result(result):
    spin_result_label.config(text="\n".join(" | ".join(row) for row in result))

def get_spin_result():
    result = []
    for _ in range(COLS):
        symbols = [random2.choice(list(symbol_count.keys())) for _ in range(ROWS)]
        result.append(symbols)
    return result

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)

    return winnings, winnings_lines

def quit_game():
    root.destroy()

# Create GUI
root = tk.Tk()
root.title("Slot Machine")

balance_label = tk.Label(root, text="Enter Initial Balance:")
balance_label.pack()

balance_var = tk.StringVar(root)
balance_entry = tk.Entry(root, textvariable=balance_var)
balance_entry.pack()

enter_button = tk.Button(root, text="Enter", command=initialize_game)
enter_button.pack()

play_button = tk.Button(root, text="Play Game", command=play_game)
quit_button = tk.Button(root, text="Quit", command=quit_game)

lines_label = tk.Label(root, text="Number of Lines you wanna bet on:")
lines_var = tk.StringVar(root)
lines_entry = tk.Entry(root, textvariable=lines_var)

bet_label = tk.Label(root, text="Rs bet on per line:")
bet_var = tk.StringVar(root)
bet_entry = tk.Entry(root, textvariable=bet_var)

spin_button = tk.Button(root, text="Spin", command=spin)

spin_result_label = tk.Label(root, text="", font=("Helvetica", 16), justify="left")
spin_result_label.pack()

result_label = tk.Label(root, text="", font=("Helvetica", 12), justify="left")
result_label.pack()

reel_frame = tk.Frame(root)
reel_frame.pack()

root.mainloop()

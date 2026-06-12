import tkinter as tk
from tkinter import messagebox


window = tk.Tk()
window.title("Tic-Tac-Toe")

current_player = "X"

def click_button(btn):
    global current_player
    
    if btn["text"] == " ":
        btn["text"] = current_player  
        
        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} wins! 🎉")
            reset_board()
        elif check_tie():
            messagebox.showinfo("Game Over", "It's a tie! 🤝")
            reset_board()
        else:
            
            current_player = "O" if current_player == "X" else "X"


def check_winner():
    b = buttons  
  
    if b[0]["text"] == b[1]["text"] == b[2]["text"] != " ": return True
    if b[3]["text"] == b[4]["text"] == b[5]["text"] != " ": return True
    if b[6]["text"] == b[7]["text"] == b[8]["text"] != " ": return True
    # Check Columns
    if b[0]["text"] == b[3]["text"] == b[6]["text"] != " ": return True
    if b[1]["text"] == b[4]["text"] == b[7]["text"] != " ": return True
    if b[2]["text"] == b[5]["text"] == b[8]["text"] != " ": return True
    # Check Diagonals
    if b[0]["text"] == b[4]["text"] == b[8]["text"] != " ": return True
    if b[2]["text"] == b[4]["text"] == b[6]["text"] != " ": return True
    return False

def check_tie():
    return all(btn["text"] != " " for btn in buttons)

def reset_board():
    global current_player
    current_player = "X"
    for btn in buttons:
        btn["text"] = " "


buttons = []
for i in range(9):

    btn = tk.Button(window, text=" ", font=("Normal", 20, "bold"), width=5, height=2)
    
    btn.config(command=lambda b=btn: click_button(b))
    
    btn.grid(row=i // 3, column=i % 3)
    buttons.append(btn)


window.mainloop()

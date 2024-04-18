import tkinter as tk
from tkinter import messagebox
import morpionGame	
import minimax

# Création fenêtre Tkinter
root = tk.Tk()
root.geometry('350x350')
root.resizable(width=False, height=False)

# Action des 2 boutons
def PVP_start():
    exec(open("PVP\PvP_TicTacToe.py").read())

def AI_start():
    exec(open("minmax\gui.py").read())

# Couleur des boutons
colour1 = 'WHITE'
colour2 = '#05d7ff'
colour3 = '#65e7ff'
colour4 = 'BLACK'

# Configuration taille des boutons et padding
main_frame = tk.Frame(root, bg=colour1, pady=40)
main_frame.pack(fill=tk.BOTH, expand=True)
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)


# Caractéristiques et actions des boutons
button1 = tk.Button(
    main_frame,
    command=AI_start,
    background=colour1,
    foreground=colour2,
    activebackground=colour3,
    activeforeground=colour1,
    highlightthickness=2,
    highlightbackground=colour2,
    highlightcolor='WHITE',
    width=13,
    height=2,
    border=0,
    text='AI Game',
    font=('Arial', 16, 'bold')

)

button1.grid(column=0, row=0)



# Caractéristiques et actions des boutons
button2 = tk.Button(
    main_frame,
    command=PVP_start,
    background=colour1,
    foreground=colour2,
    activebackground=colour3,
    activeforeground=colour1,
    highlightthickness=2,
    highlightbackground=colour2,
    highlightcolor='WHITE',
    width=13,
    height=2,
    border=0,
    text='PVP Game',
    font=('Arial', 16, 'bold')

)

button2.grid(column=0, row=1)

root.mainloop()

# a class for the graphism
class MorpionGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Morpion")
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.player = None
        self.bot = None
        self.current_turn = None
        self.game=morpionGame.morpion()

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.window, text='', width=10, height=3, command=lambda i=i, j=j: self.on_button_click(i, j))
                self.buttons[i][j].grid(row=i, column=j)

        self.choose_symbol()
    # allow the player to choose the symbol that he wants
    def choose_symbol(self):
        choice_window = tk.Toplevel(self.window)
        choice_window.title("Choix du symbole")
        tk.Label(choice_window, text="Choisissez votre symbole:").grid(row=0, column=0, columnspan=2)
        tk.Button(choice_window, text="X", command=lambda: self.set_symbols('X')).grid(row=1, column=0)
        tk.Button(choice_window, text="O", command=lambda: self.set_symbols('O')).grid(row=1, column=1)

    # initializes the player and bot symbols and determines who goes first.
    def set_symbols(self, symbol):
        self.player = symbol
        self.bot = 'O' if symbol == 'X' else 'X'
        if self.bot=='X':
            self.bot_move()
            self.current_turn = 'O'
        else:
            self.current_turn = 'X'
        self.window.focus_set()

    # handles the button click event, updates the game board, and performs checks to determine if the game is over.
    def on_button_click(self, i, j):
        if not self.player:
            messagebox.showerror("Erreur", "Veuillez choisir un symbole avant de jouer.")
            self.choose_symbol()
            return

        if self.board[i][j] == '' and self.current_turn == self.player:
            self.board[i][j] = self.player
            self.buttons[i][j].config(text=self.player, state=tk.DISABLED)
            self.game=self.game.result((i,j), self.player)
            self.check_win()

            self.current_turn = self.bot
            
            self.bot_move()
    # allow the bot to play
    def bot_move(self):
        if not self.is_board_full():
            #move = minimax.minimax(self.game, self.bot)[1]
            move = minimax.alphabeta(self.game, self.bot)[1]
            
            print(move)# Utilisez votre fonction alphabeta ici
            i, j = move[0], move[1]
            self.board[i][j] = self.bot
            self.game=self.game.result(((i,j)), self.bot)
            self.buttons[i][j].config(text=self.bot, state=tk.DISABLED)
            self.check_win()

            self.current_turn = self.player
    # check if there is a winneror a draw
    def check_win(self):
        
        if self.game.terminalTest():
            util=self.game.utility()
            if util==1:
                messagebox.showinfo("Félicitations", "Le joueur X a gagné !")
                self.reset_board()
                self.game=morpionGame.morpion()
            if util==0:
                messagebox.showinfo("Égalité", "C'est une égalité !")
                self.reset_board()
                self.game=morpionGame.morpion()
            if util==-1:
                messagebox.showinfo("Félicitations", "Le joueur O a gagné !")
                self.reset_board()
                self.game=morpionGame.morpion()
        
    # reset the board for the next game
    def reset_board(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='', state=tk.NORMAL)

    # check if the board is full
    def is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == '':
                    return False
        return True
    
    def run(self):
        self.window.mainloop()
    
    
gui = MorpionGUI()
gui.run()
                
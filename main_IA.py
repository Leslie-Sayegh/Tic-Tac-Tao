# TicTacToe
# https://fr.wikipedia.org/wiki/Tic-tac-toe
 
# Import des bibliothèques
from tkinter import *
from tkinter.messagebox import *
import numpy as np
import random
 
 
# # # # # # # # # # # # # # # # # # # #
# Initialisation de la classe Joueur  #
# # # # # # # # # # # # # # # # # # # #
 
class Player():
    def __init__(self,name):
        """ Attribution du nom et du score """
        self.name = name
        self.score = 0
 
# # # # # # # # # # # # # # # # # #
# Initialisation de la classe UI  #
# # # # # # # # # # # # # # # # # #
 
class UI(Tk):
 
    def __init__(self):
        """ Initialisation """   
        # On ouvre une fenêtre
        Tk.__init__(self)
        self.title("Tic Tac Toe")
        self.game_mode = 0
        # On lance les fonctions graphiques
        self.menu()
        self.main_screen()
        self.center_window()
     
    # # # # # # # # # # # #
    # Fonctions générales #
    # # # # # # # # # # # #
 
    def menu(self):
        """ Création des menus """
        self.top_menu = Menu(self)
        self.config(menu=self.top_menu)
        # Ajout des boutons
        self.top_menu.add_command(label="Nouvelle Manche", command = self.new_game_dialog, state=DISABLED)
        self.top_menu.add_command(label="À propos",command = self.about)
        self.top_menu.add_command(label="Quitter",command = self.exit_dialog)
     
    def about(self):
        """ Popup A propos """
        showinfo("A propos", "TicTacToe Python 3 \nInterface Tkinter \n\nCodé par Thibault JOUSSE,\nMartinière Duchère 2015/2016.")
 
    def main_screen(self):
        """ Ecran d'accueil """
        # Zone de dessin temporaire
        Canvas(self, width=400, height=200, bg='ivory').pack(side=TOP, padx=5, pady=5)
 
        # Boutons de sélection de mode
        single_player_button = Button(self, text="1 joueur", command=self.single_player_mode)
        single_player_button.pack(side=LEFT, padx=5, pady=5)
        two_players_button = Button(self, text="2 joueurs", command=self.two_players_mode)
        two_players_button.pack(side=RIGHT, padx=5, pady=5)
     
    # # # # # # # # # # # #
    #   Centrage fenêtre  #
    # # # # # # # # # # # #
     
    def center_window(self):
        """ Centre la fenêtre """
        self.eval('tk::PlaceWindow %s center' % self.winfo_pathname(self.winfo_id()))
     
    def center_popup(self, popup):
        """ Centre la popup """
        w = popup.winfo_reqwidth()
        h = popup.winfo_reqheight()
        ws = popup.winfo_screenwidth()
        hs = popup.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        popup.geometry('+%d+%d' % (x, y))
     
    # # # # # # # # # # # #
    #    Mode 2 joueurs   #
    # # # # # # # # # # # #
 
    def two_players_mode(self):
        """ Initialise le mode 2 joueurs """
        self.game_mode = 2
        # Destruction des éléments non utilisés
        for i in range(1,4):
            self.winfo_children()[1].destroy()
        # Ajout des joueurs et dessin des zones
        self.add_players()
        self.draw_player_zone()
        self.draw_game_zone()
        self.center_window()
        # Sélection des noms, activation du menu + lancement partie
        self.get_name()
        self.top_menu.entryconfig(1,state=ACTIVE)
        self.launch_game()
         
    # # # # # # # # # # # #
    # Variables & joueurs #
    # # # # # # # # # # # #
     
    def default_variables(self):
        """ Réinitialisation des variables """
        self.active_player = 1
        self.game_table = np.array([[0]*3]*3)
     
    def add_players(self):
        """ Ajout des joueurs """
        if self.game_mode is 2:
            self.Player1 = Player1
            self.Player2 = Player2
             
        elif self.game_mode is 1:
            self.Player1 = Player1
            self.AI = AI
 
    # # # # # # # # # # # #
    #   Gestion des noms   #
    # # # # # # # # # # # #
     
    def get_name(self):
        """ Ouvre la saisie des noms de joueurs """
        # On ouvre une fenêtre de saisie successivement pour chaque joueur
        for self.i in range(1,3):
            self.name_selection_window = Toplevel()
            self.center_popup(self.name_selection_window)
            self.name_selection_window.resizable(0,0)
            self.name_selection_window.wait_visibility()
            self.name_selection_window.grab_set()
            self.name_selection_window.transient(self)
            self.name_selection_window.focus_force()
             
            player_name_label = Label(self.name_selection_window, text="Nom du Joueur %d : " % self.i)
 
            if self.game_mode is 1 and self.i is 2:
                player_name_label = Label(self.name_selection_window, text="Nom de l'IA")
 
            player_name_label.pack()   
             
            # On applique la fonction d'attribution du nom
            self.name_entry = Entry(self.name_selection_window, bd=3)
            self.name_entry.bind("<Return>",self.apply_name)
            self.name_entry.pack()
             
            # On attend que la fenêtre soit fermée pour continuer
            self.wait_window(self.name_selection_window)
             
    def apply_name(self, event):
        """ Récupère et attribue les noms saisis aux joueurs """
         # On récupère le texte dans la zone de saisie
        name = self.name_entry.get()
         
         # On attribue un nom si l'entrée n'est pas vide ou ne fait pas plus de 10 caractères
        if len(name) > 10:
                showwarning("Attention", "Le nom ne doit pas dépasser 10 caractères.")
        else:
            if name != "":
                if self.i == 1:
                    self.Player1.name = name
                    self.player1_zone.itemconfig(self.player1_label,text=name)
                elif self.i == 2:
                    if self.game_mode is 2:
                        self.Player2.name = name
                        self.player2_zone.itemconfig(self.player2_label,text=name)
                    elif self.game_mode is 1:
                        self.AI.name = name
                        self.player2_zone.itemconfig(self.player2_label,text=name)
            self.name_selection_window.destroy()
         
 
    # # # # # # # # # # # # #
    #  Fonctions graphiques  #
    # # # # # # # # # # # # #
 
    def draw_player_zone(self):
        """ Dessine les zones d'information sur les joueurs """
        # On dessine la zone du joueur 1 à gauche
        # On y affiche son nom, son score, son signe
        self.player1_zone = Canvas(self, width = 150, height = 305, bg="light green")
         
        self.player1_label = self.player1_zone.create_text(77,35,text = self.Player1.name,font="Helvetica 18 normal bold")
        self.player1_score = self.player1_zone.create_text(80,65,text = "Score : %d " %Player1.score, font="Helvetica 13 normal bold")
         
        self.player1_zone.create_line(55, 170, 95, 130, width=3, fill="red")
        self.player1_zone.create_line(55, 130, 95, 170, width=3, fill="red")
        self.player1_zone.pack(side=LEFT)
         
        # Même chose pour le joueur 2 mais à droite
        self.player2_zone = Canvas(self, width = 150, height = 305, bg="ivory")
         
        self.player2_zone.create_oval(55, 170, 95, 130, width=3, outline="green")
        self.player2_zone.pack(side=RIGHT)
 
        if self.game_mode is 2:
            self.player2_label = self.player2_zone.create_text(79,35,text = self.Player2.name, font="Helvetica 18 normal bold")
            self.player2_score = self.player2_zone.create_text(82,65,text = "Score : %d " %Player2.score, font="Helvetica 13 normal bold")
        elif self.game_mode is 1:
            self.player2_label = self.player2_zone.create_text(79,35,text = self.AI.name, font="Helvetica 18 normal bold")
            self.player2_score = self.player2_zone.create_text(82,65,text = "Score : %d " %AI.score, font="Helvetica 13 normal bold")
             
     
    def draw_game_zone(self):
        """ Dessine le plateau de jeu """
        self.game_zone = Canvas(self, width=300, height=300, bg="light blue")
        for i in range(0,3):
            self.game_zone.create_line(100*i, 0, 100*i, 310)
            self.game_zone.create_line(0, 100*i, 310, 100*i)
        self.game_zone.pack(padx=5, pady=5)
        # On attribue le focus au plateau de jeu
        self.game_zone.focus_set()
     
    def draw_shape(self, x, y):
        """ Dessine la forme correspondante au joueur"""
        if self.active_player is 1:
            self.game_zone.create_line(x-40, y-40, x+40, y+40, width=3, fill="red")
            self.game_zone.create_line(x-40, y+40, x+40, y-40, width=3, fill="red")
        else:
            self.game_zone.create_oval(x-40, y-40, x+40, y+40, width=3, outline="green")
     
    def highlight_active_player(self):
        """ Change la couleur de la zone du joueur actif """
        if self.active_player is 1:
            self.player1_zone.config(bg="light green")
            self.player2_zone.config(bg="ivory")
        else:
            self.player2_zone.config(bg="light green")
            self.player1_zone.config(bg="ivory")
     
    # # # # # # # # # # # # # # #
    #      Mode 1/2 joueurs     #
    #   Lancement de la partie  #
    # # # # # # # # # # # # # # #
     
    def launch_game(self):
        """ Lance le jeu """
        self.default_variables()
        self.bind_click()
 
    # # # # # # # # # # # #
    #   Mode 1/2 joueurs   #
    #  Popup de dialogues  #
    # # # # # # # # # # # #
     
    def new_game_dialog(self):
        """ Popup de confirmationd de nouvelle partie """
        if askyesno("Nouvelle Manche", "Le tableau de jeu sera effacé. Continuer ?"):
            self.clear_board()
        else:
            pass
     
    def exit_dialog(self):
        """ Popup de confirmationd pour quitter """
        if askyesno("Quitter", "Voulez-vous vraiment quitter ?"):
            self.destroy()
        else:
            pass
     
    # # # # # # # # # # # # # # # #
    #       Mode 1/2 joueurs      #
    #   Réinitialisation du jeu   #
    # # # # # # # # # # # # # # # #
     
    def clear_board(self):
        """ Nettoie le tableau de jeu """
        self.winfo_children()[3].destroy()
        self.player1_zone.itemconfig(self.player1_score,text ="Score : %d " %Player1.score)
        self.player2_zone.itemconfig(self.player2_score,text ="Score : %d " %Player2.score)
        self.player1_zone.config(bg="light green")
        self.player2_zone.config(bg="ivory")
        self.draw_game_zone()
        self.launch_game()
     
    # # # # # # # # # # # # #
    #    Mode 1/2 joueurs    #
    #  Gestion de la souris  #
    # # # # # # # # # # # # #
     
    def bind_click(self):
        """ Associe le click gauche à la fonction click_event """
        self.game_zone.bind("<Button-1>", self.click_event)
     
    def click_event(self, event):
        """ Analyse de la position de la souris sur les cases du canevas game_zone,
        appelle la fonction de dessin des motifs, puis check_victory() et next_turn() """
     
        if self.game_mode is 2 or self.game_mode is 1 and self.active_player is 1:
            x = int(event.x/100)
            y = int(event.y /100)
            if self.game_table[y][x] == 0:
                self.player_move(y, x, self.active_player)
     
    def player_move(self, y, x, mark):
            self.game_table[y][x] = mark
            self.x = x*100+50
            self.y = y*100+50
            self.draw_shape(self.x, self.y)
            self.next_turn()
 
    # # # # # # # # # # # # # # # # # #
    #         Mode 1/2 joueurs        #
    #  Gestion des évènements de jeu  #
    # # # # # # # # # # # # # # # # # #
     
    def check_victory(self, board, mark):
        """ Vérifie si il existe une combinaison gagnante sur le tableau """
        for i in board:
            if np.array_equal(i, [mark]*3):
                return True
 
        for i in range (0, 3):
            if (board[0][i] == board[1][i] == board[2][i] == mark):
                return True
                 
        if (board [0][0] == board [1][1] == board [2][2] == mark) or (board [0][2] == board [1][1] == board [2][0] == mark):
            return True
        return False
         
    def next_turn(self):
        """ Affiche un message de victoire ou d'égalité, ou passe au tour suivant en fonction de check_victory() """
        if self.check_victory(self.game_table, self.active_player):
            if self.active_player is 1:
                winner_name = Player1.name
                Player1.score += 1
            elif self.active_player is 2:
                winner_name = Player2.name
                Player2.score += 1
            showinfo("Fin de la partie", "Victoire de {}".format(winner_name))
            self.clear_board()
         
        elif 0 not in self.game_table:
            showinfo("Fin de la partie", "Égalité")
            self.clear_board()
             
        else:
            if self.active_player is 1:
                self.active_player = 2
                if self.game_mode is 1:
                    self.ia_move()
            elif self.active_player is 2:
                self.active_player = 1
        self.highlight_active_player()
 
     
    # # # # # # # # # #
    #  Mode 1 Joueur  #
    # # # # # # # # # #
     
    def single_player_mode(self):
        """ Initialise le mode solo """
        self.game_mode = 1
        # Destruction des éléments non utilisés
        for i in range(1,4):
            self.winfo_children()[1].destroy()
 
        self.center_window()
        self.top_menu.entryconfig(1,state=ACTIVE)
             
        # Ajout du joueur et de l'IA
        self.add_players()
         
        # Dessin des zones
        self.draw_player_zone()
        self.draw_game_zone()
        self.center_window()
         
        # Sélection des noms, activation du menu + lancement partie
        self.get_name()
        self.top_menu.entryconfig(1,state=ACTIVE)
        self.launch_game()
     
    # # # # # # # # # # # # # # # #
    #        Mode 1 Joueur        #
    #  Intelligence artificielle  #
    # # # # # # # # # # # # # # # #
     
    def ia_move(self):
        y, x = self.choose_ia_move()
       (())
        self.player_move(y, x, self.active_player)
     
    def choose_ia_move(self):
        """ Cherche la meilleure position où jouer pour l'IA """
         
        # On définit les coins et les côtés
        self.corners = ( [0,0], [0,2], [2,0], [2,2] )
        self.sides = ( [0,1], [1,0], [1,2], [2,1] )
         
        # On cherche si l'IA peut gagner au coup suivant
        for i in range(0,3):
            for j in range(0,3):
                self.game_table_copy = np.copy(self.game_table)
                if self.game_table_copy[i][j] == 0:
                    self.game_table_copy[i][j] = 2
                    if self.check_victory(self.game_table_copy, 2):
                        return i,j
         
        # On cherche si le joueur peut gagner au coup suivant
        for i in range(0,3):
            for j in range(0,3):
                self.game_table_copy = np.copy(self.game_table)
                if self.game_table_copy[i][j] == 0:
                    self.game_table_copy[i][j] = 1
                    if self.check_victory(self.game_table_copy, 1):
                        return i,j
         
        # Sinon on cherche un coin, on en prend un au hasard
        move = self.choose_random_move(self.corners)
        if move != None:
            return move[0],move[1]
             
        # Sinon, on prend le milieu s'il est libre
        if self.game_table[1][1] == 0:
            return 1,1
         
        # Sinon, on prend un côté au hasard
        return self.choose_random_move(self.sides)[0],self.choose_random_move(self.sides)[1]
 
    def choose_random_move(self, move_list):
        possible_moves = []
        for position in move_list:
            i = position[0]
            j = position[1]
            if self.game_table[i][j] == 0:
                possible_moves.append(position)
        if len(possible_moves) != 0:
            return random.choice(possible_moves)
        else:
            return None
             
# # # # # # # # # # # #
#  Boucle Principale  #
# # # # # # # # # # # #
 
if __name__ == "__main__":
     
    # # # # # # # # # # # # #
    #  Création des joueurs  #
    # # # # # # # # # # # # #
     
    Player1 = Player("Joueur 1")
    Player2 = Player("Joueur 2")
    AI = Player("Jackie")
     
    # # # # # # # # # # # # # # # # # #
    #  Création de la fenêtre de jeu  #
    # # # # # # # # # # # # # # # # # #
     
    TicTacToe = UI()
    TicTacToe.resizable(0,0)
    TicTacToe.mainloop()
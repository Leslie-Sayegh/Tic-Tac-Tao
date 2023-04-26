#import tkinter as tk

#app = tk.Tk() 

#message = tk.Label(app, text = "Tic-Tac-Toe")
#message.pack()

#app.mainloop()


import tkinter
from tkinter import *
from tkinter import messagebox 

#creer objet = creer pt fenetre 
window = Tk()
#titre fenetre
window.title("Tic-Tac-Toe")

# creer fonction
 
 #si x commence ca donne true
clicked = True
count = 0


# creer boutons (9 boutons)
b1 = Button(window, text=" ",font=("helvetica",20), height=3, width=6, bg="systemButtonFace", command=lambda: b_click(b1))
b2 = Button(window, text=" ",font=("helvetica",20), height=3, width=6, bg="systemButtonFace", command=lambda: b_click(b2))
b3 = Button(window, text=" ",font=("helvetica",20), height=3, width=6, bg="systemButtonFace", command=lambda: b_click(b3))

b4 = Button(window, text=" ",font=("helvetica",20), height=3, width=6, bg="systemButtonFace", command=lambda: b_click(b4))
b5 = Button(window, text=" ",font=("helvetica",20), height=3, width=6, bg="systemButtonFace", command=lambda: b_click(b5))
b6 = Button(window, text=" ",font=("helvetica",20), height=3, width=6, bg="systemButtonFace", command=lambda: b_click(b6))

b7 = Button(window, text=" ",font=("helvetica",20), height=3, width=6, bg="systemButtonFace", command=lambda: b_click(b7))
b8 = Button(window, text=" ",font=("helvetica",20), height=3, width=6, bg="systemButtonFace", command=lambda: b_click(b8))
b9 = Button(window, text=" ",font=("helvetica",20), height=3, width=6, bg="systemButtonFace", command=lambda: b_click(b9))

# creer une grille pour poser les bouttons
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

# donner fonction aux boutons
# fonction du cick
def b_click(b) :
    global clicked, count
    if b["text"] == " " and clicked == True :
        b["text"] = "X"
        clicked = False
        count += 1
        checkifwon()
    elif b["text"] == " " and clicked == False :
          b["text"] = "O"
          clicked = True
          count += 1
          checkifwon()
    else :
         messagebox.showerror ("Tic Tac Toe","Hey! ce carreaux est deja utilise \nChoisit un autre ...")

#fonction verifier si joueur gagne
def checkifwon() :
     global winner
     winner = False
     if b1["text"] == "X" and b2["text"]  == "X" and b3["text"] == "X" :
         b1.config(bg = "green")
         b2.config(bg = "green")
         b3.config(bg = "green")
         winner = True
         messagebox.showinfo("Tic Tac Toe", "Joueur X Gagnant")
         disable_buttons()
     elif b4["text"] == "X" and b5["text"]  == "X" and b6["text"] == "X" :
           b4.config(bg = "green")
           b5.config(bg = "green")
           b6.config(bg = "green")
           winner = True
           messagebox.showinfo("Tic Tac Toe", "Joueur X Gagnant")
           disable_buttons()
     elif b7["text"] == "X" and b8["text"]  == "X" and b9["text"] == "X" :
           b7.config(bg = "green")
           b8.config(bg = "green")
           b9.config(bg = "green")
           winner = True
           messagebox.showinfo("Tic Tac Toe", "Joueur X Gagnant")
           disable_buttons()
     elif b1["text"] == "X" and b4["text"]  == "X" and b7["text"] == "X" :
           b1.config(bg = "green")
           b4.config(bg = "green")
           b7.config(bg = "green")
           winner = True
           messagebox.showinfo("Tic Tac Toe", "Joueur X Gagnant")
           disable_buttons()         
     elif b2["text"] == "X" and b5["text"]  == "X" and b8["text"] == "X" :
           b2.config(bg = "green")
           b5.config(bg = "green")
           b8.config(bg = "green")
           winner = True
           messagebox.showinfo("Tic Tac Toe", "Joueur X Gagnant")
           disable_buttons()
     elif b3["text"] == "X" and b6["text"]  == "X" and b9["text"] == "X" :
           b3.config(bg = "green")
           b6.config(bg = "green")
           b9.config(bg = "green")
           winner = True
           messagebox.showinfo("Tic Tac Toe", "Joueur X Gagnant")
           disable_buttons()
     elif b3["text"] == "X" and b5["text"]  == "X" and b7["text"] == "X" :
           b3.config(bg = "green")
           b5.config(bg = "green")
           b7.config(bg = "green")
           winner = True
           messagebox.showinfo("Tic Tac Toe", "Joueur X Gagnant")
           disable_buttons()
     elif b1["text"] == "X" and b5["text"]  == "X" and b9["text"] == "X" :
           b1.config(bg = "green")
           b5.config(bg = "green")
           b9.config(bg = "green")
           winner = True
           messagebox.showinfo("Tic Tac Toe", "Joueur X Gagnant")
           disable_buttons()
     elif b1["text"] == "O" and b2["text"]  == "O" and b3["text"] == "O" :
           b1.config(bg = "green")
           b2.config(bg = "green")
           b3.config(bg = "green")
           winner = True
           messagebox.showinfo("Tic Tac Toe", "Joueur O Gagnant")
           disable_buttons()
     elif b4["text"] == "O" and b5["text"]  == "O" and b6["text"] == "O" :
           b4.config(bg = "green")
           b5.config(bg = "green")
           b6.config(bg = "green")
           winner = True
           messagebox.showinfo("Tic Tac Toe", "Joueur O Gagnant")
           disable_buttons()
     elif b7["text"] == "O" and b8["text"]  == "O" and b9["text"] == "O" :
           b7.config(bg = "green")
           b8.config(bg = "green")
           b9.config(bg = "green")
           winner = True
           messagebox.showinfo("Tic Tac Toe", "Joueur O Gagnant")
           disable_buttons()
     elif b1["text"] == "O" and b4["text"]  == "O" and b7["text"] == "O" :
           b1.config(bg = "green")
           b4.config(bg = "green")
           b7.config(bg = "green")
           winner = True
           messagebox.showinfo("Tic Tac Toe", "Joueur O Gagnant")
           disable_buttons()         
     elif b2["text"] == "O" and b5["text"]  == "O" and b8["text"] == "O" :
           b2.config(bg = "green")
           b5.config(bg = "green")
           b8.config(bg = "green")
           winner = True
           messagebox.showinfo("Tic Tac Toe", "Joueur O Gagnant")
           disable_buttons()
     elif b3["text"] == "O" and b6["text"]  == "O" and b9["text"] == "O" :
           b3.config(bg = "green")
           b6.config(bg = "green")
           b9.config(bg = "green")
           winner = True
           messagebox.showinfo("Tic Tac Toe", "Joueur O Gagnant")
           disable_buttons()
     elif b3["text"] == "O" and b5["text"]  == "O" and b7["text"] == "O" :
           b3.config(bg = "green")
           b5.config(bg = "green")
           b7.config(bg = "green")
           winner = True
           messagebox.showinfo("Tic Tac Toe", "Joueur O Gagnant")
           disable_buttons()
     elif b1["text"] == "O" and b5["text"]  == "O" and b9["text"] == "O" :
           b1.config(bg = "green")
           b5.config(bg = "green")
           b9.config(bg = "green")
           winner = True
           messagebox.showinfo("Tic Tac Toe", "Joueur O Gagnant")
           disable_buttons()

#verifier si egalite
     if count == 9 and winner == False :
        messagebox.showinfo("Tic Tac Toe","Match Nul")
        disable_buttons()

#fonction désactiver tt les boutons
def disable_buttons() :
     b1.config(state=DISABLED)
     b2.config(state=DISABLED)
     b3.config(state=DISABLED)
     b4.config(state=DISABLED)
     b5.config(state=DISABLED)
     b6.config(state=DISABLED)
     b7.config(state=DISABLED)
     b8.config(state=DISABLED)
     b9.config(state=DISABLED)


#afficher la fenetre
window.mainloop()



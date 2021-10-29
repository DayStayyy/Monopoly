from tkinter import *
from tkinter.messagebox import *
# ----------------------------------------------------------------

# Engine

# ----------------------------------------------------------------

# lancerJeux(nbJoueur,monopole,possederXArgent,argentMax) :


def play(check2, check3, nbJoueur, fen_princ, argentMax, lancerJeux, joueur1, joueur2, joueur3, joueur4):
    err = False
    errmoney = False
    try:
        nbJoueur = int(nbJoueur)
    except:
        print("Nombre de joueur invalide")
        err = True
        pass
    if check2 == 1:
        print("3 Monopole")
    if check3 == 1:
        print("Posseder")
        try:
            argentMax = int(argentMax)
            print(argentMax)
        except:
            print("Argent max invalide")
            errmoney = True
    if err or nbJoueur > 4:
        showinfo('Erreur', 'Erreur nombre de joueur invalide')
    elif errmoney:
        showinfo('Erreur', 'Erreur argent max invalide')
    else:
        fen_princ.destroy()
        NamePlayer = [joueur1, joueur2, joueur3, joueur4]
        lancerJeux(nbJoueur, check2, check3, argentMax, NamePlayer)
# ----------------------------------------------------------------

# Interface graphique

# ----------------------------------------------------------------


def interface_menu(fenetre, lancerJeux):

    MenuPrinc = Canvas(fenetre, width=700, height=720, background='snow3')
    MenuPrinc.chkValue_1 = BooleanVar()
    MenuPrinc.chkValue_2 = BooleanVar()
    MenuPrinc.chkValue_3 = BooleanVar()

    # Création de nos widgets

    MenuPrinc.create_rectangle(
        225, 60, 475, 150, width=4, outline='white', fill='red')
    MenuPrinc.create_text(350, 100, text="Monopoly",
                          font=(None, 40), fill='white')
    MenuPrinc.create_text(
        350, 350, text="N'oublie pas les options \n            ↓   ↓   ↓", font=(None, 20))
    MenuPrinc.create_line(0, 400, 700, 400, width=2, fill="black")

    MenuPrinc.textenbjoueur = Label(fenetre, text="Nombre de joueurs", font=(
        None, 20), height=3, background='snow3')
    MenuPrinc.textenbjoueur.place(x=20, y=450)

    MenuPrinc.NameJoueurs = Label(fenetre, text="Nom des joueurs", font=(
        None, 20), height=3, background='snow3')
    MenuPrinc.NameJoueurs.place(x=20, y=520)

    MenuPrinc.joueur1 = StringVar()
    Name1 = Entry(fenetre, textvariable=MenuPrinc.joueur1, width=30)
    Name1.pack()
    Name1.place(x=20, y=600)
    MenuPrinc.joueur2 = StringVar()
    Name2 = Entry(fenetre,  textvariable=MenuPrinc.joueur2, width=30)
    Name2.pack()
    Name2.place(x=20, y=630)
    MenuPrinc.joueur3 = StringVar()
    Name3 = Entry(fenetre,  textvariable=MenuPrinc.joueur3, width=30)
    Name3.pack()
    Name3.place(x=20, y=660)
    MenuPrinc.joueur4 = StringVar()
    Name4 = Entry(fenetre,  textvariable=MenuPrinc.joueur4, width=30)
    Name4.pack()
    Name4.place(x=20, y=690)

    MenuPrinc.nbJoueur = StringVar()
    entreenbjoueur = Spinbox(
        fenetre, from_=2, to=4, textvariable=MenuPrinc.nbJoueur, font=(None, 15), width=2)
    entreenbjoueur.pack()
    entreenbjoueur.place(x=260, y=490)

    MenuPrinc.texte = Label(fenetre, text="Conditions de victoire(s) \n↓   ↓   ↓", font=(
        None, 15), height=3, background='snow3')
    MenuPrinc.texte.place(x=455, y=420)

    MenuPrinc.bouton2 = Checkbutton(fenetre, text="3 Monopoles", font=(
        None, 15), var=MenuPrinc.chkValue_2, background='snow3')
    MenuPrinc.bouton2.place(x=470, y=515)

    MenuPrinc.bouton3 = Checkbutton(fenetre, text="Posseder                 $", font=(
        None, 15), var=MenuPrinc.chkValue_3, background='snow3')
    MenuPrinc.bouton3.place(x=470, y=550)

    MenuPrinc.argentMax = StringVar()
    entreeargentMax = Spinbox(fenetre, from_=10000, to=1000000, textvariable=MenuPrinc.argentMax, font=(
        None, 15), width=7, increment=1000)
    entreeargentMax.pack()
    entreeargentMax.place(x=582, y=555)

    MenuPrinc.bouton_jouer = Button(fenetre, text="Lancer la partie", font=(None, 20), command=lambda a=0: play(
        MenuPrinc.chkValue_2.get(), MenuPrinc.chkValue_3.get(), MenuPrinc.nbJoueur.get(), fenetre, MenuPrinc.argentMax.get(), lancerJeux, MenuPrinc.joueur1.get(), MenuPrinc.joueur2.get(), MenuPrinc.joueur3.get(), MenuPrinc.joueur4.get()))
    MenuPrinc.bouton_jouer.place(x=245, y=175)
    MenuPrinc.pack()


# ----------------------------------------------------------------

# Corps du programme

# ----------------------------------------------------------------
def start_menu(lancerJeux):
    fen_princ = Tk()
    fen_princ.title("Menu")
    fen_princ.geometry("700x720")

    interface_menu(fen_princ, lancerJeux)
    fen_princ.mainloop()

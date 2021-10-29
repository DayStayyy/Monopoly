from random import randint
import os


def startPendu(nom1, nom2):
    print("Vous devez ecrire le mot complet pour gagner !\nEcrivez 1 lettre pour deviner une lettre ou plusieurs lettres pour deviner le mot \nIl n'y a pas d'espace dans les mots")
    listeMots = ["jambon", "brebis", "dromadaire", "avion", "diplodocus", "justice", "bureau", "pasteque", "mathematique", "aventure", "consoles", "dictionnaire", "histoire", "estomac", "baignoire", "parapluie", "sauvage", "patate", "dehors", "ordinateur",
                 "poubelle", "rideau", "jouets", "fatigue", "arbre", "fleur", "extincteur", "horloge"]
    victoire = False

    listJoueur = [nom1, nom2]
    joueursTours = 0

    nbMot = randint(0, len(listeMots)-1)
    motMasquer = []
    mot = listeMots[nbMot]
    for i in mot:
        motMasquer.append("_")
    while victoire != True:
        print("mot : ", end='')
        for i in motMasquer:
            print(i, end='')
            print(" ", end='')
        print(" \n C'est au tour de {} de joueur\nVous devez ecrire le mot complet pour gagner !".format(
            listJoueur[joueursTours]))
        réponse = input("Quel lettre/mot voulez vous tentez ? ")
        if len(réponse) == 1:
            print(mot)
            for i in range(len(mot)):
                if mot[i] == réponse:
                    motMasquer[i] = réponse
        elif mot == réponse:
            victoire = True
            break

        os.system("CLS")

        if victoire != True:
            if joueursTours == 0:
                joueursTours = 1
            else:
                joueursTours = 0

    print("Le joueur {} a gagner".format(listJoueur[joueursTours]))
    return listJoueur[joueursTours]
from random import randrange
import os


def startBatons(nom1, nom2):
    print("Le joueur qui tire le dernier batons a perdu")
    nbBatons = randrange(21, 40)

    listJoueur = [nom1, nom2]
    joueursTours = 0

    while nbBatons >= 1:

        print("C'est au tou de {} de joueur".format(
            listJoueur[joueursTours]))
        print("Il reste {} batons".format(nbBatons))
        nombreValide = False
        while nombreValide != True:
            try:
                nbBatonsEnlever = int(
                    input("Combien de batons voulez vous enlevez ? (1,2 ou 3) "))
                if nbBatonsEnlever > 0 and nbBatonsEnlever < 4:
                    nombreValide = True
            except:
                pass
            print("Veuillez entrez un chiffre valide")
        nbBatons -= nbBatonsEnlever

        os.system("CLS")

        if joueursTours == 1:
            joueursTours = 0
        else:
            joueursTours = 1

    print("Le joueur {} a gagner".format(listJoueur[joueursTours]))
    return listJoueur[joueursTours]

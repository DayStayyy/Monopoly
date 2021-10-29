import os


class Joueur(object):

    def __init__(self, nom, symbole):
        self.nom = nom
        self.symbole = symbole


def startPuissance4(nom1, nom2):
    # init variables
    joueur_tours = 1
    etage_0 = 0
    etage_1 = 0
    etage_2 = 0
    etage_3 = 0
    etage_4 = 0
    etage_5 = 0
    etage_6 = 0

    # init liste
    colonne_0 = [" ", " ", " ", " ", " ", " "]
    colonne_1 = [" ", " ", " ", " ", " ", " "]
    colonne_2 = [" ", " ", " ", " ", " ", " "]
    colonne_3 = [" ", " ", " ", " ", " ", " "]
    colonne_4 = [" ", " ", " ", " ", " ", " "]
    colonne_5 = [" ", " ", " ", " ", " ", " "]
    colonne_6 = [" ", " ", " ", " ", " ", " "]
    list_joueur = []
    list_colonne = [colonne_0, colonne_1, colonne_2,
                    colonne_3, colonne_4, colonne_5, colonne_6]
    list_etage = [etage_0, etage_1, etage_2,
                  etage_3, etage_4, etage_5, etage_6]

    # sys nom et symbole
    joueurs = Joueur(nom1, "O")
    list_joueur.append(joueurs)
    joueurs = Joueur(nom2, "X")
    list_joueur.append(joueurs)

    print("  1   2   3   4   5   6   7 \n"
          "|", list_colonne[0][5], "|", list_colonne[1][5], "|", list_colonne[2][5], "|", list_colonne[
              3][5], "|", list_colonne[4][5], "|", list_colonne[5][5], "|", list_colonne[6][5], "|""\n"
          "|", list_colonne[0][4], "|", list_colonne[1][4], "|", list_colonne[2][4], "|", list_colonne[
              3][4], "|", list_colonne[4][4], "|", list_colonne[5][4], "|", list_colonne[6][4], "|""\n"
          "|", list_colonne[0][3], "|", list_colonne[1][3], "|", list_colonne[2][3], "|", list_colonne[
              3][3], "|", list_colonne[4][3], "|", list_colonne[5][3], "|", list_colonne[6][3], "|""\n"
          "|", list_colonne[0][2], "|", list_colonne[1][2], "|", list_colonne[2][2], "|", list_colonne[
              3][2], "|", list_colonne[4][2], "|", list_colonne[5][2], "|", list_colonne[6][2], "|""\n"
          "|", list_colonne[0][1], "|", list_colonne[1][1], "|", list_colonne[2][1], "|", list_colonne[
              3][1], "|", list_colonne[4][1], "|", list_colonne[5][1], "|", list_colonne[6][1], "|""\n"
          "|", list_colonne[0][0], "|", list_colonne[1][0], "|", list_colonne[2][0], "|", list_colonne[
              3][0], "|", list_colonne[4][0], "|", list_colonne[5][0], "|", list_colonne[6][0], "|""\n"
          )

    while 1 == 1:

        # sys de tours
        if joueur_tours == 0:
            joueur_tours = 1

        elif joueur_tours == 1:
            joueur_tours = 0

        # Boucle dans la quel le joueur choisi une colone
        while 1 == 1:

            message = "Joueur " + \
                list_joueur[joueur_tours].nom + \
                " ou voulez vous placez votre pion ? (ex: 3) "
            emplacement = input(message)

            try:
                emplacement = int(emplacement)

                if emplacement > 0 and emplacement < 8:
                    emplacement -= 1

                    if list_etage[emplacement] < 6:
                        break
                    else:
                        print("La colonne choisie est pleine ")

                else:
                    print("Le chiffre entrez doit etre compris entre 1 et 7 inclus")

            except:
                print("Veuillez entrez un chiffre")

        while 1 == 1:
            list_colonne[emplacement][list_etage[emplacement]
                                      ] = list_joueur[joueur_tours].symbole
            list_etage[emplacement] += 1
            break

        os.system("CLS")

        print("  1   2   3   4   5   6   7 \n"
              "|", list_colonne[0][5], "|", list_colonne[1][5], "|", list_colonne[2][5], "|", list_colonne[
                  3][5], "|", list_colonne[4][5], "|", list_colonne[5][5], "|", list_colonne[6][5], "|""\n"
              "|", list_colonne[0][4], "|", list_colonne[1][4], "|", list_colonne[2][4], "|", list_colonne[
                  3][4], "|", list_colonne[4][4], "|", list_colonne[5][4], "|", list_colonne[6][4], "|""\n"
              "|", list_colonne[0][3], "|", list_colonne[1][3], "|", list_colonne[2][3], "|", list_colonne[
                  3][3], "|", list_colonne[4][3], "|", list_colonne[5][3], "|", list_colonne[6][3], "|""\n"
              "|", list_colonne[0][2], "|", list_colonne[1][2], "|", list_colonne[2][2], "|", list_colonne[
                  3][2], "|", list_colonne[4][2], "|", list_colonne[5][2], "|", list_colonne[6][2], "|""\n"
              "|", list_colonne[0][1], "|", list_colonne[1][1], "|", list_colonne[2][1], "|", list_colonne[
                  3][1], "|", list_colonne[4][1], "|", list_colonne[5][1], "|", list_colonne[6][1], "|""\n"
              "|", list_colonne[0][0], "|", list_colonne[1][0], "|", list_colonne[2][0], "|", list_colonne[3][0], "|", list_colonne[4][0], "|", list_colonne[5][0], "|", list_colonne[6][0], "|""\n")

        # On verifie la victoire sur le bas
        etage = list_etage[emplacement]
        etage -= 1
        nb_symbole = 1
        while list_colonne[emplacement][etage] == list_joueur[joueur_tours].symbole:
            etage -= 1
            if etage < 0:
                break
            nb_symbole += 1

        if nb_symbole >= 4:
            break

        # On verifie la victoire sur la gauche
        emplacement_save = emplacement
        nb_symbole = 1
        emplacement_save -= 1
        etage = list_etage[emplacement]
        etage -= 1
        while list_colonne[emplacement_save][etage] == list_joueur[joueur_tours].symbole:
            emplacement_save -= 1
            nb_symbole += 1
            nb_symbole += 1
            if etage < 0:
                break

        if nb_symbole >= 4:
            break

        # On verifie la victoire sur la droite
        emplacement_save = emplacement
        emplacement_save += 1
        etage = list_etage[emplacement]
        etage -= 1
        if emplacement_save < 7:
            while list_colonne[emplacement_save][etage] == list_joueur[joueur_tours].symbole:
                emplacement_save += 1
                nb_symbole += 1
                if etage < 0:
                    break
                if emplacement_save > 6:
                    break
        if nb_symbole >= 4:
            break

        # On verifie la victoire sur la diagonale haut droite
        nb_symbole = 1
        emplacement_save = emplacement
        emplacement_save += 1
        etage = list_etage[emplacement]
        if emplacement_save < 7:
            while list_colonne[emplacement_save][etage] == list_joueur[joueur_tours].symbole:
                emplacement_save += 1
                etage += 1
                nb_symbole += 1
                if emplacement_save > 6:
                    break

        if nb_symbole >= 4:
            break

        # On verifie la victoire sur la diagonale bas gauche
        emplacement_save = emplacement
        emplacement_save -= 1
        etage = list_etage[emplacement]
        etage -= 2
        print(list_colonne[emplacement_save][etage])
        while list_colonne[emplacement_save][etage] == list_joueur[joueur_tours].symbole:
            emplacement_save -= 1
            etage -= 1
            nb_symbole += 1
            if etage < 0:
                break
        if nb_symbole >= 4:
            break

        # On verifie la victoire sur la diagonale haut gauche
        nb_symbole = 1
        emplacement_save = emplacement
        emplacement_save -= 1
        etage = list_etage[emplacement]
        while list_colonne[emplacement_save][etage] == list_joueur[joueur_tours].symbole:
            emplacement_save -= 1
            etage += 1
            nb_symbole += 1
            if etage > 5:
                break

        if nb_symbole >= 4:
            break

        # On verifie la victoire sur la diagonale bas droite
        emplacement_save = emplacement
        emplacement_save += 1
        etage = list_etage[emplacement]
        etage -= 2
        if emplacement_save < 7:
            while list_colonne[emplacement_save][etage] == list_joueur[joueur_tours].symbole:
                emplacement_save += 1
                etage -= 1
                nb_symbole += 1
                if etage < 0:
                    break
                if emplacement_save > 6:
                    break

            if nb_symbole >= 4:
                break

    print(list_joueur[joueur_tours].nom, "a gagner")
    return joueur_tours

import os


class Joueur(object):

    def __init__(self, nom, symbole):
        self.nom = nom
        self.symbole = symbole


def startMorpion(nom1, nom2):
    # init variables
    boucle_principale = 1
    boucle_coordonnes = 1
    modif = 0
    joueur_tours = 1
    a = 2
    suite = 0

    # init lignes
    ligne_1 = [" ", " ", " "]
    ligne_2 = [" ", " ", " "]
    ligne_3 = [" ", " ", " "]
    list_ligne = [ligne_1, ligne_2, ligne_3]
    list_joueur = []
    coord_list = []

    joueurs = Joueur(nom1, "O")
    list_joueur.append(joueurs)

    joueurs = Joueur(nom2, "X")
    list_joueur.append(joueurs)

    print("   A   B   C ")
    print("#############")
    print("#", list_ligne[0][0], "|", list_ligne[0]
          [1], "|", list_ligne[0][2], "# 1")
    print("#", list_ligne[1][0], "|", list_ligne[1]
          [1], "|", list_ligne[1][2], "# 2")
    print("#", list_ligne[2][0], "|", list_ligne[2]
          [1], "|", list_ligne[2][2], "# 3")
    print("#############")

    while boucle_principale == 1:

        boucle_coordonnes = 1

        if joueur_tours == 0:
            joueur_tours = 1

        elif joueur_tours == 1:
            joueur_tours = 0

        while 1 == 1:

            message = "Joueur " + \
                list_joueur[joueur_tours].nom + \
                " ou voulez vous placez votre symbole ? (ex: A3) "
            coord = input(message)
            coord = str(coord)
            coord = coord.lower()

            coord_list = []

            for i in coord:
                coord_list.append(i)

            while 1 == 1:

                if len(coord_list) > 2:
                    print("Veuillez entre seulement deux coordonnées")
                    break

                elif coord_list[0] != "a" and coord_list[0] != "b" and coord_list[0] != "c":
                    print("Veuillez entre A,B ou C en premier")
                    break

                elif coord_list[1] != "1" and coord_list[1] != "2" and coord_list[1] != "3":
                    print("Veuillez entre 1,2 ou 3 en deuxieme")
                    break

                if coord_list[0] == "a":
                    coord_list[0] = 0

                elif coord_list[0] == "b":
                    coord_list[0] = 1

                elif coord_list[0] == "c":
                    coord_list[0] = 2

                coord_list[1] = int(coord_list[1])
                coord_list[1] -= 1
                suite = 1
                break

            while suite == 1:
                if list_ligne[coord_list[1]][coord_list[0]] == " ":
                    list_ligne[coord_list[1]][coord_list[0]
                                              ] = list_joueur[joueur_tours].symbole
                    boucle_coordonnes = 0
                    suite = 0
                    break
                else:
                    print("L'emplacement choisi est deja utilisé")
                    suite = 0
                    break
            if boucle_coordonnes == 0:
                break

        os.system("CLS")

        print("   A   B   C ")
        print("#############")
        print("#", list_ligne[0][0], "|", list_ligne[0]
              [1], "|", list_ligne[0][2], "# 1")
        print("#", list_ligne[1][0], "|", list_ligne[1]
              [1], "|", list_ligne[1][2], "# 2")
        print("#", list_ligne[2][0], "|", list_ligne[2]
              [1], "|", list_ligne[2][2], "# 3")
        print("#############")

        if list_ligne[0][0] != " ":
            if list_ligne[0][0] == list_ligne[0][1] and list_ligne[0][2] == list_ligne[0][0]:
                break
            elif list_ligne[0][0] == list_ligne[1][0] and list_ligne[2][0] == list_ligne[0][0]:
                break
            elif list_ligne[0][0] == list_ligne[1][1] and list_ligne[2][2] == list_ligne[0][0]:
                break

        if list_ligne[1][1] != " ":
            if list_ligne[1][0] == list_ligne[1][1] and list_ligne[1][2] == list_ligne[1][0]:
                break

            elif list_ligne[2][0] == list_ligne[1][1] and list_ligne[1][1] == list_ligne[0][2]:
                break

            elif list_ligne[0][1] == list_ligne[1][1] and list_ligne[2][1] == list_ligne[0][1]:
                break

        if list_ligne[2][2] != " ":
            if list_ligne[2][0] == list_ligne[2][1] and list_ligne[2][2] == list_ligne[2][0]:
                break

            elif list_ligne[0][2] == list_ligne[1][2] and list_ligne[2][2] == list_ligne[0][2]:
                break

    print(list_joueur[joueur_tours].nom, "a gagner")
    return joueur_tours

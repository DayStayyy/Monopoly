import os
import colored
from colored import stylize
from engine import initRue
from engine import initPlateau
from engine import initJoueur
from Classes.Joueur import Joueur


def FormatCellName(s, nbchar=-1):
    if nbchar == -1:
        length = len(s)
    else:
        length = nbchar
    end = True
    while length < 17:
        if end == True:
            s += " "
            end = False
        else:
            s = " " + s
            end = True
        length += 1
    return s


def FormatBlankSpace(s):
    length = len(s)
    end = True
    while length < 161:
        if end == True:
            s += " "
            end = False
        else:
            s = " " + s
            end = True
        length += 1
    return s


def AffPlateau(plateau, joueur, listejoueurs, textes):
    os.system("CLS")
    # Premiere ligne
    i = 0
    print("="*199)
    while i < 11:
        cell = plateau[i]
        if i == 0:
            print("|", end="")
        try:
            print(stylize(FormatCellName(cell.nom),
                          colored.fg(cell.couleur)), end='|')
        except:
            print(FormatCellName(cell.nom), end='|')
        i += 1
    print("")

    # espace premiere ligne
    i = 0
    listecoo = []
    for alljoueur in listejoueurs:
        listecoo.append(alljoueur.position - 1)
    while i < 11:
        stringBilles = ""
        nbBilles = 0
        cell = plateau[i]
        if i == 0:
            print("|", end="")
        if i in listecoo:
            for alljoueur in listejoueurs:
                if i == alljoueur.position-1:
                    stringBilles += stylize("°", colored.fg(alljoueur.couleur))
                    nbBilles += 1
        try:
            print(FormatCellName(stringBilles, nbBilles), end='|')
        except:
            print(FormatCellName(""), end='|')
        i += 1
    print("")
    print("="*199)

    # Deuxieme et quatrieme lignes
    j = 43
    k = 0
    while i < 22:
        cell = plateau[i]
        cell2 = plateau[j]
        print("|", end="")
        try:
            print(stylize(FormatCellName(cell2.nom),
                          colored.fg(cell2.couleur)), end="")
        except:
            print(FormatCellName(cell2.nom), end="")
        print("|", end="")
        print(FormatBlankSpace(textes[k]), end="")
        print("|", end="")
        try:
            print(stylize(FormatCellName(cell.nom),
                          colored.fg(cell.couleur)), end="")
        except:
            print(FormatCellName(cell.nom), end="")
        print("|")
        # espace deuxieme, derniere ligne à remplacer
        k += 1
        print("|", end="")
        stringBilles = ""
        nbBilles = 0
        cell = plateau[i]
        if j in listecoo:
            for alljoueur in listejoueurs:
                if j == alljoueur.position-1:
                    stringBilles += stylize("°", colored.fg(alljoueur.couleur))
                    nbBilles += 1
        try:
            print(FormatCellName(stringBilles, nbBilles), end='|')
        except:
            print(FormatCellName(""), end='|')
        print(FormatBlankSpace(textes[k]), end="")
        k += 1
        print("|", end="")
        stringBilles = ""
        nbBilles = 0
        cell = plateau[i]
        if i in listecoo:
            for alljoueur in listejoueurs:
                if i == alljoueur.position-1:
                    stringBilles += stylize("°", colored.fg(alljoueur.couleur))
                    nbBilles += 1
        try:
            print(FormatCellName(stringBilles, nbBilles), end='')
        except:
            print(FormatCellName(""), end='')
        print("|")
        print("|", end="")
        print("=================", end="")
        print("|", end="")
        if i == 21:
            print("="*161, end="")
        else:
            print(FormatBlankSpace(textes[k]), end="")
        print("|", end="")
        print("=================", end="")
        print("|")
        i += 1
        j -= 1
        k += 1

    # troisieme ligne
    i = 32
    while i > 21:
        cell = plateau[i]
        if i == 32:
            print("|", end="")
        try:
            print(stylize(FormatCellName(cell.nom),
                          colored.fg(cell.couleur)), end='|')
        except:
            print(FormatCellName(cell.nom), end='|')
        i -= 1
    print("")
    # espace troisieme ligne à remplacer
    i = 32
    while i > 21:
        stringBilles = ""
        nbBilles = 0
        cell = plateau[i]
        if i == 32:
            print("|", end="")
        if i in listecoo:
            for alljoueur in listejoueurs:
                if i == alljoueur.position-1:
                    stringBilles += stylize("°", colored.fg(alljoueur.couleur))
                    nbBilles += 1
        try:
            print(FormatCellName(stringBilles, nbBilles), end='|')
        except:
            print(FormatCellName(""), end='|')
        i -= 1
    print("")
    print("="*199)


def AffInfo(joueur, nom, plateau, listeJoueur):
    textes = [""] * 32
    textespropr = ""
    textes[0] = "C'est au tour de {}, Il possède {} euros et a les propriétés suivantes :".format(
        joueur.nom, joueur.argent)
    i = 3
    if joueur.proprieter:
        for proprietes in joueur.proprieter:
            if proprietes == joueur.proprieter[0]:
                textespropr += proprietes.nom
            else:
                textespropr += ", " + proprietes.nom
            if len(textespropr) > 140:
                textes[i] = textespropr
                textespropr = ""
                i += 1
        textes[i] = textespropr
    else:
        textes[3] = "Il n'a pas de propriétés "
    textes[20] = "Il est actuellement sur la case {} : {}".format(
        joueur.position, nom)
    AffPlateau(plateau, joueur, listeJoueur, textes)
    os.system("pause")
    os.system("CLS")

def messageProprieteJoueur(proprietaire, somme):
    print("Vous êtes sur la case de {}, vous payez {} ".format(proprietaire.nom, somme))
    os.system("pause")


def achatProposition(prix, argent):
    reponse = input(
        "Voulez-vous acheter cette propriété au prix de {}, vous avez actuellement {}, tapez oui pour acheter et autre chose pour refuser ".format(prix, argent))
    return reponse


def manqueArgent():
    print("Vous n'avez pas assez d'argent")
    os.system("pause")
    os.system("CLS")


def achatMessage():
    print("Vous avez réalisé cet achat avec succès")
    os.system("pause")
    os.system("CLS")


def achatMaison(prix, argent, loyer, nbMaison):
    reponse = input("Voulez-vous acheter une maison au prix de {},il y a actuellement {} maison sur cette prorpriété, l'achat ferait passer le loyer de {} à {} ,vous avez actuellement {}, tapez oui pour acheter et autre chose pour refuser ".format(prix, nbMaison, loyer, loyer*(nbMaison+1), argent))
    return reponse
    os.system("pause")


def messageLancerDes(des, de1, de2, plateau, joueur, listeJoueur):
    textes = [""] * 32
    textes[15] = "Vous avez avancé de {} cases".format(des)
    asciiDes = {1 :["/-------\\","|       |","|   o   |","|       |","\\-------/"],2 : ["/-------\\","|  o    |","|       |","|    o  |","\\-------/"],3:["/-------\\","|  o    |","|   o   |","|    o  |","\\-------/"],4:["/-------\\","| o   o |","|       |","| o   o |","\\-------/"],5:["/-------\\","| o   o |","|   o   |","| o   o |","\\-------/"],6:["/-------\\","| o   o |","| o   o |","| o   o |","\\-------/"]}
    de1ascii = asciiDes.get(de1)
    de2ascii = asciiDes.get(de2)
    textes[6] = de1ascii[0] + "        " + de2ascii[0]
    textes[7] = de1ascii[1] + "        " + de2ascii[1]
    textes[8] = de1ascii[2] + "        " + de2ascii[2]
    textes[9] = de1ascii[3] + "        " + de2ascii[3]
    textes[10] = de1ascii[4] + "        " + de2ascii[4]
    AffPlateau(plateau, joueur, listeJoueur, textes)
    os.system("pause")


def messageAvancement(position, nom):
    print("Vous êtes sur la case {} : {}".format(position, nom))


def messageVictoire(nom):
    print("{} a gagné".format(nom))


def messagePrison(nom, tours):
    print("{}, Lancez les dés pour obtenir votre liberté sans double dans {} tours vous payerez".format(nom, tours))
    os.system("pause")
    os.system("CLS")


def messagePrisonLose():
    print("Attention camarade, tu vas bientôt devoir payer")
    os.system("pause")
    os.system("CLS")


def messagePrisonWin():
    print("Tu as réussi à économiser ton argent, essaie de ne pas le perdre en tombant sur une case un peu trop chère")
    os.system("pause")
    os.system("CLS")


def messageMiniJeux():
    print("Vous êtes attéris sur une case Mini Jeu. Un joueur sera choisi au hasard puis vous miserez chacun 500 euros, un jeu sera choisis au hasard et vous vous affronterez dessus, le gagnant gagne la mise du perdant")
    os.system("CLS")


def messageApresRandomMiniJeux(nom):
    print("Le joueur tiré au sort est {}".format(nom))


def messageVictoirePersonne():
    print("Aucun joueur n'a gagner")


def messageCarteChance(message):
    print(message)
    os.system("pause")


def venteProprietesInfo(joueur):
    print("{} vous n'avez plus que {} euros, vous devez vendre des propriétés pour repasser en positif".format(
        joueur.nom, joueur.argent))
    for index, proprietes in enumerate(joueur.listeProprietes):
        print("Numéro {} {} : {} euros".format(
            index, proprietes.nom, proprietes.prix/2))


def venteProprietesQuestion():
    num = input("Entrez le numéro de la case que vous voulez vendre (vous pourrez en vendre plusieurs, mais une a la fois), sinon entrez \"abandon\" pour abandonner")
    return num


def nombreInvalide():
    print("Veuillez entrer nombre valide")


def perdu(nom):
    print("{} vous n'avez plus d'argent, la vente de toutes vos propriétés ne peut vous passer en positif, ou vous avez abandonnez")


def continuezVente():
    reponse = input(
        "Si vous voulez continuer à vendre des propriétés tapez oui sinon tapez autre chose : ")
    return reponse

# rues,_ = initRue()
# plateau = initPlateau(rues)
# joueur = Joueur("toto", 5)
# AffPlateau(plateau,joueur)

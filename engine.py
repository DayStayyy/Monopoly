from random import randint
from Classes.Prison import Prison
from Classes.Attente import Attente
from Classes.Chance import Chance
from Classes.DirPrison import DirPrison
from Classes.Regles import Regles
from Classes.Depart import Depart
from Classes.Gare import Gare
from Classes.Joueur import Joueur
from Classes.Propriete import Propriete
from Classes.CaseMiniJeux import CaseMiniJeux
from miniJeux import Morpion
from miniJeux import Puissance4
from miniJeux import Pendu
from miniJeux import JeuxDesBatons


# ----------------------------------------------------------------

# Jeu

# ----------------------------------------------------------------

def changementJoueur(joueur, listeJoueur):
    if joueur.num == len(listeJoueur)-1:
        joueur = listeJoueur[0]
    else:
        joueur = listeJoueur[joueur.num+1]
    return joueur


def recuperationCase(position, plateau):
    return plateau[position-1]


def vaEnPrison(joueur):
    joueur.position = 12
    joueur.prison = True


def achat(joueur, case):
    joueur.argent -= case.prix
    joueur.proprieter.append(case)
    case.proprietere = joueur


def verifVictoire(listeJoueur, regles, plateau):
    for joueur in listeJoueur:
        if regles.argentMax:
            result, joueur = victoireArgent(listeJoueur, regles.argentMax)
            if result:
                return result, joueur
        if regles.monopole:
            result, joueur = victoireMonopole(
                plateau, listeJoueur, regles.dictionnaireCouleurs)
            if result:
                return result, joueur
        result, joueur = victoireSeul(listeJoueur)
        if result:
            return result, joueur
    return False, None


def victoireMonopole(plateau, listeJoueur, dictionnaireCouleurs):
    for joueur in listeJoueur:
        couleursPosseder = {}
        for proprieté in joueur.proprieter:
            if proprieté.couleur in couleursPosseder:
                couleursPosseder[proprieté.couleur] += 1
            else:
                couleursPosseder[proprieté.couleur] = 1
        nbMonopole = 0
        for couleurs, nombre in couleursPosseder.items():
            if dictionnaireCouleurs[couleurs] == nombre:
                nbMonopole += 1
        if nbMonopole >= 3:
            return True, joueur
    return False, None


def victoireSeul(listeJoueur):
    if len(listeJoueur) == 1:
        return True, listeJoueur[0]
    elif len(listeJoueur) == 0:
        return True, "Personne"
    else:
        return False, None


def victoireArgent(listeJoueur, argentMax):
    for joueur in listeJoueur:
        if joueur.argent >= int(argentMax):
            return True, joueur
    return False, None


def enleverJoueur(listeJoueur):
    for i in range(listeJoueur):
        joueur = listeJoueur[i]
        if joueur.argent <= 0:
            del listeJoueur[i]
    return listeJoueur


def lancerDes():
    double = False
    de1 = randint(1, 6)
    de2 = randint(1, 6)
    if de1 == de2:
        double = True
    addiDe = de1 + de2
    return addiDe, double, de1, de2

def venteProprietes(joueur,num) :
    joueur.argent += joueur.proprieter[num].prix/2
    joueur.proprieter.proprietere = None
    del joueur.proprieter[num] 

def supprimerJoueur(listeJoueur, joueur) :
    listeJoueur.remove(joueur) 
# ----------------------------------------------------------------

# Init Params

# ----------------------------------------------------------------


def initParam(nbJoueur, NamePlayer):
    listeJoueur = initJoueur(nbJoueur, NamePlayer)
    listeRue, dictionnaireCouleurs = initRue()
    plateau = initPlateau(listeRue)

    return listeJoueur, listeRue, plateau, dictionnaireCouleurs


def initJoueur(nbJoueur, NamePlayer):
    listeJoueur = []
    for i in range(nbJoueur):
        listeCouleur = ["blue","red","green","yellow"]
        nom = NamePlayer[i]
        listeJoueur.append(Joueur(nom, i, listeCouleur[i]))
    return listeJoueur


def initRue():
    listeCouleur = ["blue", "blue", "blue", "red", "red", "yellow", "yellow", "yellow", "green", "green", "green", "magenta", "magenta", "magenta", "orange_3", "orange_3",
                    "cyan", "cyan", "thistle_3", "thistle_3", "thistle_3", "gold_1", "gold_1", "gold_1", "turquoise_4", "turquoise_4", "light_coral", "light_coral", "light_coral", "purple_3", "purple_3", "purple_3"]
    listeNom = ["Rue de la paix", "Rue de la chance", "Rue du désastre", "Rue des pauvres", "Rue commerciale", "Rue du talent", "Le quartier chic", "Rue des gagnants", "Rue mélancolique", "Rue du désespoir", "Rue de la joie", "Rue du bonheur", "Rue des fruits", "Rue du soleil", "Rue de la passion", "Rue traditionelle", "Rue des égouts",
                "Rue de la maladie", "Rue du style", "Rue des affaires", "Rue hantée", "Rue décorative", "Rue des poissons", "Rue de la défense", "Quartier de l'or", "Quartier riche", "Rue des marchands", "Rue des magasins", "Quartier fidèle", "Rue de la force", "Rue des malheurs", "Quartier malade"]
    listePrix = [140, 150, 170, 180, 200, 210, 230, 240, 270, 290, 300, 310, 330, 340, 350,
                 360, 360, 370, 390, 400, 420, 430, 440, 460, 480, 500, 510, 530, 550, 570, 600, 620]
    listeRue = []
    for i in range(len(listeNom)):
        listeRue.append(
            Propriete(listeNom[i], listeCouleur[i], listePrix[i], listePrix[i]/2.5))
    dictionnaireCouleurs = {}
    for couleur in listeCouleur:
        if couleur in dictionnaireCouleurs:
            dictionnaireCouleurs[couleur] += 1
        else:
            dictionnaireCouleurs[couleur] = 1
    return listeRue, dictionnaireCouleurs


def initPlateau(listeRue):
    caseDepart = Depart()
    casePrison = Prison()
    caseChance = Chance()
    caseJeux = CaseMiniJeux(Morpion.startMorpion,
                            Puissance4.startPuissance4, JeuxDesBatons.startBatons, Pendu.startPendu)
    caseDirPrison = DirPrison()
    caseAttente = Attente()
    caseGare1 = Gare("Gare du N")
    caseGare2 = Gare("Gare de L")
    caseGare3 = Gare("Gare de E")
    caseGare4 = Gare("Gare S-L")
    plateau = [caseDepart, listeRue[0], listeRue[1], listeRue[2], caseJeux,
               listeRue[3], listeRue[4], caseGare1, listeRue[5], listeRue[6], listeRue[7], casePrison,
               listeRue[8], listeRue[9], caseGare2, listeRue[10],
               listeRue[11], listeRue[12], caseChance, listeRue[13], listeRue[14], listeRue[15],
               caseAttente, listeRue[16], listeRue[17], caseJeux, listeRue[18],
               listeRue[19], listeRue[20], caseGare3, listeRue[21], listeRue[22], listeRue[23],
               caseDirPrison, listeRue[24], listeRue[25], listeRue[26], caseChance,
               listeRue[27], listeRue[28], caseGare4, listeRue[29], listeRue[30], listeRue[31]]
    return plateau
# ----------------------------------------------------------------

# Start Game

# ----------------------------------------------------------------

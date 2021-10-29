from miniJeux import Morpion
from io import StringIO
from sys import stdout, __stdout__
from engine import *
from consoles import *
from menu import *


def lancerJeux(nbJoueur, monopole, possederXArgent, argentMax, NamePlayer):
    listeJoueur, listeRue, plateau, dictionnaireCouleurs = initParam(
        nbJoueur, NamePlayer)
    regles = Regles(monopole, possederXArgent, argentMax, dictionnaireCouleurs)
    deroulement(plateau, listeRue, listeJoueur, regles)


def deroulement(plateau, listeRueLibre, listeJoueur, regles, listeRueAcheter=[], victoire=False):
    joueurActif = listeJoueur[0]
    result = False
    while result == False:
        AffInfo(joueurActif, recuperationCase(
        joueurActif.position, plateau).nom,plateau, listeJoueur)
        tourJoueur(joueurActif, plateau, listeJoueur, regles)
        verifArgent(listeJoueur)
        result, joueurGagnant = verifVictoire(listeJoueur, regles, plateau)
        if result == True:
            if joueurGagnant == "personne":
                messageVictoirePersonne()
            else:
                messageVictoire(joueurGagnant.nom)
            break
        joueurActif = changementJoueur(joueurActif, listeJoueur)


def tourJoueur(joueur, plateau, listeJoueur, regles):
    compteurDouble = 0
    double = True
    while double == True and compteurDouble < 3:
        if isinstance(recuperationCase(joueur.position, plateau), Prison) and joueur.prison == True:
            _, double,_ ,_ = lancerDes()
            prisonEffet(joueur, double)
        if joueur.prison == False:
            double = playerPlay(joueur, plateau, listeJoueur, regles)
            if double == True:
                compteurDouble += 1

    if compteurDouble == 3:
        vaEnPrison(joueur)


def playerPlay(joueur, plateau, listeJoueur, regles):
    result, double , de1, de2 = lancerDes()
    joueur.deplacement(result, regles.reverse)
    messageLancerDes(result,de1, de2,plateau,joueur, listeJoueur)
    messageAvancement(joueur.position, recuperationCase(
        joueur.position, plateau).nom)
    caseEffet(recuperationCase(joueur.position, plateau),
              joueur, listeJoueur, regles, plateau)
    return double

def verifArgent(listeJoueur) :
    for joueur in listeJoueur :
        if joueur.argent <= 0 :
            if len(joueur.proprieter) == 0 :
                perdu(joueur.nom)
                supprimerJoueur(listeJoueur,joueur)
            argentVente = 0
            for proprieter in joueur.proprieter :
                argentVente += proprieter.prix/2
            if argentVente + joueur.argent < 0 :
                perdu(joueur.nom)
                supprimerJoueur(listeJoueur,joueur)
            venteProprietesInfo(joueur)

            num = 0
            vente = False
            while vente == True :
                while num == 0 :
                    try :
                        num = venteProprietesQuestion()
                        if num == "abandon":
                            perdu(joueur.nom)
                            supprimerJoueur(listeJoueur,joueur)
                        num = int(num)
                        if num > len(joueur.listeProprietes) or num <= 0 :
                            nombreInvalide()
                        else :
                            break
                    except :
                        nombreInvalide()
                venteProprietes(joueur,num-1)
                if joueur.argent > 0 :
                    reponse = continuezVente()
                    if reponse != "oui" :
                        vente = False
                        break
                    else :
                        continue
        
            

def proprieterEffet(case, joueur, listeJoueur):
    if case.proprietere == None:
        reponse = achatProposition(case.prix, joueur.argent)
        if reponse == "oui":
            if joueur.argent >= case.prix:
                achat(joueur, case)
                achatMessage()
            else:
                manqueArgent()
    else:
        if case in joueur.proprieter:
            reponse = achatMaison(
                case.prix/2, joueur.argent, case.loyer, case.nbMaison)
            if reponse == "oui":
                if joueur.argent >= case.prix/2:
                    achatMessage()
                    case.nbMaison += 1
                    case.augmentationLoyer()
                else:
                    manqueArgent()
        else:
            if joueur.argent - case.loyer >= 0:
                joueur.argent -= case.loyer
                case.proprietere.argent += case.loyer
                somme = case.loyer
            else:
                somme = joueur.argent
                case.proprietere.argent += joueur.argent
                joueur.argent = 0
            messageProprieteJoueur(case.proprietere, somme )


def gareEffect(case, joueur, listeJoueur):
    if case.proprietere == None:
        reponse = achatProposition(case.prix, joueur.argent)
        if reponse == "oui":
            if joueur.argent >= case.prix:
                achat(joueur, case)
                achatMessage()
        else:
            manqueArgent()
    else:
        if case in joueur.proprieter:
            reponse = achatMaison(
                case.prix/2, joueur.argent, case.loyer, case.nbMaison)
            if reponse == "oui":
                if joueur.argent >= case.prix/2:
                    case.nbMaison += 1
                    case.augmentationLoyer
                    achatMessage()
                else:
                    manqueArgent()
        else:
            if joueur.argent - case.loyer >= 0:
                joueur.argent -= case.loyer
                case.proprietere.argent += case.loyer
            else:
                case.proprietere.argent += joueur.argent
                joueur.argent = 0


def prisonEffet(joueur, double):
    messagePrison(joueur.nom, joueur.prisonTour)
    if double:
        joueur.prisonTour = 0
        joueur.prison = False
        messagePrisonWin()
    else:
        messagePrisonLose()
        joueur.prisonTour += 1
    if joueur.prisonTour == 3:
        joueur.prison = False
        joueur.prisonTour = 0


def caseEffet(case, joueur, listeJoueur, regles, plateau):
    if isinstance(case, Propriete):
        proprieterEffet(case, joueur, listeJoueur)
    elif isinstance(case, Chance):
        chanceEffet(case, joueur, listeJoueur, regles, plateau)
    elif isinstance(case, Gare):
        gareEffect(case, joueur, listeJoueur)
    elif isinstance(case, Attente):
        pass
    elif isinstance(case, DirPrison):
        vaEnPrison(joueur)
    elif isinstance(case, CaseMiniJeux):
        miniJeux(listeJoueur, joueur, case)


def chanceEffet(case, joueur, listeJoueur, regles, plateau):
    message, stat = case.tirage(joueur, listeJoueur, regles)
    messageCarteChance(message)
    if stat == 1:
        playerPlay(joueur, plateau, listeJoueur, regles)


def miniJeux(listeJoueur, joueur, case):
    messageMiniJeux()
    randJoueur = randint(0, len(listeJoueur)-1)
    while listeJoueur[randJoueur] == joueur:
        randJoueur = randint(0, len(listeJoueur)-1)
    messageApresRandomMiniJeux(listeJoueur[randJoueur].nom)
    nomGagnant = case.choixJeux(joueur.nom, listeJoueur[randJoueur].nom)
    if nomGagnant == joueur.nom:
        joueur.argent += 500
        listeJoueur[randJoueur].argent -= 500
            

if __name__ == '__main__':
    start_menu(lancerJeux)

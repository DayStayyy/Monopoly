from random import randint, random


class Chance():
    def __init__(self):
        self.nom = "Chance"
        self.listeNomCartes = ["Demi-Tour", "Prison", "Va à la case départ", "Avance", "Recule", "Va là-bas", "Va ici",
                               "Vole à la carte", "Vole à la tire", "Avion ecoplus", "Robin des bois avare", "Homme charitable", "Tricheur", "Loto", "Bug", "Quitte ou double", "Impots"]
        self.paquet = [self.changeDirection, self.depart, self.prison, self.plusTroisCase, self.moinsTroisCase, self.rueConfiance, self.rueDefense,self.volPropriete, self.volArgent, self.donation, self.rejoue, self.concours, self.faveurBanque, self.impots]

    def tirage(self, joueur, listeJoueur, regles):
        carte_tiree = randint(0, len(self.paquet)-1)
        message,stat = self.paquet[carte_tiree](joueur, listeJoueur, regles)
        return message,stat

    def changeDirection(self, joueur, listeJoueur, regles):
        regles.reversePlateau()
        return "Demi-Tour \n Elle inverse le sens du jeu",0

    def prison(self, joueur, listeJoueur, regles):
        joueur.prison = True
        joueur.position = 12
        return "Prison \n Le joueur se retrouve en prison",0

    def depart(self, joueur, listeJoueur, regles):
        joueur.position = 1
        joueur.finiTour()
        return "Case départ \n Téléporte le joueur à la case départ",0

    def plusTroisCase(self, joueur, listeJoueur, regles):
        joueur.deplacement( 3, regles.reverse)
        return "Avance \n Le joueur avance de 3 cases\nil se trouve désormais sur la case {}".format(joueur.position),0

    def moinsTroisCase(self, joueur, listeJoueur, regles):
        joueur.deplacement(-3, regles.reverse)
        return "Recule \n Le joueur recule de 3 cases\nil se trouve désormais sur la case {}".format(joueur.position),0

    def rueConfiance(self, joueur, listeJoueur, regles):
        if regles.reverse:
            if joueur.position < 15:
                joueur.argent += 400
        else:
            if joueur.position > 15:
                joueur.argent += 400
        joueur.position = 15
        return "Va-ici \n Le joueur est téléporté à Rue de la Joie. S'il passe par la case départ, il reçoit 400 euros\nil se trouve désormais sur la case {}".format(joueur.position),0

    def rueDefense(self, joueur, listeJoueur, regles):
        if regles.reverse:
            if joueur.position < 32:
                joueur.argent += 400
        else:
            if joueur.position > 32:
                joueur.argent += 400
        joueur.position = 32
        return "Va là-bas \n Le joueur est téléporté à Rue de la Défense. S'il passe par la case départ, il reçoit 400 euros\nil se trouve désormais sur la case {}".format(joueur.position),0

    def volPropriete(self, joueur, listeJoueur, regles):
        verifBool = False
        for verif in listeJoueur:
            if len(verif.proprieter) != 0 and verif != joueur:
                verifBool = True
        if verifBool:
            cible = listeJoueur[randint(0, len(listeJoueur)-1)]
            while cible == joueur or len(cible.proprieter) == 0:
                cible = listeJoueur[randint(0, len(listeJoueur)-1)]
            propriVol = cible.proprieter[randint(0, len(cible.proprieter)-1)]
            cible.proprieter.remove(propriVol)
            propriVol.proprietere = joueur
            joueur.proprieter.append(propriVol)
            return "Vol à la carte \n Vous prenez une propriété aléatoire d'un joueur choisi aléatoirement",0
        else:
            return "Vol à la carte \n Vous prenez une propriété aléatoire d'un joueur choisi aléatoirement \n les autres joueurs n'ont pas de propriétés, vous ne pouvez rien voler",0

    def volArgent(self, joueur, listeJoueur, regles):
        argentJ = 0
        cibleValide = joueur
        for cible in listeJoueur:
            if argentJ < cible.argent and cible != joueur:
                cibleValide = cible
                argentJ = cible.argent
        if cibleValide != joueur:
            cibleValide.argent -= 200
            joueur.argent += 200
            return "Robin des bois avare \n Vous prenez 200 euros au joueur le plus riche",0
        return "Robin des bois avare \n Vous prenez 200 euros au joueur le plus riche \n Vous êtes le joueur le plus riche, rien ne se passe",0

    def donation(self, joueur, listeJoueur, regles):
        argentJ = joueur.argent
        cibleValide = joueur
        for cible in listeJoueur:
            if argentJ > cible.argent and cible != joueur:
                cibleValide = cible
                argentJ = cible.argent
        if cibleValide != joueur:
            cibleValide.argent += 50
            joueur.argent -= 50
            return "Homme charitable \n Vous faites don de 50 euros au joueur le plus pauvre",0
        return "Homme charitable \n Vous faites don de 50 euros au joueur le plus pauvre \n Vous êtes le joueur le plus pauvre, rien ne se passe",0

    def rejoue(self, joueur, listeJoueur, regles):
        return "Avion ecoplus \n Le joueur relance les dés, cependant si il fait un double le double ne sera pas pris en compte",1

    def concours(self, joueur, listeJoueur, regles):
        joueur.argent += 100
        return "Concours \n Le joueur gagne 100 euros",0

    def faveurBanque(self, joueur, listeJoueur, regles):
        joueur.argent += 300
        return "Loto \n Le joueur gagne 300 euros",0

    def impots(self, joueur, listeJoueur, regles):
        count = 0
        for propriete in joueur.proprieter:
            count += propriete.nbMaison
        joueur.argent -= count*50
        return "Impôts \n Vous payer 50 euros par maison que vous possédez",0

# tests
# self.paquet = [self.changeDirection, self.depart, self.prison, self.plusTroisCase, self.moinsTroisCase, self.rueConfiance, self.rueDefense,
#                        self.volPropriete, self.volArgent, self.donation, self.rejoue, self.concours, self.faveurBanque, self.impots]
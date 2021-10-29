from random import randint


class CaseMiniJeux():

    def __init__(self,*args):
        self.nom = "Mini Jeux"
        self.listeJeux = []
        for i in args :
            self.listeJeux.append(i)
        print(i)

    def choixJeux(self, nom1, nom2):
        rand = randint(0, len(self.listeJeux)-1)
        gagnant = self.listeJeux[rand](nom1, nom2)
        return gagnant

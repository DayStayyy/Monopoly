class Propriete():
    def __init__(self, nom, couleur, prix, loyer_base):
        self.nom = nom
        self.couleur = couleur
        self.prix = prix
        self.loyer_base = loyer_base
        self.loyer = loyer_base
        self.nbMaison = 0
        self.proprietere = None

    def augmentationLoyer(self):
        self.loyer = self.loyer_base * self.nbMaison * 2

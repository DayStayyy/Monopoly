class Joueur():
    def __init__(self, nom, num, couleur):
        self.nom = nom
        self.argent = 3000
        self.proprieter = []
        self.position = 1
        self.num = num
        self.prison = False
        self.prisonTour = 0
        self.couleur = couleur

    def achat(self, case):
        self.argent -= case.prix
        self.proprieter.append(case)
        case.proprietere = self

    def deplacement(self, deplacement, reverse):
        if reverse:
            if self.position - deplacement > 1:
                self.position -= deplacement
            else:
                self.position = 44 - deplacement
                self.finiTour()
        else:
            if self.position + deplacement < 45:
                self.position += deplacement
            else:
                self.position = self.position + deplacement - 44
                self.finiTour()
    
    def finiTour(self):
        self.argent += 400
class Regles():
    def __init__(self, monopole, possederXArgent, argentMax,dictionnaireCouleurs):
        self.reverse = False
        self.monopole = monopole
        self.argentMax = argentMax
        self.possederXArgent = possederXArgent
        self.dictionnaireCouleurs = dictionnaireCouleurs

    def reversePlateau(self):
        if self.reverse == False:
            self.reverse = True
        else:
            self.reverse = False

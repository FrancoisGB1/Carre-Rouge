class Carre():
    def init(self, parent, largeur, hauteur):
        self.parent = parent
        self.largeur = 40
        self.hauteur = 40
        self.pos_x = 255
        self.pos_y = 255

class Rectangle():
    def init(self, parent, largeur, hauteur, pos_x, pos_y):
        self.parent = parent
        self.largeur = largeur
        self.hauteur = hauteur
        self.pos_x = pos_x
        self.pos_y = pos_y

    def deplacer():
        pass


class Modele():
    def init(self, parent, largeur, hauteur):
        self.parent = parent
        self.largeur = largeur
        self.hauter = hauteur
        self.rectangles = []
        self.joueur = []
        self.scores = {} # key: name, value: score

    def initialiser_partie(self):
        self.rectangles = []
        self.joueur = []
        self.creer_rectangles()
        self.creer_joueur()

    def creer_joueur(self):
        joueur = Carre(self)
        self.joueur.append(joueur)

    def creer_rectangles(self):
        recGauche = Rectangle(self, 60, 60, 100, 100)
        recSupDroit = Rectangle(self, 60, 50, 300, 85)
        recInfGauche = Rectangle(self, 30, 60, 85, 350)
        recInfDroit = Rectangle(self, 100, 20, 355, 340)
        self.rectangles.append(recGauche, recSupDroit, recInfGauche, recInfDroit)

    
    
    

    
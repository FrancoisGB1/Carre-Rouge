class Carre():
    def __init__(self, parent, largeur, hauteur, pos_x, pos_y):
        self.parent = parent
        self.largeur = largeur
        self.hauteur = hauteur
        self.pos_x = pos_x
        self.pos_y = pos_y


class Rectangle():
    def __init__(self, parent, largeur, hauteur, pos_x, pos_y):
        self.parent = parent
        self.largeur = largeur
        self.hauteur = hauteur
        self.pos_x = pos_x
        self.pos_y = pos_y
        

class Modele():
    def __init__(self, parent, largeur, hauteur):
        self.parent = parent
        self.largeur = largeur
        self.hauter = hauteur
        self.rectangles = []
        self.scores = {} # key: name, value: score

    def demarrer_partie(self):
        self.rectangles = []
    
    def creer_rectangles(self):
        recGauche = Rectangle(self, 60, 60, 100, 100)
        recSupDroit = Rectangle(self, 60, 50, 300, 85)
        recInfGauche = Rectangle(self, 30, 60, 85, 350)
        recInfDroit = Rectangle(self, 100, 20, 355, 340)
        self.rectangles.append(recGauche, recSupDroit, recInfGauche, recInfDroit)
    
    

    
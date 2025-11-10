class Carre():
    def __init__(self, parent):
        self.parent = parent
        self.largeur = 40
        self.hauteur = 40
        self.pos_x = 255
        self.pos_y = 255
        self.cote_haut = self.pos_y - self.hauteur 
        self.cote_bas = self.pos_y + self.hauteur 
        self.cote_gauche = self.pos_x - self.largeur
        self.cote_droite = self.pos_x + self.largeur

class Rectangle():
    def __init__(self, parent, largeur, hauteur, pos_x, pos_y, or_x, or_y):
        self.parent = parent
        self.largeur = largeur
        self.hauteur = hauteur
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vitesse = 4
        self.orientation_x = or_x
        self.orientation_y = or_y
        self.orientations = {
            'bas-droit' : (1,1),
            'bas-gauche' : (-1,1),
            'haut-droit' : (1,-1),
            'haut-gauche' : (-1,-1),
        }

class Modele():
    def __init__(self, parent, largeur, hauteur):
        self.parent = parent
        self.largeur = largeur
        self.hauteur = hauteur
        self.rectangles = []
        self.joueur = None
        self.scores = {} # key: name, value: score
        self.enJeu = False

    def initialiser_partie(self):
        self.rectangles = []
        self.joueur = None
        self.creer_rectangles()
        self.creer_joueur()

    def creer_joueur(self):
        self.joueur = Carre(self)

    def creer_rectangles(self):
        recGauche = Rectangle(self, 60, 60, 100, 100, 1, 1)
        recSupDroit = Rectangle(self, 60, 50, 300, 85, -1, 1)
        recInfGauche = Rectangle(self, 30, 60, 85, 350, 1, 1)
        recInfDroit = Rectangle(self, 100, 20, 355, 340, -1, -1)
        self.rectangles.append(recGauche)
        self.rectangles.append(recSupDroit)
        self.rectangles.append(recInfGauche)
        self.rectangles.append(recInfDroit)

    def bouger_rectangle(self):
        for rec in self.rectangles:
            rec.pos_x += rec.orientation_x * rec.vitesse
            rec.pos_y += rec.orientation_y * rec.vitesse
    def bouger_carre(self, souris_x_root, souris_y_root):
        difference_x = self.pos_x - souris_x_root
        difference_y = self.pos_y - souris_y_root
        self.pos_x += difference_x + souris_x_root
        self.pos_y += difference_y + souris_y_root
    def collision(self):
        pass
        
    
    def demarrer_partie(self, evt):
        pass

marge = 50

class Carre():
    def __init__(self, parent):
        self.parent = parent
        self.largeur = 40
        self.hauteur = 40
        self.pos_x = 225
        self.pos_y = 225

class Rectangle():
    def __init__(self, parent, largeur, hauteur, pos_x, pos_y, or_x, or_y):
        self.parent = parent
        self.largeur = largeur
        self.hauteur = hauteur
        self.pos_x = pos_x
        self.pos_y = pos_y
        
        self.orientation_x = or_x
        self.orientation_y = or_y
        self.orientations = {
            'bas-droit' : (1,1),
            'bas-gauche' : (-1,1),
            'haut-droit' : (1,-1),
            'haut-gauche' : (-1,-1),
        }
        
    def deplacer(self):
        x,y = self.orientations['bas-droit']
        self.pos_x = self.pos_x + (self.vitesse * x)
        self.pos_y = self.pos_y + (self.vitesse * y)


class Modele():
    def __init__(self, parent, largeur, hauteur):
        self.parent = parent
        self.largeur = largeur
        self.hauteur = hauteur
        self.rectangles = []
        self.joueur = None
        self.scores = {} # key: name, value: score
        self.enJeu = False
        self.vitesse = 2
        self.cursor_x = 0
        self.cursor_y = 0
        self.frames = 0
        self.score= 0


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
        recInfGauche = Rectangle(self, 30, 60, 85, 350, 1,1)
        recInfDroit = Rectangle(self, 100, 20, 355, 340, -1, 1)
        self.rectangles.append(recGauche)
        self.rectangles.append(recSupDroit)
        self.rectangles.append(recInfGauche)
        self.rectangles.append(recInfDroit)

    def bouger_rectangle(self):
        for rec in self.rectangles:
            rec.pos_x += rec.orientation_x * self.vitesse
            rec.pos_y += rec.orientation_y * self.vitesse

    def bouger_carre(self):
        self.joueur.pos_x = self.cursor_x
        self.joueur.pos_y = self.cursor_y

    def collision(self):
        for rec in self.rectangles:
            if rec.pos_x + rec.largeur / 2 >= 450 or rec.pos_x - rec.largeur / 2 <= 0:
                rec.orientation_x *= -1
            if rec.pos_y + rec.hauteur / 2 >= 450 or rec.pos_y - rec.hauteur / 2 <= 0:
                rec.orientation_y *= -1
        self.verifier_collisions()

#----------------------------------------------------------------------- DERNIER PUSH Francois ---------------------------------------------------------------

    def aire_blanche(self):
        left = 50
        top = 50
        right = self.largeur - 50
        bottom = self.hauteur - 50
        return left, top, right, bottom

    def bords_rect(self, x_centre, y_centre, largeur, hauteur):
        # l = left, t = top, r = right, b = bottom
        l = x_centre - largeur/2
        t = y_centre - hauteur/2
        r = x_centre + largeur/2
        b = y_centre + hauteur/2
        return l, t, r, b

    def trouver_overlap(self, l1, t1, r1, b1, l2, t2, r2, b2):
            #Rectangle 1 : l1, t1, r1, b1   PS : Le carré rouge est aussi un rectangle
            #Rectangle 2 : l2, t2, r2, b2
        return not (r1 <= l2 or l1 >= r2 or b1 <= t2 or t1 >= b2)

    def joueur_touche_bordure(self):
        left, top, right, bottom = self.aire_blanche()
        # meme principe jl = joueur left, jt = joueur top, jr = joueur right, jb = joueur bottom
        jl, jt, jr, jb = self.bords_rect(self.joueur.pos_x, self.joueur.pos_y, 
                                        self.joueur.largeur, self.joueur.hauteur)
        return (jl <= left) or (jt <= top) or (jr >= right) or (jb >= bottom)

    def joueur_touche_obstacle(self):
        jl, jt, jr, jb = self.bords_rect(self.joueur.pos_x, self.joueur.pos_y,
                                        self.joueur.largeur, self.joueur.hauteur)
        for rec in self.rectangles:
            rl, rt, rr, rb = self.bords_rect(rec.pos_x, rec.pos_y, rec.largeur, rec.hauteur)
            if self.trouver_overlap(jl, jt, jr, jb, rl, rt, rr, rb):
                print("Ran into obstacle")
                return True
        return False

    def verifier_collisions(self):
        if self.enJeu == True:
            if self.joueur_touche_obstacle() or self.joueur_touche_bordure():
                self.enJeu = False
                return True
        return False
    


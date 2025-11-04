import tkinter as tk

class Vue():
    def __init__(self, parent, largeur, hauteur):
        self.parent = parent
        self.largeur = largeur
        self.hauteur = hauteur
        self.root = tk.Tk()
        self.creer_interface()

    def creer_interface(self):
        self.cadre_principale = tk.Frame(self.root) 
        self.cadre_principale.pack()

        self.canvas = tk.Canvas(self.cadre_principale, width=self.largeur, height=self.hauteur)
        self.canvas.pack()
        self.canvas.create_rectangle(0,0, self.largeur, self.hauteur, fill="black")

        self.canvas.create_rectangle(50,50, self.largeur - 50, self.hauteur -50, fill="white")

    def dessiner_entité(self, rectangle, carree):
        for rect in rectangle:
            self.canvas.create_rectangle(rect.pos_x - rect.largeur / 2, rect.pos_y - rect.hauteur,
                                         rect.pos_x + rect.largeur / 2, rect.pos_y + rect.hauteur, fill="blue",
                                         tags=("rectangle"))
        self.canvas.create_rectangle(carree.pos_x - carree.largeur / 2, carree.pos_y - carree.hauteur,
                                         carree.pos_x + carree.largeur / 2, carree.pos_y + carree.hauteur, fill="red",
                                         tags=("carre"))
        self.canvas.tag_bind("carre", "<onclick>", self.demarrer_partie)

    def demarrer_partie(self):
        pass






#initialiser
#mainloop






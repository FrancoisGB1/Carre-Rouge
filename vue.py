import tkinter as tk

class Vue():
    def __init__(self, parent, largeur, hauteur):
        self.parent = parent
        self.largeur = largeur
        self.hauteur = hauteur
        self.root = tk.Tk()
        self.creer_interface()
        self.pressed = False
        self.score_text = self.canvas.create_text(100, 430, text="Score : 0", font=("Arial", 16), fill="white", anchor="center")


    def creer_interface(self):
        self.cadre_principale = tk.Frame(self.root) 
        self.cadre_principale.pack()

        self.canvas = tk.Canvas(self.cadre_principale, width=self.largeur, height=self.hauteur)
        self.canvas.pack()
        self.canvas.create_rectangle(0,0, self.largeur, self.hauteur, fill="black")

        self.canvas.create_rectangle(50,50, self.largeur - 50, self.hauteur -50, fill="white")

    def dessiner_entité(self, rectangle, carree):
        for rect in rectangle:
            self.canvas.create_rectangle(rect.pos_x - rect.largeur / 2, rect.pos_y - rect.hauteur / 2,
                                         rect.pos_x + rect.largeur / 2, rect.pos_y + rect.hauteur / 2, fill="blue",
                                         tags=("rectangle"))
        self.canvas.create_rectangle(carree.pos_x - carree.largeur / 2, carree.pos_y - carree.hauteur / 2,
                                         carree.pos_x + carree.largeur / 2, carree.pos_y + carree.hauteur / 2, fill="red",
                                         tags=("carre"))
        self.canvas.tag_bind("carre", "<Button-1>", self.demarrer_partie)
        self.canvas.tag_bind("carre", "<ButtonRelease-1>", self.is_released)
        self.canvas.bind("<ButtonRelease-1>", self.is_released)
    def demarrer_partie(self, evt):
        self.pressed = True
        self.parent.demarrer_partie(evt)
        

    def is_released(self, evt):
        self.pressed = False


    def mise_jour(self, rectangle, carree):
        self.canvas.delete("rectangle")
        self.canvas.delete("carre")
        self.dessiner_entité(rectangle, carree)
    
    def update_score(self, score):
        self.canvas.itemconfig(self.score_text, text=f"Score : {score:.2f}")



#initialiser
#mainloop






import modele as mod
import vue

class Controleur():
    def __init__(self):
        self.modele = mod.Modele(self, 450, 450)
        self.vue = vue.Vue(self, 450, 450)
        self.modele.initialiser_partie()
        self.vue.root.after(50,self.initialiser_partie)
        self.vue.root.mainloop()

    def initialiser_partie(self):
        self.vue.dessiner_entité(self.modele.rectangles, self.modele.joueur)

    def demarrer_partie(self, evt):
        self.modele.enJeu = True
        self.boucle(evt)
        
    def boucle(self, evt):
        self.modele.bouger_carre(evt.x_root, evt.y_root)
        self.modele.bouger_rectangle()
        self.modele.collision()
        self.vue.mise_jour(self.modele.rectangles, self.modele.joueur)
        self.vue.root.after(50, self.boucle)
import modele as mod
import vue

class Controleur():
    def __init__(self):
        self.modele = mod.Modele(self, 450, 450)
        self.vue = vue.Vue(self, 450, 450)
        self.modele.initialiser_partie()
        self.vue.root.mainloop()

    def initialiser_partie(self):
        self.modele.initialiser_partie()
        self.vue.dessiner_entité(self.modele.rectangles, self.modele.joueur)

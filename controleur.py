import modele as mod
import vue

class Controleur():
    def __init__(self):
        self.modele = mod.Modele(self, largeur=450, hauteur=450)
        self.vue = vue.Vue(self, largeur=450, hauter=450)
        self.modele.initialiser_partie()
        self.vue.root.mainloop()

    def initialiser_partie(self):
        self.modele.initialiser_partie()
        self.vue.dessiner_entité()

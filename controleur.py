import modele as mod
import vue

class Controleur():
    def __init__(self):
        self.modele = Modele(self, largeur=450, hauteur=450)
        self.vue = Vue(self, largeur=450, hauter=450)
        self.vue.root.mainloop()

    def demarrer_partie(self):
        self.modele.demarrer_partie()

if __name__ == "__main__":
    c = Controleur()
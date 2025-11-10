import modele as mod
import vue

class Controleur():
    def __init__(self):
        self.modele = mod.Modele(self, 450, 450)
        self.vue = vue.Vue(self, 450, 450)
        self.modele.initialiser_partie()
        self.vue.root.after(50,self.initialiser_partie)
        self.vue.root.mainloop()
        self.temp = 0


    def initialiser_partie(self):
        self.vue.dessiner_entité(self.modele.rectangles, self.modele.joueur)

    def demarrer_partie(self, evt):
        if self.modele.enJeu == False:
            self.modele.enJeu = True
            self.boucle()
            self.aug_vitesse()
            self.vue.root.bind('<Motion>', self.motion)
        
    def boucle(self):
        self.modele.bouger_carre()
        self.modele.bouger_rectangle()
        self.modele.collision()
        self.vue.mise_jour(self.modele.rectangles, self.modele.joueur)
        self.vue.root.after(30, self.boucle)
        print(self.vue.pressed)

    def aug_vitesse(self):
        cnt = 0
        cnt += 1
        print(cnt)
        self.modele.vitesse += 1
        self.vue.root.after(5000,self.aug_vitesse)

    def motion(self, event):
        if self.vue.pressed:
            self.modele.cursor_x, self.modele.cursor_y = event.x, event.y


    
    
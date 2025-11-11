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

    def demarrer_partie(self, event):
        self.initialiser_position_carre(event)
        if self.modele.enJeu == False:
            self.modele.enJeu = True
            self.boucle()
            self.aug_vitesse()
            self.vue.root.bind('<Motion>', self.motion)
            
        
    def boucle(self):

        if not self.modele.enJeu:
            #Update le final frame
            self.modele.bouger_carre()
            self.modele.bouger_rectangle()
            #Arreter le motion event listener sinon ca continue 
            self.terminer_partie()
            #terminer la boucle
    
            return
        
        self.modele.frames += 1
        self.modele.score = self.modele.frames * 0.015
        self.modele.bouger_carre()
        self.modele.bouger_rectangle()
        self.modele.collision()
        self.vue.mise_jour(self.modele.rectangles, self.modele.joueur)
        self.vue.update_score(self.modele.score)
        self.vue.root.after(15, self.boucle)
        
        
 

    def aug_vitesse(self):
        self.modele.vitesse += 0.5
        self.vue.root.after(5000,self.aug_vitesse)

    def motion(self, event):
        if self.vue.pressed:
            self.modele.cursor_x, self.modele.cursor_y = event.x, event.y
    # Bug si on initialise pas la position avant de demarrer (Collisions fantomes)
    def initialiser_position_carre(self, event):
        self.modele.cursor_x = event.x
        self.modele.cursor_y = event.y
        self.modele.joueur.pos_x = event.x
        self.modele.joueur.pos_y = event.y
        
    def terminer_partie(self):
        self.vue.root.unbind('<Motion>')
        self.vue.canvas.tag_unbind("carre", "<Button-1>")
        self.vue.canvas.tag_unbind("carre", "<ButtonRelease-1>")
    
    def restart_game(self):
        self.modele = mod.Modele(self, 450, 450)
        self.modele.initialiser_partie()
        self.vue.mise_jour(self.modele.rectangles, self.modele.joueur)
        self.initialiser_partie()
        self.modele.score = 0
        self.vue.update_score(self.modele.score)
        pass
    
    
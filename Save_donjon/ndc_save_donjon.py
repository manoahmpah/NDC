# Pyxel Studio

# Bienvenue chèr(e) Joueur(euse) dans SaveDungeons , c'est un jeu RPG qui s'inspire de l'univers des donjons où le but est de
# s'échapper de cette fôret mystique et dangereuse sans se faire toucher par les créatures maléfiques qui rôdent dans cette fôret
# et dans l'épeuvre du donjon que vous aller découvrir.

# COMMENT Y JOUER : Les flèches directionnelles pour se déplacer ,la touche LShift pour courir plus vite et  la touche W pour ouvrir la porte qui vous menera à
# la liberté !!

import pyxel

class Joueur:
    def __init__(self):
        pyxel.init(128, 128, title="NDC 2023")
        self.x = 1
        self.y = 10
        self.vie = 3
        self.energie = 3
        self.faim = 3

    
        self.compteur = 0
        self.compteur1 = 0
        self.acceuil = False
        self.end = False
        pyxel.load("5.pyxres")
        pyxel.run(self.update, self.draw)
        
    def update(self):
        self.deplacement()
        self.vide()
        
    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0,0,1,0,0,128,128)
        
        # La page d'acceuil
        if self.acceuil == False:
            
            if self.compteur==1:
                self.acceuil = True
            else:
                if pyxel.frame_count%5 == 0:
                    pyxel.text(20, 60, ">> PRESS E TO PLAY <<", 0)
                    if pyxel.btn(pyxel.KEY_E):
                        self.compteur += 1
                else:
                    pyxel.text(20, 60, ">> PRESS E TO PLAY <<", 6)
        else:
            # ouverture du jeu
            pyxel.bltm(0,0,0,0,0,128,128)

            pyxel.blt(0, 1, 0, 141,12, 8, 7, 12)
            pyxel.blt(9, 1, 0, 141,12, 8, 7, 12)
            pyxel.blt(19, 1, 0, 141,12, 8, 7, 12)

            pyxel.blt(self.x, self.y, 0, 122,12, 6, 8, 5)

            #ennemis
            pyxel.blt(55, 16, 0, 141,65, 6, 8, 5)
            pyxel.blt(55, 65, 0, 141,65, 6, 8, 5)

       


        
        if self.x == 97 and self.y == 112:
            pyxel.text(10, 10, "PRESS W", 7)
            if pyxel.btn(pyxel.KEY_W):
                self.end = True
            if self.end == False:
                
                pass
                    
            else:
                pyxel.bltm(0,0,2,0,0,128,128)


        

# depalcement 
    def deplacement(self):
        if pyxel.btn(pyxel.KEY_RIGHT)  :
            if self.x > 119 or pyxel.pget(self.x+6,self.y)==4 or pyxel.pget(self.x+6,self.y)==1 or pyxel.pget(self.x+6,self.y)==12:
                self.x -=1
            self.x +=1
            if pyxel.btn(pyxel.KEY_LSHIFT):
                if self.x > 119 or pyxel.pget(self.x+6,self.y)==4 or pyxel.pget(self.x+6,self.y)==1 or pyxel.pget(self.x+6,self.y)==12:
                    self.x -=1
                self.x+=1

 
        if pyxel.btn(pyxel.KEY_LEFT):
            if self.x < 1 or pyxel.pget(self.x-1,self.y)==4 or pyxel.pget(self.x-1,self.y)==1 or pyxel.pget(self.x-1,self.y)==12:
                self.x +=1
            self.x -=1
            
            if pyxel.btn(pyxel.KEY_LSHIFT):
                if self.x < 1 or pyxel.pget(self.x-1,self.y)==4 or pyxel.pget(self.x-1,self.y)==1 or pyxel.pget(self.x-1,self.y)==12:
                    self.x +=1
                self.x -=1

        if pyxel.btn(pyxel.KEY_UP) :
            if self.y < 1 or pyxel.pget(self.x,self.y-1)==4 or pyxel.pget(self.x,self.y-1)==1 or pyxel.pget(self.x,self.y-1)==12:
                self.y +=1
            self.y -=1
            
            if pyxel.btn(pyxel.KEY_LSHIFT):
                if self.y < 1 or pyxel.pget(self.x,self.y-1)==4 or pyxel.pget(self.x,self.y-1)==1 or pyxel.pget(self.x,self.y-1)==12:
                    self.y +=1
                self.y-=1
                
        if pyxel.btn(pyxel.KEY_DOWN):
            if self.y > 119 or pyxel.pget(self.x,self.y+8)==4 or pyxel.pget(self.x,self.y+8)==1 or pyxel.pget(self.x,self.y+8)==12:
                self.y -=1
            self.y +=1
            
            if pyxel.btn(pyxel.KEY_LSHIFT):
                if self.y > 119 or pyxel.pget(self.x,self.y+8)==4 or pyxel.pget(self.x,self.y+8)==1 or pyxel.pget(self.x,self.y+8)==12:
                    self.y -=1
                self.y+=1
   
    def vide(self):
        if pyxel.pget(self.x,self.y-1) == 10:
            self.vie -= 1
            self.y += 3

        
    
    def ennemi(self):
        pass
            
        
            
            
Joueur()
import pygame
import sys
import time
import random
import math

LARGEUR = 1280
HAUTEUR = 840

pygame.display.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
fenetre.fill([0, 0, 0])


class Balle:
    def __init__(self, largeur_fenetre, hauteur_fenetre):
        self.rayon = 20
        self.x = random.randint(self.rayon, largeur_fenetre - self.rayon)
        self.y = random.randint(self.rayon, hauteur_fenetre - self.rayon)
        self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.dx = random.choice([-4, -3, -2, 2, 3, 4])
        self.dy = random.choice([-4, -3, -2, 2, 3, 4])

    def dessiner(self, fenetre):
        pygame.draw.circle(fenetre, self.couleur, (self.x, self.y), self.rayon)

    def bouger(self, largeur_fenetre, hauteur_fenetre):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
         # Rebondir sur les parois
        if self.x - self.rayon <= 0 or self.x + self.rayon >= largeur_fenetre:
            self.dx = -self.dx
        if self.y - self.rayon <= 0 or self.y + self.rayon >= hauteur_fenetre:
            self.dy = -self.dy

        # Rebondir entre les balles
        for autre_balle in Balle:
            if autre_balle != self:
                distance = ((self.x - autre_balle.x) ** 2 + (self.y - autre_balle.y) ** 2) ** 0.5
                if distance <= self.rayon + autre_balle.rayon:
                    # Échange des vitesses pour l'illusion du rebond
                    self.dx, autre_balle.dx = autre_balle.dx, self.dx
                    self.dy, autre_balle.dy = autre_balle.dy, self.dy

class SacDeBalles:
    def __init__(self, nb_balles, largeur_fenetre, hauteur_fenetre):
        self.balles = [Balle(largeur_fenetre, hauteur_fenetre) for _ in range(nb_balles)]

    def dessiner_et_bouger(self, fenetre):
        fenetre.fill([0, 0, 0])
        for balle in self.balles:
            balle.dessiner(fenetre)
            balle.bouger(LARGEUR, HAUTEUR)
        pygame.display.update()

balle = Balle(LARGEUR, HAUTEUR)
sb20=SacDeBalles(5,LARGEUR,HAUTEUR)
continuer = True
while continuer:
    fenetre.fill([0, 0, 0])

    sb20.dessiner_et_bouger(fenetre)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
    time.sleep(0.01)

pygame.display.quit()
sys.exit()

SacDeBalles(20,LARGEUR,HAUTEUR)

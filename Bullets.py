import pygame
from pygame.sprite import Sprite
bullet_img = pygame.image.load('spr_bullet_strip02.png')
class Bullets(Sprite):
    def __init__(self, guardian):
        super(Bullets, self).__init__()
        self.x = guardian.x - 3
        self.y = guardian.y - 175
        self.speed = 25
        self.rect = pygame.Rect(0,0,32,32)
        self.rect.centerx = self.x
        self.rect.centery = self.y
        self.bullets = []
        self.bullets.append(bullet_img)
        self.img = self.bullets[0]
    def update_me(self):
        self.y -= self.speed
        self.rect.x = self.x
        self.rect.y = self.y
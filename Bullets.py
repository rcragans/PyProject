import pygame
from pygame.sprite import Sprite
class Bullets(Sprite):
    def __init__(self, guardian):
        super(Bullets, self).__init__()
        self.x = guardian.x
        self.y = guardian.y
        self.speed = 5
        self.rect = pygame.Rect(0,0,32,32)
        self.rect.centerx = self.x
        self.rect.centery = self.y
        self.bullets = []
        self.bullets.append(pygame.image.load('spr_bullet_strip02.png'))
    def update_me(self):
        self.x += self.speed
        self.rect.x = self.x
        self.rect.y = self.y
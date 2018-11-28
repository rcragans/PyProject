import pygame
from random import randint
from math import hypot
from pygame.sprite import Sprite
class Monster(object):
    def __init__(self):
        self.x = randint(1,512)
        self.y = randint(1,480)
        self.speed = 1
        self.rect = pygame.Rect(0,0,32,32)
        self.rect.centerx = self.x
        self.rect.centery = self.y
    def move_me(self, guardian):
        dx = self.x - guardian.x
        dy = self.y - guardian.y
        dist = hypot(dx, dy)
        dx = dx / dist
        dy = dy / dist
        self.x -= dx * self.speed
        self.y -= dy * self.speed
        self.rect.x = self.x
        self.rect.y = self.y

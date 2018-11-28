import pygame
from pygame.sprite import Sprite
from random import randint
class Gems(Sprite):
    def __init__(self, image):
        super(Gems,self).__init__()
        self.x = randint(1, 512)
        self.y = randint(1,1024)
        self.rect = pygame.Rect(0,0,32,32)
        self.rect.left = self.x
        self.rect.top = self.y


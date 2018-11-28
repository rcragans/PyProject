from random import randint
import pygame
from pygame.sprite import Sprite
class Guardian(Sprite):
    def __init__(self):
        super(Guardian, self).__init__()
        self.x = 256
        self.y = 512
        self.speed = 20
        self.should_move_down = False
        self.should_move_left = False
        self.should_move_right = False
        self.should_move_up = False
        self.rect = pygame.Rect(0,0,60,60)
        self.rect.centerx = self.x
        self.rect.centery = self.y
        self.gem_count = 0
        self.kills = 0
    def shouldMove(self, direction, start = True):
        if direction == "right":
            self.should_move_right = start
        if direction == "left":
            self.should_move_left = start
        if direction == "up":
            self.should_move_up = start
        if direction == "down":
            self.should_move_down = start
    def draw_me(self,w,h):
        if self.should_move_right:
            if self.x <= (w - 75):
                self.x += self.speed
        elif self.should_move_left:
            if self.x >= (10):
                self.x -= self.speed
        if self.should_move_down:
            # if self.y <= (h - 60):
            self.y += self.speed
        elif self.should_move_up:
            # if self.y >= (60):
            self.y -= self.speed
        self.rect.left = self.x
        self.rect.top = self.y
    

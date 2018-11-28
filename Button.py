import pygame.font
import pygame
class Start_Button(object):
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.width = 100
        self.height = 50
        self.button_color = 0,200,150
        self.text_color = 255,255,255
        self.font = pygame.font.Font(None, 52)
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
    def setup_message(self):
        self.image_message = self.font.render("Play", True, self.text_color)
        self.image_message_rect = self.image_message.get_rect()
        self.image_message_rect.center = self.rect.center
    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.image_message, self.image_message_rect)
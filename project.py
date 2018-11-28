import pygame
pygame.init()
from pygame.sprite import Group
from pygame.sprite import groupcollide
from Guardian import Guardian
guardian = Guardian()
from Monster import Monster
monster = Monster()
monsters = Group()
from Bullets import Bullets
bullets = Group()
screen_size = (512,1024)
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Space Shooter')
guardian_image = pygame.image.load('ship3.png')
guardian_image = pygame.transform.scale(guardian_image, (60,60))
background = [[pygame.image.load('middle_background.png'), pygame.image.load('monster1.png')], [pygame.image.load('top_background.png'), pygame.image.load('monster2.png')],[pygame.image.load('bottom_background.png'), pygame.image.load('monster3.png')]] 
map_x = guardian.x
map_y = guardian.y
game_on = True
while game_on:
    guardian.draw_me(512, 1024)
    if (guardian.y > -1 and guardian.y < 1025):
        pygame_screen.blit((background[0][0]), (0,0))
        map_y = guardian.y
    if guardian.y > 1024:
        pygame_screen.blit((background[2][0]), (0,0))
        map_y = guardian.y -1024
    if guardian.y < 0:
        pygame_screen.blit((background[1][0]), (0,0))
        map_y = guardian.y +1024
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        elif event.type == pygame.KEYDOWN:
            if event.key == 275:
                guardian.shouldMove("right",True)
            elif event.key == 276:
                guardian.shouldMove("left",True)
            if event.key == 273:
                guardian.shouldMove("up",True)
            elif event.key == 274:
                guardian.shouldMove("down",True)
            elif event.key == 32:
                new_bullet = Bullets(guardian)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == 275:
                guardian.shouldMove("right",False)
            elif event.key == 276:
                guardian.shouldMove("left",False)
            if event.key == 273:
                guardian.shouldMove("up",False)
            elif event.key == 274:
                guardian.shouldMove("down",False)
        for bullet in bullets:
            bullet.update_me()
            pygame_screen.blit('spr_bullet_strip02.png',[bullet.x, bullet.y])
    pygame_screen.blit(guardian_image,[guardian.x, guardian.y])
    pygame.display.flip()
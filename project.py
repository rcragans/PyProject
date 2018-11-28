import pygame
pygame.init()
from pygame.sprite import Group
from pygame.sprite import groupcollide
from Guardian import Guardian
from Monster import Monster
monsters = Group()
from Bullets import Bullets
from Gems import Gems
bullets = Group()
gems = Group()
guardians = Group()
screen_size = (512,1024)
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Space Shooter')
guardian_image = pygame.image.load('ship3.png')
guardian_image = pygame.transform.scale(guardian_image, (60,60))
monster1_image = pygame.image.load('monster1.png')
monster1_image = pygame.transform.scale(monster1_image, (60,60))
monster2_image = pygame.image.load('monster2.png')
monster2_image = pygame.transform.scale(monster2_image, (60,60))
monster3_image = pygame.image.load('monster3.png')
monster3_image = pygame.transform.scale(monster3_image, (60,60))
gridmap = [
{"map" : "", "monster" : ""},
{"map" : pygame.image.load('top_background.png'), "monster" : (monster2_image)},
{"map" : "", "monster" : ""},
{"map" : "", "monster" : ""},
{"map" : pygame.image.load('middle_background.png'), "monster" : (monster1_image)},
{"map" : "", "monster" : ""},
{"map" : "", "monster" : ""},
{"map" : pygame.image.load('bottom_background.png'), "monster" : (monster3_image)},
{"map" : "", "monster" : ""},
{"map" : "", "monster" : ""}] 
guardian = Guardian()
guardians.add(guardian)
game_on = True
curr_map = 4
curr_mon = 4
tick = 0
gem_image = pygame.image.load('diamond5.png')
game_start = False
while game_on:
    tick += 1
    if tick % 90 == 0:
        monsters.add(Monster(gridmap[curr_mon]['monster']))
    if tick % 450 == 0:
        gems.add(Gems(gem_image))
    guardian.draw_me(512, 1024)
    if (guardian.y > -1 and guardian.y < 1025):
        pass
    if guardian.y > 1024:
        curr_map += 3
        guardian.y = 1
        curr_mon += 3
    if guardian.y < 0:
        curr_map -= 3
        guardian.y = 1000
        curr_mon -= 3
    pygame_screen.blit((gridmap[curr_map]['map']), (0,0)) 
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
        pygame_screen.blit(pygame.transform.rotate(bullet.img,90),[bullet.x, bullet.y])
    bullet_hit = groupcollide(bullets, monsters, True, True)
    if bullet_hit:
        guardian.kills += 1
        # monsters.add(Monster(gridmap[curr_mon]['monster']))
    get_gem = groupcollide(guardians, gems, False, True) 
    if get_gem:
        guardian.gem_count += 1 
    for monster in monsters:
        pygame_screen.blit(monster.image, [monster.x, monster.y])
        monster.move_me(guardian)
    for gem in gems:
        pygame_screen.blit(gem_image, [gem.rect.x, gem.rect.y])
        # if guardian.gem_count % 5 == 0:
        #     monster.speed += 1
    pygame_screen.blit(guardian_image,[guardian.x, guardian.y])
    pygame.display.flip()
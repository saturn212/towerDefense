import pygame as pg
import os
import sys

pg.init()
current_path = os.path.dirname(__file__)
os.chdir(current_path)
lvl_game = 1
WIDTH = 1280
HEIGHT = 800
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (28, 170, 200)
MP_BLUE = (0, 0, 255)
from load import *

f1 = pg.font.Font(None, 36)
clock = pg.time.Clock()
score = 30000
timer = 0

camera_group = pg.sprite.Group()


class Bush(pg.sprite.Sprite):
    def __init__(self, image, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


class Dir(pg.sprite.Sprite):
    def __init__(self, image, pos, dir):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.dir = dir


class Bush_Tower(pg.sprite.Sprite):
    def __init__(self, image, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


class Tower(pg.sprite.Sprite):
    def __init__(self, image, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


class Tower_panel(pg.sprite.Sprite):
    def __init__(self, image, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.buy = False
        self.timer_click = 0

    def update(self):
        if score >= 300:
            self.image = tower_on_image
        else:
            self.image = tower_of_image
        if score >= 300:
            if pg.mouse.get_pressed()[0]:
                pos_mouse = pg.mouse.get_pos()
                if self.rect.left < pos_mouse[0] < self.rect.right and self.rect.top < pos_mouse[1] < self.rect.bottom:
                    self.buy = not self.buy
                    print(575756)
        if self.buy:
            cursor = pg.mouse.get_pos()
            screen.blit(tower_on_image, (cursor[0] - 40, cursor[1]-40))


class Enemy(pg.sprite.Sprite):
    def __init__(self, image, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.dir = 'right'
        self.speedx = 2
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.dir == 'right':
            self.speedx = 2
            self.speedy = 0
            self.image = pg.transform.rotate(enemy_image, 0)

        elif self.dir == 'bottom':
            self.speedx = 0
            self.speedy = 2
            self.image = pg.transform.rotate(enemy_image, 270)
        elif self.dir == 'left':
            self.speedx = -2
            self.speedy = 0
            self.image = pg.transform.rotate(enemy_image, 180)
        elif self.dir == 'top':
            self.speedx = 0
            self.speedy = -2
            self.image = pg.transform.rotate(enemy_image, 90)
        if pg.sprite.spritecollide(self, dir_group, False):
            tile = pg.sprite.spritecollide(self, dir_group, False)[0]
            if abs(self.rect.centerx - tile.rect.centerx) <= 5 and abs(self.rect.centery - tile.rect.centery) <= 5:
                self.dir = tile.dir


def restart():
    global bush_group, bush_tower_group, dir_group, enemy_group, panel_group, tower_group, tower_panel_group, timer

    bush_group = pg.sprite.Group()
    bush_tower_group = pg.sprite.Group()
    dir_group = pg.sprite.Group()
    enemy_group = pg.sprite.Group()
    tower_group = pg.sprite.Group()
    tower_panel_group = pg.sprite.Group()
    svitok_group = pg.sprite.Group()
    fire_group = pg.sprite.Group()
    tower_panel = Tower_panel(tower_of_image, (5, 712))
    tower_panel_group.add(tower_panel)
    # player = Player(player_image, (330, 500))
    # player_group.add(player)


def drawMaps(nameFile):
    maps = []
    source = 'game_lvl/' + str(nameFile)
    with open(source, "r") as file:
        for i in range(0, 10):
            maps.append(file.readline().replace("\n", "").split(",")[0:-1])
    pos = [0, 0]
    for i in range(0, len(maps)):
        pos[1] = i * 80
        for j in range(0, len(maps[0])):
            pos[0] = 80 * j
            if maps[i][j] == "1":
                bush = Bush(bush_image, pos)
                bush_group.add(bush)

            elif maps[i][j] == "2":
                grass = Bush(grass_image, pos)
                bush_group.add(grass)

            elif maps[i][j] == "3":
                bush_tower = Bush_Tower(bush_tower_image, pos)
                bush_tower_group.add(bush_tower)

            elif maps[i][j] == "4":
                # water = Water(water_image, pos)
                # water_group.add(water)
                # camera_group.add(water)
                pass
            elif maps[i][j] == "5":
                top = Dir(top_image, pos, 'top')
                dir_group.add(top)

            elif maps[i][j] == "6":
                right = Dir(right_image, pos, 'right')
                dir_group.add(right)

            elif maps[i][j] == "7":
                bottom = Dir(bottom_image, pos, 'bottom')
                dir_group.add(bottom)

            # elif maps[i][j] == "8":
            #     enemy = Enemy(enemy_2_image, pos)
            #     enemy_group.add(enemy)
            #     camera_group.add(enemy)
            # elif maps[i][j] == "9":
            #     enemy = Enemy(enemy_3_image, pos)
            #     enemy_group.add(enemy)
            #     camera_group.add(enemy)
            # elif maps[i][j] == "10":
            #     enemy = Enemy(enemy_4_image, pos)
            #     enemy_group.add(enemy)
            #     camera_group.add(enemy)
            # elif maps[i][j] == "11":
            #     portal = Portal(portal_image, pos)
            #     portal_group.add(portal)
            #     camera_group.add(portal)


def game_lvl():
    screen.fill(BLUE)
    bush_group.draw(screen)
    bush_group.update()
    bush_tower_group.draw(screen)
    bush_tower_group.update()
    dir_group.draw(screen)
    dir_group.update()
    enemy_group.update()
    enemy_group.draw(screen)
    tower_group.update()
    tower_group.draw(screen)
    screen.blit(panel_image, (0, 700))
    tower_panel_group.update()
    tower_panel_group.draw(screen)

    # box_group.draw(screen)
    # box_group.update(0)
    # center_group.update(0)
    # center_group.draw(screen)
    # portal_group.update(0)
    # portal_group.draw(screen)
    # monetka_group.update(0)
    # monetka_group.draw(screen)
    # stopenemy_group.update(0)
    # enemy_group.update(0)
    # enemy_group.draw(screen)
    # hp_group.update(0)
    # hp_group.draw(screen)
    # mp_group.update(0)
    # mp_group.draw(screen)
    # npc_group.update(0)
    # npc_group.draw(screen)
    # svitok_group.update(0)
    # svitok_group.draw(screen)
    # fire_group.draw(screen)
    # fire_group.update(0)

    pg.display.update()


restart()
drawMaps('1.txt')

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    timer += 1
    if timer == 60:
        enemy = Enemy(enemy_image, (-20, 573))
        enemy_group.add(enemy)
        timer = 0

    game_lvl()
    clock.tick(FPS)

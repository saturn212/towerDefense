import pygame as pg
from script import load_image
bush_image = pg.image.load("image/tile map/bush_tile 1.png").convert_alpha()
grass_image = pg.image.load("image/tile map/grass_tile_1.png").convert_alpha()
bush_tower_image = pg.image.load("image/tile map/bush_tile_tower.png").convert_alpha()
top_image = pg.image.load("image/tile map/top.png").convert_alpha()
bottom_image = pg.image.load("image/tile map/bottom.png").convert_alpha()
right_image = pg.image.load("image/tile map/right.png").convert_alpha()
left_image = pg.image.load("image/tile map/left.png").convert_alpha()
enemy_image = pg.image.load("image/enemy/right.png").convert_alpha()
panel_image = pg.image.load("image/panel.jpg").convert_alpha()
tower_on_image = pg.image.load("image/tower 1/1_on.png").convert_alpha()
tower_of_image = pg.image.load("image/tower 1/1_of.png").convert_alpha()
upgrade = pg.image.load("image/upgrade.png").convert_alpha()
bulet1_image = pg.image.load("image/tower 1/bullet 1.png").convert_alpha()
bulet2_image = pg.image.load("image/tower 1_1/bullet 2.png").convert_alpha()

tower_1 = load_image("image/tower 1/tower")
tower_1_1 = load_image("image/tower 1_1/tower")
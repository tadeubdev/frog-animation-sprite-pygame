import pygame as pg
from pygame.locals import *
import sys
from frog import Frog

pg.init()

game_name = "Frog animation with sprites - Pygame"
screen_size = (720, 480)
background_color = (255, 255, 255)

screen = pg.display.set_mode(screen_size)
pg.display.set_caption(game_name)

frog = Frog(screen_size[0] // 2, screen_size[1] // 2)

clock = pg.time.Clock()
clock.tick(120)

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        if event.type == KEYDOWN:
            frog.act()

    frog.update()

    screen.fill(background_color)
    screen.blit(frog.image, frog.rect)
    pg.display.flip()
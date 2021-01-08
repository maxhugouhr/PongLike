import pygame as pg

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 750
pg.display.init()
gameDisplay1 = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pg.time.Clock()

crashed = False

while not crashed:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            crashed = True


    pg.display.update()
    clock.tick(60)


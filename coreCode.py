import pygame as pg
from battlefield import Battlefield


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 750
pg.display.init()
gameDisplay1 = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pg.time.Clock()

crashed = False

battlefield1 = Battlefield(SCREEN_WIDTH, SCREEN_HEIGHT)
battlefield1.addEdges()

while not crashed:
    gameDisplay1.fill((0,0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            crashed = True

    for surface in battlefield1.surfaces:
        surface.draw(gameDisplay1)
    battlefield1.ball.draw(gameDisplay1)

    for surface in battlefield1.surfaces:
        surface.checkHit(battlefield1.ball)
    battlefield1.ball.updatePosition()

    pg.display.flip()
    clock.tick(30)


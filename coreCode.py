import pygame as pg
from battlefield import Battlefield
import time
from constants import Constant



pg.display.init()
gameDisplay1 = pg.display.set_mode([Constant.SCREEN_WIDTH, Constant.SCREEN_HEIGHT])
clock = pg.time.Clock()


crashed = False

battlefield1 = Battlefield(Constant.SCREEN_WIDTH, Constant.SCREEN_HEIGHT)
battlefield1.addEdges()

pg.joystick.init()
if pg.joystick.get_count() != 1:
    print("joystick error, remove excess controllers or power cycle single controller")
    exit()
joystick = pg.joystick.Joystick(0)
joystick.init()
loopTime = time.time_ns()
previousLoopTime = loopTime

while not crashed:
    currentLoopTime = time.time_ns()
    gameDisplay1.fill((0,0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            crashed = True

    for surface in battlefield1.surfaces:
        surface.checkHit(battlefield1.ball)
        surface.move(currentLoopTime - previousLoopTime)
    battlefield1.player.checkHit(battlefield1.ball)
    battlefield1.ball.updatePosition(currentLoopTime - previousLoopTime)
    jhat = [joystick.get_axis(0), joystick.get_axis(1)]
    print(jhat)
    battlefield1.player.move(jhat,currentLoopTime - previousLoopTime)



    if time.time_ns() - loopTime > 33333333:
        loopTime = time.time_ns()
        for surface in battlefield1.surfaces:
            surface.draw(gameDisplay1)
        battlefield1.ball.draw(gameDisplay1)
        battlefield1.player.draw(gameDisplay1)
        pg.display.flip()

    previousLoopTime = currentLoopTime


pg.joystick.quit()


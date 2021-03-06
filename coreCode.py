import pygame as pg
from battlefield import Battlefield
import time
from constants import Constant



pg.display.init()
gameDisplay1 = pg.display.set_mode([Constant.SCREEN_WIDTH, Constant.SCREEN_HEIGHT])
clock = pg.time.Clock()


crashed = False

battlefield1 = Battlefield(Constant.SCREEN_WIDTH, Constant.SCREEN_HEIGHT)
battlefield1.initializeLevel()

loopTime = time.time_ns()
previousLoopTime = loopTime

while not crashed:
    currentLoopTime = time.time_ns() #main loop runs on time to keep frames and movement time dependent
    gameDisplay1.fill((0,0,0)) #black background
    for event in pg.event.get():
        if event.type == pg.QUIT:
            crashed = True
        elif event.type == pg.JOYBUTTONDOWN:
            battlefield1.player.triggerPressed()

    battlefield1.moveAll(currentLoopTime,previousLoopTime)
    battlefield1.checkHitboxes()



    if time.time_ns() - loopTime > 1e9 / Constant.FRAME_RATE: #draws a new frame 30 times a second
        loopTime = time.time_ns()
        battlefield1.draw(gameDisplay1)
        pg.display.flip() #update the screen

    previousLoopTime = currentLoopTime
    if battlefield1.checkWinConditions() == 1:
        battlefield1.initializeLevel()


pg.joystick.quit()


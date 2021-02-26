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
    currentLoopTime = time.time_ns() #main loop runs on time to keep frames and movement time dependent
    gameDisplay1.fill((0,0,0)) #black background
    for event in pg.event.get():
        if event.type == pg.QUIT:
            crashed = True

    for surface in battlefield1.surfaces:
        surface.checkHit(battlefield1.ball) #check if the ball has hit any surfaces
        surface.move(currentLoopTime - previousLoopTime) #update the position of all surfaces
    battlefield1.ball.updatePosition(currentLoopTime - previousLoopTime) #update the ball position
    battlefield1.player.jhat = [joystick.get_axis(0), joystick.get_axis(1)] #get the position of the joystick on the controller
    battlefield1.player.move(currentLoopTime - previousLoopTime) #move the player with the joystick
    battlefield1.player.checkHit(battlefield1.ball)  # chekc if the ball has hit the player



    if time.time_ns() - loopTime > 1e9 / Constant.FRAME_RATE: #draws a new frame 30 times a second
        loopTime = time.time_ns()
        for surface in battlefield1.surfaces:
            surface.draw(gameDisplay1)
        battlefield1.ball.draw(gameDisplay1)
        battlefield1.player.draw(gameDisplay1)
        pg.display.flip() #update the screen

    previousLoopTime = currentLoopTime


pg.joystick.quit()


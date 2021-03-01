import pygame as pg
from constants import Constant

pg.joystick.init()
joystick = pg.joystick.Joystick(0)
joystick.init()
clock = pg.time.Clock()
pg.display.init()
gameDisplay1 = pg.display.set_mode([Constant.SCREEN_WIDTH, Constant.SCREEN_HEIGHT])

while True:
    gameDisplay1.fill((0, 0, 0))  # black background
    for event in pg.event.get():
        if event.type==pg.JOYBUTTONDOWN:
            print("button pressed")
    print(joystick.get_button(5))
    print(joystick.get_axis(2), joystick.get_axis(3))
    clock.tick(1)
    pg.display.flip()
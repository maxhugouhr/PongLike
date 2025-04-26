import pygame as pg
import enum

class Controller():

    class Type(enum):
        CONTROLLER = "controller"
        KEYBOARD = "keyboard"

    class ButtonType(enum):
        GRAB = "grab"


    def __init__(self):
        pg.joystick.init()
        if pg.joystick.get_count() == 0:
            self.type = Controller.Type.KEYBOARD
        else:
            self.type = Controller.Type.CONTROLLER



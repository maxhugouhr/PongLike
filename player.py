import pygame as pg
from constants import Constant
from surface import Surface

class Player(Surface):

    def __init__(self, speed=[float(Constant.SCREEN_WIDTH/1e9),float(Constant.SCREEN_WIDTH/1e9)], leftEnd=[5,Constant.SCREEN_HEIGHT - 100], rightEnd=[50,Constant.SCREEN_HEIGHT - 100] , color=(255,0,255), width=5,reflector=True,speedMultiplier=1,defAngle=0):
        super().__init__(speed, leftEnd, rightEnd, color, width,reflector,speedMultiplier,defAngle)
        # magnitude of the velocity in pixels per nanosecond

    def move(self, jhat, time):
        if self.inBounds():
            if jhat[0] > 0.1:
                self.leftEndpoint[0] += jhat[0] * self.velocity[0] * time
                self.rightEndpoint[0] += jhat[0] * self.velocity[0] * time

            if jhat[1] > 0.1:
                self.leftEndpoint[1] += jhat[1] * self.velocity[1] * time
                self.rightEndpoint[1] += jhat[1] * self.velocity[1] * time

    def inBounds(self):
        if self.leftEndpoint[0] > 0 and self.rightEndpoint[0] < Constant.SCREEN_WIDTH:
            if self.leftEndpoint[1] > 0 and self.leftEndpoint[1] < Constant.SCREEN_HEIGHT:
                return True
        else:
            return False

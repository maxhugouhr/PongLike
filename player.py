import pygame as pg
from constants import Constant
from surface import Surface

class Player(Surface):

    def __init__(self, speed, leftEnd, rightEnd , color, width,reflector,speedMultiplier,defAngle):
        super().__init__(speed,leftEnd, rightEnd, color, width, reflector, speedMultiplier, defAngle)
        # magnitude of the velocity in pixels per nanosecond
        self.lowerBound = Constant.SCREEN_HEIGHT - self.width
        self.upperBound = Constant.SCREEN_HEIGHT*3/4


    def move(self, jhat, time):

        if jhat[0] > 0.2 or jhat[0] < -0.2:
            self.leftEndpoint[0] += jhat[0] * self.velocity[0] * time
            self.rightEndpoint[0] += jhat[0] * self.velocity[0] * time

        if jhat[1] > 0.2 or jhat[1] < -0.2:
            self.leftEndpoint[1] += jhat[1] * self.velocity[1] * time
            self.rightEndpoint[1] += jhat[1] * self.velocity[1] * time

        self.keepBounds()


    def keepBounds(self):
        if self.leftEndpoint[0] < 0:
            self.leftEndpoint[0] = 0
            self.rightEndpoint[0] = self.length
        if self.rightEndpoint[0] > Constant.SCREEN_WIDTH:
            self.rightEndpoint[0] = Constant.SCREEN_WIDTH
            self.leftEndpoint[0] = Constant.SCREEN_WIDTH - self.length
        if self.leftEndpoint[1] > self.lowerBound:
            self.leftEndpoint[1], self.rightEndpoint[1] = self.lowerBound, self.lowerBound
        if self.leftEndpoint[1] < self.upperBound:
            self.leftEndpoint[1], self.rightEndpoint[1] = self.upperBound, self.upperBound

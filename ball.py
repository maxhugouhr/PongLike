import pygame as pg
import numpy as np

class Ball():
    def __init__(self,position=(0,0), speed=(0,0), radius=1, color=(255,255,255)):
        self.radius = radius
        self.color = color
        self.velocity = speed
        self.position = position

    def draw(self,img):
        pg.draw.circle(img, self.color, (self.position[0], self.position[1]), self.radius)

    def updatePosition(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
import pygame as pg
import numpy as np

class Ball():
    def __init__(self,position=np.array((0.0,0.0)), speed=np.array((0.0,0.0)), radius=1, color=(255,255,255)):
        self.radius = radius
        self.color = color
        self.velocity = speed
        self.position = position

    def draw(self,img):
        pg.draw.circle(img, self.color, (self.pos[0], self.pos[1]), self.radius)
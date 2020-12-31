from reflector import Reflector
import numpy as np
import math
import pygame as pg

def unitVec(facing):
    return np.array((math.cos(facing), math.sin(facing)))

class Surface(Reflector):

    def __init__(self, speed=np.array((0.0,0.0)), leftEnd=0, rightEnd=0 , color=(255,255,255), width=0):
        self.leftEndpoint = leftEnd
        self.rightEndpoint = rightEnd
        self.color = color
        dy = float(rightEnd[1] - leftEnd[1])
        dx = float(rightEnd[0] - leftEnd[0])
        self.length = math.sqrt(dx**2 + dy**2)
        self.width = width
        self.speed = speed
        if dy < 0:
            self.normalVec = np.array((-dy,dx))
        else:
            self.normalVec = np.array(dy,-dx)


    def ends(self):
        forward = unitVec(self.rotation)
        beside = unitVec(self.rotation + math.pi/2)
        return self.pos + self.length*beside/2, self.pos - self.length*beside/2

    def draw(self, img):
        ends = self.ends()
        pg.draw.line(img, self.color, ends[0], ends[1], self.width)

    def setRotation(self,point1,point2):
        unit = np.linalg.norm(point2 - point1)
        return np.angle(unit) + math.pi/2

    def reflect(self,ball):
        #TODO
        raise NotImplementedError()


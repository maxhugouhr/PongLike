from point import Point
from reflector import Reflector
import numpy as np
import math

def unitVec(facing):
    return np.array((math.cos(facing), math.sin(facing)))

class Surface(Point, Reflector):

    def __init__(self, speed=np.array((0.0,0.0)), position=np.array((0.0,0.0)),facing=0, color=(255,255,255), length=0, width=0):
        super(speed, position, facing)
        self.color = color
        self.length = length
        self.width = width

    def ends(self):
        forward = unitVec(self.facing)
        beside = unitVec(self.facing + math.pi/2)
        return self.pos + self.length*beside/2, self.pos - self.length*beside/2

    def draw(self, img):
        ends = self.ends()
        cv.line(img, ends[0], ends[1], self.width, self.color)

    def setFacing(self,point1,point2):
        unit = np.linalg.norm(point2 - point1)
        return np.angle(unit) + math.pi/2
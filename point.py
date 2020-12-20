import numpy as np

class Point:
    def __init__(self, speed=np.array((0.0,0.0)), position=np.array((0.0,0.0)),facing=0):
        self.speed = speed
        self.pos = position
        self.facing = facing

    def draw(self,img):
        raise NotImplementedError()

    def move(self):
        self.pos += self.speed

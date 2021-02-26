from surface import Surface
from ball import Ball
from player import Player
from constants import Constant as C


class Battlefield():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surfaces = []
        self.ball = Ball([int(50),int(50)], [float(0),float(1)], float(self.height/(5e9)), 5, (255,255,255))
        self.player = Player()
        self.level = 1

    def addEdges(self):
        leftSurface = Surface([0,0],[0,0],[0, self.height],(255,255,255),5,True,1,0)
        rightSurface = Surface([0, 0],[self.width,0], [self.width,self.height], (255, 255, 255), 5, True, 1,0)
        topSurface = Surface([0,0], [0,0], [self.width,0], (255,255,255),3,True,1,0)
        bottomSurface = Surface([0, 0], [0, self.height], [self.width, self.height], (255, 255, 255), 3, True, 1, 0)
        self.surfaces.append(leftSurface)
        self.surfaces.append(rightSurface)
        self.surfaces.append(topSurface)
        self.surfaces.append(bottomSurface)


    def initializeLevelOne(self):
        pass
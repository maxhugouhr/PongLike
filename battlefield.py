from surface import Surface
from ball import Ball
from player import Player


class Battlefield():

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.surfaces = []
        self.ball = Ball([int(50),int(50)], [2,2], 5, (255,255,255))
        self.player = Player()
        self.level = 1

    def addEdges(self):
        leftSurface = Surface((0,0),(0,0),(0, self.height),(255,255,255),5,True,1,0)
        rightSurface = Surface((0, 0),(self.width,0), (self.width,self.height), (255, 255, 255), 5, True, 1,0)
        self.surfaces.append(leftSurface)
        self.surfaces.append(rightSurface)


    def initializeLevelOne(self):
        pass
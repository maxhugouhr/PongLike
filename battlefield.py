from surface import Surface
from ball import Ball
from player import Player
from constants import Constant


class Battlefield():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surfaces = []
        self.ball = Ball([int(50),int(50)], [float(0.5),float(0.5)], float(self.height/(2e9)), 4, (255,255,255))
        self.player = Player([float(Constant.SCREEN_WIDTH/1e9),float(Constant.SCREEN_WIDTH/1e9)], [Constant.SCREEN_WIDTH/2,Constant.SCREEN_HEIGHT - 100], [Constant.SCREEN_WIDTH/2 + 50,Constant.SCREEN_HEIGHT - 100], (255,0,255), 5, True,1,0)
        self.level = 1

    def addEdges(self):
        leftSurface = Surface([0,0],[0,0],[0, self.height],(255,255,255),0,True,1,0)
        rightSurface = Surface([0, 0],[self.width,0], [self.width,self.height], (255, 255, 255), 0, True, 1,0)
        topSurface = Surface([0,0], [0,0], [self.width,0], (255,255,255),3,True,1,0)
        bottomSurface = Surface([0, 0], [0, self.height], [self.width, self.height], (255, 255, 255), 3, True, 1, 0)
        self.surfaces.append(leftSurface)
        self.surfaces.append(rightSurface)
        self.surfaces.append(topSurface)
        self.surfaces.append(bottomSurface)


    def initializeLevelOne(self):
        pass
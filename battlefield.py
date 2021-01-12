from surface import Surface
from ball import Ball


class Battlefield():

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.surfaces = []
        self.ball = Ball([int(self.width/2),int(self.height/2)], [2,2], 5, (255,255,255))

    def addEdges(self):
        leftSurface = Surface((0,0),(0,0),(0, self.height),(255,255,255),5,True,1,0)
        rightSurface = Surface((0, 0),(self.width,0), (self.width,self.height), (255, 255, 255), 5, True, 1,0)
        topSurface = Surface((0, 0), (0,0),(self.width,0), (255, 255, 255), 5, True, 1,0)
        bottomSurface = Surface((0, 0), (0,self.height),(self.width,self.height), (255, 255, 255), 5, True, 1,0)
        self.surfaces.append(leftSurface)
        self.surfaces.append(rightSurface)
        self.surfaces.append(topSurface)
        self.surfaces.append(bottomSurface)
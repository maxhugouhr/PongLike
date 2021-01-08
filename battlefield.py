from coreCode import SCREEN_HEIGHT, SCREEN_WIDTH
from surface import Surface
from ball import Ball
import math
import numpy as np

class Battlefield:

    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width
        self.surfaces = []
        self.ball = Ball()

    def addEdges(self):
        leftSurface = Surface(self,(0,0),(0,0),(0,SCREEN_HEIGHT),(255,255,255),5,True,1)
        rightSurface = Surface(self, (0, 0),(SCREEN_WIDTH,0), (SCREEN_WIDTH,SCREEN_HEIGHT), (255, 255, 255), 5, True, 1)
        topSurface = Surface(self, (0, 0), (0,0),(SCREEN_WIDTH,0), (0, 0, 0), 5, True, 1)
        bottomSurface = Surface(self, (0, 0), (0,SCREEN_HEIGHT),(SCREEN_WIDTH,SCREEN_HEIGHT), (0, 0, 0), 5, True, 1)
        self.surfaces.append(leftSurface)
        self.surfaces.append(rightSurface)
        self.surfaces.append(topSurface)
        self.surfaces.append(bottomSurface)
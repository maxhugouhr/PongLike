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
        leftSurface = Surface(self,np.array((0.0,0.0)),np.array(SCREEN_HEIGHT/2, 0),math.pi/2,(0,0,0),SCREEN_HEIGHT,0)
        rightSurface = Surface(self,np.array((0.0,0.0)),np.array(SCREEN_HEIGHT/2,SCREEN_WIDTH),math.pi/2,(0,0,0),SCREEN_HEIGHT,0)
        topSurface = Surface(self,np.array((0.0,0.0)),np.array(SCREEN_WIDTH/2, 0),0,(0,0,0),SCREEN_WIDTH,0)
        bottomSurface = Surface(self,np.array((0.0,0.0)),np.array(SCREEN_WIDTH/2, SCREEN_HEIGHT),0,(0,0,0),SCREEN_WIDTH,0)
        self.surfaces.append(leftSurface)
        self.surfaces.append(rightSurface)
        self.surfaces.append(topSurface)
        self.surface.append(bottomSurface)
from surface import Surface
from ball import Ball

class Battlefield:

    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width
        self.surfaces = []
        self.ball = Ball()

    def addBorder(self,offset=10):
        corners = [(offset,offset),
                   (self.length-offset,offset),
                   (self.length-offset, self.width-offset),
                   (offset, self.width-offset)]

        for i in range(4):
            center = (corners[i-1] + corners[i])/2

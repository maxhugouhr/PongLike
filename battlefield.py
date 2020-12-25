from surface import Surface
from ball import Ball

class Battlefield:

    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width
        self.surfaces = []
        self.ball = Ball()

    
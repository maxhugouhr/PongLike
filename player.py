import pygame as pg
from surface import Surface

class Player(Surface):

    def __init__(self, speed=(3,3), leftEnd=(0,0), rightEnd=(0,0) , color=(255,0,255), width=3,reflector=True,speedMultiplier=1,defAngle=0):
        super().__init__(speed, leftEnd, rightEnd, color, width,reflector,speedMultiplier,defAngle)

    def move(self, event):
        pass

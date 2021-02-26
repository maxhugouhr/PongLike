import pygame as pg
from constants import Constant


class Ball():
    def __init__(self,position, speed, magnitude, radius=1, color=(255,255,255)):
        self.radius = radius
        self.color = color
        self.velocity = speed #unit direction the ball is traveling
        self.position = position
        self.velocMag = magnitude #magnitude of the velocity in pixels per nanosecond

    def draw(self,img):
        pg.draw.circle(img, self.color, (self.position[0], self.position[1]), self.radius)

    def updatePosition(self,time): #moves the ball according to it's velocity
        self.position[0] += self.velocity[0] * self.velocMag * time
        self.position[1] += self.velocity[1] * self.velocMag * time

    def changePosition(self, position): #force changes the position of the ball
        self.position[0] = position[0]
        self.position[1] = position[1]
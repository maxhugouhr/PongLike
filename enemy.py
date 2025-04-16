from graphicalEntity import GraphicalEntity
from physicalEntity import PhysicalEntity
from constant import Constant
import random as rand
import math
import numpy as np
import functions


class Enemy(GraphicalEntity, PhysicalEntity):

    def __init__(self, speed, leftEnd, length, color, width, ball, speedMultiplier=1):

        self.leftEndpoint = np.array(leftEnd)
        self.speed = speed
        self.color = color
        self.width = width
        self.speedMultiplier = speedMultiplier
        self.length = length
        self.rightEndpoint = np.array([self.leftEndpoint[0] + self.length, self.leftEndpoint[1]])
        self.ball = ball


    def move(self, time):
        self.trackBall(time)
        self.keepBounds()

    def keepBounds(self):
        if self.leftEndpoint[0] < 0:
            self.leftEndpoint[0] = 0
            self.rightEndpoint[0] = self.length
        if self.rightEndpoint[0] > Constant.SCREEN_WIDTH:
            self.rightEndpoint[0] = Constant.SCREEN_WIDTH
            self.leftEndpoint[0] = Constant.SCREEN_WIDTH - self.length

    def trackBall(self, time):
        midpoint = self.leftEndpoint[0] + self.length / 2
        if self.ball.position[0] > midpoint:
            self.leftEndpoint[0] += self.speed * time
            self.rightEndpoint[0] += self.speed * time
        elif self.ball.position[0] < midpoint:
            self.leftEndpoint[0] -= self.speed * time
            self.rightEndpoint[0] -= self.speed * time

    def reflect(self,ball):
        # transforms all surfaces to a horizontal surface, reflects by reversing y-velocity,
        # then find the out angle and transforms back to normal coordinates
        ball.unitVelocity = functions.reflectedAngle(ball.unitVelocity,self.leftEndpoint,self.rightEndpoint)


import time
from graphicalEntity import GraphicalEntity
from physicalEntity import PhysicalEntity
import numpy as np
import math
import pygame as pg
from constant import Constant
import functions

class Reflector(PhysicalEntity, GraphicalEntity):

    def __init__(self, leftEnd, rightEnd, color, width, velocity=[0,0], speedMultiplier=1):


        self.leftEndpoint = np.array(leftEnd)
        self.rightEndpoint = np.array(rightEnd)
        self.color = color

        normalizedRightEnd = (rightEnd[0] - leftEnd[0], rightEnd[1] - leftEnd[1])
        unitAngle = math.atan2(normalizedRightEnd[1], normalizedRightEnd[0])
        if unitAngle < math.pi/2:
            self.surfaceAngle = unitAngle
        else:
            self.surfaceAngle = -(2*math.pi - unitAngle)

        self.length = math.sqrt(normalizedRightEnd[0]**2 + normalizedRightEnd[1]**2)
        self.width = width
        self.velocity = np.array(velocity)
        self.speedMultiplier = speedMultiplier

    def draw(self,img):
        pg.draw.line(img,self.color,tuple(self.leftEndpoint), tuple(self.rightEndpoint), self.width)

    def move(self,time): #updates the position of a moving surface
        self.leftEndpoint += self.velocity * time
        self.rightEndpoint += self.velocity * time


    def checkHit(self,ball):
        pixelTolerance = 4
        dy = self.rightEndpoint[1] - self.leftEndpoint[1]
        dx = self.rightEndpoint[0] - self.leftEndpoint[0]
        if (abs(dx) < pixelTolerance): #if the surface is vertical
            if (ball.position[1] < self.rightEndpoint[1] + ball.radius and ball.position[1] > self.leftEndpoint[1] - ball.radius):
                if abs(self.leftEndpoint[0] - ball.position[0]) < pixelTolerance:
                    self.impact(ball)
        elif (abs(dy) < pixelTolerance): #if the surface is horizontal
            if (ball.position[0] < self.rightEndpoint[0] + ball.radius and ball.position[0] > self.leftEndpoint[0] - ball.radius):
                if abs(ball.position[1] - self.leftEndpoint[1]) < pixelTolerance:
                    self.impact(ball)
        else:
            y = lambda x: (dy/dx)*(x - self.leftEndpoint[0]) + self.leftEndpoint[1] #gives the y value of the surface for a given x value
            surfYValue = y(ball.position[0])
            if abs(surfYValue - ball.position[1]) < pixelTolerance:
                self.impact(ball)

    def impact(self,ball):
        if ball.lastHitObject != id(self):
            ball.lastHitTime = time.time_ns()
            ball.lastHitObject = id(self)
            self.reflect(ball)

    def reflect(self,ball):
        # transforms all surfaces to a horizontal surface, reflects by reversing y-velocity,
        # then find the out angle and transforms back to normal coordinates
        ballAngle = float(math.atan2(ball.unitVelocity[1], ball.unitVelocity[0]))  # angle with respect to the x axis
        flatBallAngle = ballAngle - self.surfaceAngle
        refTransBallVeloc = (math.cos(flatBallAngle), -math.sin(flatBallAngle))
        transOutAngle = math.atan2(refTransBallVeloc[1], refTransBallVeloc[0])
        actualOutAngle = transOutAngle + self.surfaceAngle
        ball.unitVelocity[0] = math.cos(actualOutAngle)
        ball.unitVelocity[1] = math.sin(actualOutAngle)
        ball.speed *= self.speedMultiplier
from reflector import Reflector
import numpy as np
import math
import pygame as pg

class Surface(Reflector):

    def __init__(self, speed=(0,0), leftEnd=0, rightEnd=0 , color=(255,255,255), width=0,reflector=True,speedMultiplier=1):
        self.leftEndpoint = leftEnd
        self.rightEndpoint = rightEnd
        self.color = color
        dy = float(rightEnd[1] - leftEnd[1])
        dx = float(rightEnd[0] - leftEnd[0])
        self.length = math.sqrt(dx**2 + dy**2)
        self.width = width
        self.speed = speed
        self.angle = float(math.atan(dy/dx)) #angle with respect to the horizontal x axis, between 0 and 2pi
        self.isReflector = reflector #if surface is a reflector then it reflects the ball, otherwise it deflects the ball
        self.speedMultiplier = speedMultiplier #multiplies the ball speed when hit


    def draw(self, img):
        pg.draw.line(img, self.color, self.leftEndpoint, self.rightEndpoint, self.width)


    def reflect(self,ball):
        ballAngle = float(math.atan(ball.velocity[1]/ball.velocity[0])) #angle with respect to the x axis
        reflectionAngle = self.angle - ballAngle #finds angle between the ball's velocity and the surface
        newAngle = math.pi - reflectionAngle #new angle that the velocity will be coming out at
        ballVelocityMag = self.speedMultiplier*math.sqrt(ball.velocity[0]**2 + ball.velocity[1]**2)
        ball.velocity[0] = ballVelocityMag*math.cos(newAngle) #updates the balls velocity after reflection
        ball.velocity[1] = ballVelocityMag*math.sin(newAngle)

    def deflect(self,ball):
        # TODO implement this method
        pass


    def checkHit(self,ball):
        if ball.position[0] < self.rightEndpoint[0] and ball.position[0] > self.leftEndpoint[0]:
            dy = float(self.rightEndpoint[1] - self.leftEndpoint[1])
            dx = float(self.rightEndpoint[0] - self.leftEndpoint[0])
            slope = float(dy/dx)
            surfaceYValue = slope*(ball.position[0] - self.leftEndpoint[0]) + self.rightEndpoint[0]
            ballVelocityMag = math.sqrt(ball.velocity[0] ** 2 + ball.velocity[1] ** 2)
            if math.abs(surfaceYValue - ball.position[1]) < 1.1*ballVelocityMag:
                if self.isReflector:
                    self.reflect(self,ball)
                else:
                    self.deflect(self,ball)

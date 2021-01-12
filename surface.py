from reflector import Reflector
import math
import pygame as pg

class Surface(Reflector):
    #For vertical surfaces, the left endpoint is defined as the top point and the right endpoint is the bottom
    def __init__(self, speed=(0,0), leftEnd=(0,0), rightEnd=(0,0) , color=(255,255,255), width=0,reflector=True,speedMultiplier=1,defAngle=0):
        self.leftEndpoint = leftEnd
        self.rightEndpoint = rightEnd
        self.color = color
        dy = float(rightEnd[1] - leftEnd[1])
        dx = float(rightEnd[0] - leftEnd[0])

        if dx == 0:
            self.angle = math.pi/2
        elif dy == 0:
            self.angle = math.pi
        else:
            self.angle = float(math.atan(dy / dx))  # angle with respect to the horizontal x axis, between 0 and 2pi

        self.length = math.sqrt(dx**2 + dy**2)
        self.width = width
        self.speed = speed
        self.isReflector = reflector #if surface is a reflector then it reflects the ball, otherwise it deflects the ball
        self.speedMultiplier = speedMultiplier #multiplies the ball speed when hit
        self.deflectionAngle = defAngle


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
        ballVelocityMag = math.sqrt(ball.velocity[0] ** 2 + ball.velocity[1] ** 2)
        if (self.leftEndpoint[0] == self.rightEndpoint[0]):
            if abs(ball.position[0] - self.leftEndpoint[0]) < ballVelocityMag and ball.position[1] < self.rightEndpoint[1] and ball.position[1] > self.leftEndpoint[1]:
                if self.isReflector:
                    self.reflect(ball)
                else:
                    self.deflect(ball)
        elif self.leftEndpoint[1] == self.rightEndpoint[1]:
            if abs(ball.position[0] - self.leftEndpoint[1]) <  ballVelocityMag and ball.position[0] < self.rightEndpoint[0] and ball.position[0] > self.leftEndpoint[0]:
                if self.isReflector:
                    self.reflect(ball)
                else:
                    self.deflect(ball)
        elif ball.position[0] < self.rightEndpoint[0] and ball.position[0] > self.leftEndpoint[0]:
            dy = float(self.rightEndpoint[1] - self.leftEndpoint[1])
            dx = float(self.rightEndpoint[0] - self.leftEndpoint[0])
            slope = float(dy/dx)
            surfaceYValue = slope*(ball.position[0] - self.leftEndpoint[0]) + self.rightEndpoint[0]
            if abs(surfaceYValue - ball.position[1]) < ballVelocityMag:
                if self.isReflector:
                    self.reflect(ball)
                else:
                    self.deflect(ball)

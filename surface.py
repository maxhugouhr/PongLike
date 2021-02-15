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

        normRightEnd = (rightEnd[0] - leftEnd[0], rightEnd[1] - leftEnd[1])
        unitAngle = math.atan2(normRightEnd[1],normRightEnd[0])
        if unitAngle < math.pi/2:
            self.angleToHor = unitAngle
        else:
            self.angleToHor = -(2*math.pi - unitAngle)

        self.length = math.sqrt(normRightEnd[0]**2 + normRightEnd[1]**2)
        self.width = width
        self.speed = speed
        self.isReflector = reflector #if surface is a reflector then it reflects the ball, otherwise it deflects the ball
        self.speedMultiplier = speedMultiplier #multiplies the ball speed when hit
        self.deflectionAngle = defAngle


    def draw(self, img):
        pg.draw.line(img, self.color, self.leftEndpoint, self.rightEndpoint, self.width)


    def reflect(self,ball):
        ballAngle = float(math.atan2(ball.velocity[1],ball.velocity[0])) #angle with respect to the x axis
        flatBallAngle = ballAngle - self.angleToHor
        ballMagVeloc = math.sqrt(ball.velocity[1]**2 + ball.velocity[0]**2)
        refTransBallVeloc = (math.cos(flatBallAngle), -math.sin(flatBallAngle))
        transOutAngle = math.atan2(refTransBallVeloc[1],refTransBallVeloc[0])
        actualOutAngle = transOutAngle + self.angleToHor
        ball.velocity[0] = ballMagVeloc*math.cos(actualOutAngle)
        ball.velocity[1] = ballMagVeloc*math.sin(actualOutAngle)


    def deflect(self,ball):
        # TODO implement this method
        pass


    def checkHit(self,ball):
        dy = self.rightEndpoint[1] - self.leftEndpoint[1]
        dx = self.rightEndpoint[0] - self.leftEndpoint[0]
        ballVelocityMag = math.sqrt(ball.velocity[0] ** 2 + ball.velocity[1] ** 2)
        if (self.leftEndpoint[0] == self.rightEndpoint[0]): #if the surface is vertical
            if (ball.position[1] < self.rightEndpoint[1] and ball.position[1] > self.leftEndpoint[1]):
                if abs(self.leftEndpoint[0] - ball.position[0]) < ballVelocityMag:
                    self.reflect(ball)
        elif (self.leftEndpoint[1] == self.rightEndpoint[1]): #if the surface is horizontal
            if (ball.position[0] < self.rightEndpoint[0] and ball.position[0] > self.leftEndpoint[0]):
                if abs(ball.position[1] - self.leftEndpoint[1]) < ballVelocityMag:
                    self.reflect(ball)
        else:
            y = lambda a: (dy/dx)*(a - self.leftEndpoint[0]) + self.leftEndpoint[1]
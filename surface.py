import math
import pygame as pg
import time

class Surface():
    #For vertical surfaces, the left endpoint is defined as the top point and the right endpoint is the bottom
    def __init__(self, speed=(0,0), leftEnd=(0,0), rightEnd=(0,0) , color=(255,255,255), width=0,reflector=True,speedMultiplier=1,defAngle=0):
        self.leftEndpoint = leftEnd
        self.rightEndpoint = rightEnd
        self.color = color

        #adjusts the surface to the origin to find the angle of the surface from the horizontal plane
        normRightEnd = (rightEnd[0] - leftEnd[0], rightEnd[1] - leftEnd[1])
        unitAngle = math.atan2(normRightEnd[1],normRightEnd[0]) #defines the angle of the surface using normal math angles
        if unitAngle < math.pi/2: #angles above the x-axis (negative x) will be positive angles
            self.angleToHor = unitAngle
        else: #angles below the x-axis (positive x) will be nagative angles
            self.angleToHor = -(2*math.pi - unitAngle)

        self.length = math.sqrt(normRightEnd[0]**2 + normRightEnd[1]**2)
        self.width = width
        self.velocity = speed
        self.isReflector = reflector #if surface is a reflector then it reflects the ball, otherwise it deflects the ball
        self.speedMultiplier = speedMultiplier #multiplies the ball speed when hit
        self.deflectionAngle = defAngle
        self.lastHitTime = time.time_ns()


    def draw(self, img): #draws a straight line for the surface
        pg.draw.line(img, self.color, self.leftEndpoint, self.rightEndpoint, self.width)


    def move(self): #updates the position of a moving surface
        self.leftEndpoint[0] += self.velocity[0]
        self.rightEndpoint[0] += self.velocity[0]
        self.leftEndpoint[1] += self.velocity[1]
        self.rightEndpoint[1] += self.velocity[1]


    def impact(self,ball):
        if abs(self.lastHitTime - time.time_ns()) > 500000000: #ensures the ball can't bounce twice off the same surface in short time frames
            self.lastHitTime = time.time_ns()
            if self.isReflector:
                self.reflect(ball)
            else:
                self.deflect(ball)



    def reflect(self,ball):
        #transforms all surfaces to a horizontal surface, reflects by reversing y-velocity,
        # then find the out angle and transforms back to normal coordinates
        ballAngle = float(math.atan2(ball.velocity[1],ball.velocity[0])) #angle with respect to the x axis
        flatBallAngle = ballAngle - self.angleToHor
        ballMagVeloc = math.sqrt(ball.velocity[1]**2 + ball.velocity[0]**2)
        refTransBallVeloc = (math.cos(flatBallAngle), -math.sin(flatBallAngle))
        transOutAngle = math.atan2(refTransBallVeloc[1],refTransBallVeloc[0])
        actualOutAngle = transOutAngle + self.angleToHor
        ball.velocity[0] = ballMagVeloc*math.cos(actualOutAngle)*self.speedMultiplier
        ball.velocity[1] = ballMagVeloc*math.sin(actualOutAngle)*self.speedMultiplier


    def deflect(self,ball): #for surfaces that deflect the ball by a certain angle rather than complete reflection
        ballAngle = float(math.atan2(ball.velocity[1], ball.velocity[0]))  # angle with respect to the x axis
        outAngle = ballAngle + self.deflectionAngle
        ballMagVeloc = math.sqrt(ball.velocity[1] ** 2 + ball.velocity[0] ** 2)
        ball.velocity[0] = ballMagVeloc * math.cos(outAngle) * self.speedMultiplier
        ball.velocity[1] = ballMagVeloc * math.sin(outAngle) * self.speedMultiplier


    def checkHit(self,ball):
        ballVelocityMag = math.sqrt(ball.velocity[0] ** 2 + ball.velocity[1] ** 2)
        if (self.leftEndpoint[0] == self.rightEndpoint[0]): #if the surface is vertical
            if (ball.position[1] < self.rightEndpoint[1] and ball.position[1] > self.leftEndpoint[1]):
                if abs(self.leftEndpoint[0] - ball.position[0]) < ballVelocityMag:
                    self.impact(ball)
        elif (self.leftEndpoint[1] == self.rightEndpoint[1]): #if the surface is horizontal
            if (ball.position[0] < self.rightEndpoint[0] and ball.position[0] > self.leftEndpoint[0]):
                if abs(ball.position[1] - self.leftEndpoint[1]) < ballVelocityMag:
                    self.impact(ball)
        else:
            dy = self.rightEndpoint[1] - self.leftEndpoint[1]
            dx = self.rightEndpoint[0] - self.leftEndpoint[0]
            y = lambda a: (dy/dx)*(a - self.leftEndpoint[0]) + self.leftEndpoint[1] #gives the y value of the surface for a given x value
            surfYValue = y(ball.position[0])
            if abs(surfYValue - ball.position[1]) < ballVelocityMag:
                self.impact(ball)
import math
import pygame as pg
import time
from constant import Constant



class SurfaceToChange():
    #For vertical surfaces, the left endpoint is defined as the top point and the right endpoint is the bottom
    def __init__(self, leftEnd, rightEnd, color, width, speed=[0,0], reflector=True, speedMultiplier=1, deflectionAngle=0):
        self.leftEndpoint = leftEnd
        self.rightEndpoint = rightEnd
        self.color = color

        #adjusts the surface to the origin to find the angle of the surface from the horizontal plane
        normalizedRightEnd = (rightEnd[0] - leftEnd[0], rightEnd[1] - leftEnd[1])
        unitAngle = math.atan2(normalizedRightEnd[1],normalizedRightEnd[0]) #defines the angle of the surface using normal math angles
        if unitAngle < math.pi/2: #angles above the x-axis (negative x) will be positive angles
            self.surfaceAngle = unitAngle
        else: #angles below the x-axis (positive x) will be nagative angles
            self.surfaceAngle = -(2 * math.pi - unitAngle)

        self.length = math.sqrt(normalizedRightEnd[0]**2 + normalizedRightEnd[1]**2)
        self.width = width
        self.velocity = speed #magnitude of the velocity in pixels per nanosecond
        self.isReflector = reflector #if surface is a reflector then it reflects the ball, otherwise it deflects the ball
        self.speedMultiplier = speedMultiplier #multiplies the ball speed when hit
        self.deflectionAngle = deflectionAngle
        self.lastHitTime = time.time_ns()


    def draw(self, img): #draws a straight line for the surface
        pg.draw.line(img, self.color, self.leftEndpoint, self.rightEndpoint, self.width)


    def move(self,time): #updates the position of a moving surface
        self.leftEndpoint[0] += self.velocity[0] * time
        self.rightEndpoint[0] += self.velocity[0] * time
        self.leftEndpoint[1] += self.velocity[1] * time
        self.rightEndpoint[1] += self.velocity[1] * time


    def impact(self,ball):
        if ball.lastHitObject != id(self): #ensures the ball can't bounce twice off the same surface
            self.lastHitTime = time.time_ns()
            ball.lastHitObject = id(self)
            if self.isReflector:
                self.reflect(ball)
            else:
                self.deflect(ball)



    def reflect(self,ball):
        #transforms all surfaces to a horizontal surface, reflects by reversing y-velocity,
        # then find the out angle and transforms back to normal coordinates
        ballAngle = float(math.atan2(ball.velocity[1],ball.velocity[0])) #angle with respect to the x axis
        flatBallAngle = ballAngle - self.surfaceAngle
        refTransBallVeloc = (math.cos(flatBallAngle), -math.sin(flatBallAngle))
        transOutAngle = math.atan2(refTransBallVeloc[1],refTransBallVeloc[0])
        actualOutAngle = transOutAngle + self.surfaceAngle
        ball.velocity[0] = math.cos(actualOutAngle)
        ball.velocity[1] = math.sin(actualOutAngle)
        ball.speed *= self.speedMultiplier


    def deflect(self,ball): #for surfaces that deflect the ball by a certain angle rather than complete reflection
        ballAngle = float(math.atan2(ball.velocity[1], ball.velocity[0]))  # angle with respect to the x axis
        outAngle = ballAngle + self.deflectionAngle
        ball.velocity[0] = math.cos(outAngle)
        ball.velocity[1] = math.sin(outAngle)
        ball.speed *= self.speedMultiplier


    def checkHit(self,ball):
        dy = self.rightEndpoint[1] - self.leftEndpoint[1]
        dx = self.rightEndpoint[0] - self.leftEndpoint[0]
        if (abs(dx) < Constant.TOLERANCE): #if the surface is vertical
            if (ball.position[1] < self.rightEndpoint[1] + ball.radius and ball.position[1] > self.leftEndpoint[1] - ball.radius):
                if abs(self.leftEndpoint[0] - ball.position[0]) < Constant.TOLERANCE:
                    self.impact(ball)
        elif (abs(dy) < Constant.TOLERANCE): #if the surface is horizontal
            if (ball.position[0] < self.rightEndpoint[0] + ball.radius and ball.position[0] > self.leftEndpoint[0] - ball.radius):
                if abs(ball.position[1] - self.leftEndpoint[1]) < Constant.TOLERANCE:
                    self.impact(ball)
        else:
            y = lambda x: (dy/dx)*(x - self.leftEndpoint[0]) + self.leftEndpoint[1] #gives the y value of the surface for a given x value
            surfYValue = y(ball.position[0])
            if abs(surfYValue - ball.position[1]) < Constant.TOLERANCE:
                self.impact(ball)
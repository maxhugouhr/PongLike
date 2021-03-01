import pygame as pg
from constants import Constant
from surface import Surface
import random as rand
import math
import time

class Player(Surface):

    def __init__(self, speed, leftEnd, rightEnd , color, width,reflector,speedMultiplier,defAngle):
        super().__init__(speed,leftEnd, rightEnd, color, width, reflector, speedMultiplier, defAngle)
        # magnitude of the velocity in pixels per nanosecond
        self.lowerBound = Constant.SCREEN_HEIGHT - self.width
        self.upperBound = Constant.SCREEN_HEIGHT*3/4
        self.leftJhat = [0, 0]
        pg.joystick.init()
        if pg.joystick.get_count() != 1:
            print("joystick error, remove excess controllers or check connectivity")
            exit()

        self.joystick = pg.joystick.Joystick(0)
        self.joystick.init()
        self.randomAngle = False
        self.lastTriggerTime = 0
        self.grabTime = 0


    def move(self, time):
        self.leftJhat = [self.joystick.get_axis(0), self.joystick.get_axis(1)]
        if self.leftJhat[0] > 0.15 or self.leftJhat[0] < -0.15:
            self.leftEndpoint[0] += self.leftJhat[0] * self.velocity[0] * time
            self.rightEndpoint[0] += self.leftJhat[0] * self.velocity[0] * time

        if self.leftJhat[1] > 0.15 or self.leftJhat[1] < -0.15:
            self.leftEndpoint[1] += self.leftJhat[1] * self.velocity[1] * time
            self.rightEndpoint[1] += self.leftJhat[1] * self.velocity[1] * time

        self.keepBounds()


    def keepBounds(self):
        if self.leftEndpoint[0] < 0:
            self.leftEndpoint[0] = 0
            self.rightEndpoint[0] = self.length
        if self.rightEndpoint[0] > Constant.SCREEN_WIDTH:
            self.rightEndpoint[0] = Constant.SCREEN_WIDTH
            self.leftEndpoint[0] = Constant.SCREEN_WIDTH - self.length
        if self.leftEndpoint[1] > self.lowerBound:
            self.leftEndpoint[1], self.rightEndpoint[1] = self.lowerBound, self.lowerBound
        if self.leftEndpoint[1] < self.upperBound:
            self.leftEndpoint[1], self.rightEndpoint[1] = self.upperBound, self.upperBound


    def reflect(self,ball):
        rand.seed(time.time_ns())
        ballAngle = float(math.atan2(ball.velocity[1], ball.velocity[0]))  # angle with respect to the x axis
        flatBallAngle = ballAngle - self.angleToHor
        refTransBallVeloc = (math.cos(flatBallAngle), -math.sin(flatBallAngle))
        transOutAngle = math.atan2(refTransBallVeloc[1], refTransBallVeloc[0])
        actualOutAngle = transOutAngle + self.angleToHor
        actualOutAngle += rand.choice([-1,1]) * (math.pi / 6) * rand.random()
        ball.velocity[0] = math.cos(actualOutAngle)
        ball.velocity[1] = math.sin(actualOutAngle)
        ball.velocMag *= self.speedMultiplier

    def triggerPressed(self):
        if self.joystick.get_button(5): #right trigger on an XBox controller
            self.lastTriggerTime = time.time_ns()


    def grabBall(self,ball):
        if ball.isGrabbed:
            vecNorm = math.sqrt(self.joystick.get_axis(2)**2 + self.joystick.get_axis(3)**2) + 0.0000000001
            ball.velocity = [self.joystick.get_axis(2) / vecNorm, self.joystick.get_axis(3) / vecNorm]
            if not self.joystick.get_button(5):#time.time_ns() - self.grabTime > 1e9:
                ball.isGrabbed = False
        if abs(self.lastTriggerTime - self.lastHitTime) < 1e9*0.2:
            ball.isGrabbed = True
            self.grabTime = time.time_ns()

    def impact(self,ball):
        if ball.isGrabbed:
            self.lastHitTime = time.time_ns()
        elif abs(self.lastHitTime - time.time_ns()) > 1e9/100:
            self.lastHitTime = time.time_ns()
            self.reflect(ball)



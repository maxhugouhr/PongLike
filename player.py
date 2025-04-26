import pygame as pg
import numpy as np
from constant import Constant
from graphicalEntity import GraphicalEntity
from physicalEntity import PhysicalEntity
import random as rand
import math
import time

class Player(GraphicalEntity, PhysicalEntity):


    def __init__(self, speed, leftEnd, rightEnd, color, width):
        self.leftEndpoint = np.array(leftEnd)
        self.rightEndpoint = np.array(rightEnd)
        self.color = color
        self.lastHitTime = time.perf_counter()

        normalizedRightEnd = (rightEnd[0] - leftEnd[0], rightEnd[1] - leftEnd[1])
        unitAngle = math.atan2(normalizedRightEnd[1],
                               normalizedRightEnd[0])  # defines the angle of the surface using normal math angles
        if unitAngle < math.pi / 2:  # angles above the x-axis (negative x) will be positive angles
            self.surfaceAngle = unitAngle
        else:  # angles below the x-axis (positive x) will be nagative angles
            self.surfaceAngle = -(2 * math.pi - unitAngle)

        self.length = math.sqrt(normalizedRightEnd[0] ** 2 + normalizedRightEnd[1] ** 2)
        self.width = width

        # magnitude of the velocity in pixels per nanosecond
        self.lowerMovementBoundary = Constant.SCREEN_HEIGHT - self.width
        self.upperMovementBoundary = Constant.SCREEN_HEIGHT * 3 / 4
        self.stickPosition = [0, 0]
        self.speed = speed

        pg.joystick.init()
        if pg.joystick.get_count() != 1:
            print("joystick error, remove excess controllers or check connectivity")
            exit()

        self.joystick = pg.joystick.Joystick(0)
        self.joystick.init()

        self.lastTriggerTime = time.perf_counter()
        self.grabTime = None


    def normalizeJoystickPosition(self, stickPosition):
        if Constant.STICK_TOLERANCE > stickPosition[0] > -Constant.STICK_TOLERANCE:
            return [0,0]
        if Constant.STICK_TOLERANCE > stickPosition[1] > -Constant.STICK_TOLERANCE:
            return [0,0]
        stickPositionMagnitude = math.sqrt(self.stickPosition[0] ** 2 + self.stickPosition[1] ** 2)
        return [x / stickPositionMagnitude for x in stickPosition]



    def move(self, time):
        self.stickPosition = [self.joystick.get_axis(0), self.joystick.get_axis(1)]
        normalizedStickPosition = self.normalizeJoystickPosition(self.stickPosition)

        self.leftEndpoint[0] += normalizedStickPosition[0] * self.speed * time
        self.rightEndpoint[0] += normalizedStickPosition[0] * self.speed * time

        self.leftEndpoint[1] += normalizedStickPosition[1] * self.speed * time
        self.rightEndpoint[1] += normalizedStickPosition[1] * self.speed * time

        self.keepBounds()

    def draw(self,img):
        pg.draw.line(img,self.color,self.leftEndpoint, self.rightEndpoint, self.width)


    def keepBounds(self):
        if self.leftEndpoint[0] < 0:
            self.leftEndpoint[0] = 0
            self.rightEndpoint[0] = self.length
        if self.rightEndpoint[0] > Constant.SCREEN_WIDTH:
            self.rightEndpoint[0] = Constant.SCREEN_WIDTH
            self.leftEndpoint[0] = Constant.SCREEN_WIDTH - self.length
        if self.leftEndpoint[1] > self.lowerMovementBoundary:
            self.leftEndpoint[1], self.rightEndpoint[1] = self.lowerMovementBoundary, self.lowerMovementBoundary
        if self.leftEndpoint[1] < self.upperMovementBoundary:
            self.leftEndpoint[1], self.rightEndpoint[1] = self.upperMovementBoundary, self.upperMovementBoundary


    def reflect(self,ball):
        rand.seed(time.perf_counter())
        ballAngle = float(math.atan2(ball.unitVelocity[1], ball.unitVelocity[0]))  # angle with respect to the x axis
        flatBallAngle = ballAngle - self.surfaceAngle
        refTransBallVeloc = (math.cos(flatBallAngle), -math.sin(flatBallAngle))
        transOutAngle = math.atan2(refTransBallVeloc[1], refTransBallVeloc[0])
        actualOutAngle = transOutAngle + self.surfaceAngle
        actualOutAngle += self.stickPosition[0] * math.pi / 3
        ball.unitVelocity[0] = math.cos(actualOutAngle)
        ball.unitVelocity[1] = math.sin(actualOutAngle)
        if self.stickPosition[1] < -0.1:
            ball.speed += -self.stickPosition[1] * self.speed

    def triggerPressed(self):
        if self.joystick.get_button(5): #right trigger on an XBox controller
            self.lastTriggerTime = time.perf_counter()


    def grabBall(self,ball):
        if ball.isGrabbed:
            vecNorm = math.sqrt(self.joystick.get_axis(2)**2 + self.joystick.get_axis(3)**2) + 0.0000000001
            ball.velocity = [self.joystick.get_axis(2) / vecNorm, self.joystick.get_axis(3) / vecNorm]
            if not self.joystick.get_button(5):#time.time_ns() - self.grabTime > 1e9:
                ball.isGrabbed = False
        if abs(self.lastTriggerTime - self.lastHitTime) < Constant.TRIGGER_TOLERANCE:
            ball.isGrabbed = True
            self.grabTime = time.perf_counter()

    def impact(self,ball):
        if ball.isGrabbed:
            self.lastHitTime = time.perf_counter()
        elif ball.lastHitObject != id(self):
            self.lastHitTime = time.perf_counter()
            ball.lastHitObject = id(self)
            self.reflect(ball)


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



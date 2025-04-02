import pygame as pg
import numpy as np
from constant import Constant



class Ball():

    returnSpeed = float(Constant.SCREEN_HEIGHT / 2e9)

    def __init__(self,position, velocity, speed, radius=1, color=(255,255,255)):
        self.radius = radius
        self.color = color
        self.unitVelocity = np.array(velocity) #unit direction the ball is traveling
        self.position = np.array(position)
        self.speed = speed #scalar
        self.isGrabbed = False
        self.lastHitObject = int(-1)
        self.lastHitTime = None
        self.returnSpeed = speed



    def draw(self, image):
        pg.draw.circle(image, self.color, (self.position[0], self.position[1]), self.radius)
        if self.isGrabbed:
            pg.draw.line(image, (0, 255, 0), self.position, [self.position[0] + self.speed * self.unitVelocity[0] * 0.1e9, self.position[1] + self.speed * self.unitVelocity[1] * 0.1e9], 1)

    def updatePosition(self,time): #moves the ball according to it's velocity
        self.position[0] += self.unitVelocity[0] * self.speed * time
        self.position[1] += self.unitVelocity[1] * self.speed * time
        if self.speed > self.returnSpeed or self.speed < self.returnSpeed:
            self.speed -= (self.speed - self.returnSpeed) * time / 2e9

    def reset(self):
        self.position = [Constant.SCREEN_WIDTH / 2, Constant.SCREEN_HEIGHT / 2]
        self.speed = self.returnSpeed
        self.unitVelocity = [0, 1]

    def move(self,time, player):
        if not self.isGrabbed:
            self.updatePosition(time)
        else:
            self.position[0] = player.leftEndpoint[0] + player.length / 2
            self.position[1] = player.leftEndpoint[1]


    def getTrajectory(self):
        ballX = lambda dt: self.position[0] + self.speed * self.unitVelocity[0] * dt
        ballY = lambda dt: self.position[1] + self.speed * self.unitVelocity[1] * dt
        return [ballX, ballY]
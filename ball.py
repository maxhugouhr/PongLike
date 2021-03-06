import pygame as pg
from constants import Constant


class Ball():

    returnVelocity = float(Constant.SCREEN_HEIGHT / 2e9)

    def __init__(self,position, speed, magnitude, radius=1, color=(255,255,255)):
        self.radius = radius
        self.color = color
        self.velocity = speed #unit direction the ball is traveling
        self.position = position
        self.velocMag = magnitude #magnitude of the velocity in pixels per nanosecond
        self.isGrabbed = False
        self.lastHitObject = int(-1)


    def draw(self,img):
        pg.draw.circle(img, self.color, (self.position[0], self.position[1]), self.radius)
        if self.isGrabbed:
            pg.draw.line(img, (0,255,0), self.position, [self.position[0]+self.velocMag*self.velocity[0]*0.1e9, self.position[1]+self.velocMag*self.velocity[1]*0.1e9],1)

    def updatePosition(self,time): #moves the ball according to it's velocity
        self.position[0] += self.velocity[0] * self.velocMag * time
        self.position[1] += self.velocity[1] * self.velocMag * time
        if self.velocMag > self.returnVelocity or self.velocMag < self.returnVelocity:
            self.velocMag -= (self.velocMag - self.returnVelocity) * time / 2e9

    def reset(self):
        self.position = [Constant.SCREEN_WIDTH / 2, Constant.SCREEN_HEIGHT / 2]
        self.velocMag = self.returnVelocity
        self.velocity = [0,1]

    def move(self,time, player):
        if not self.isGrabbed:
            self.updatePosition(time)
        else:
            self.position[0] = player.leftEndpoint[0] + player.length / 2
            self.position[1] = player.leftEndpoint[1]

    def getTrajectory(self):
        ballX = lambda dt: self.position[0] + self.velocMag*self.velocity[0]*dt
        ballY = lambda dt: self.position[1] + self.velocMag*self.velocity[1]*dt
        return [ballX, ballY]
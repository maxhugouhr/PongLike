from surfaceToChange import Surface
from constant import Constant
import random as rand
import math

class Enemy(Surface):

    returnVelocity = [float(Constant.SCREEN_WIDTH/3e9),float(Constant.SCREEN_WIDTH/3e9)]

    def __init__(self, speed, leftEnd, rightEnd, color, width, reflector, speedMultiplier, deflectionAngle):
        super().__init__(speed, leftEnd, rightEnd, color, width, reflector, speedMultiplier, deflectionAngle)
        self.level = 0
        self.randomAngle = False
        self.velocity = self.returnVelocity
        self.length = Constant.SCREEN_WIDTH / 5
        self.rightEndpoint[0] = self.leftEndpoint[0] + self.length

    def reset(self):
        self.velocity = self.returnVelocity
        self.speedMultiplier = 1
        self.leftEndpoint[0] = Constant.SCREEN_WIDTH/2 - self.length/2
        self.rightEndpoint[0] = self.leftEndpoint[0] + self.length

    def move(self,ball,time):
        if self.level == 0 or self.level == 1:
            self.trackBall(ball,time)
        self.keepBounds()

    def keepBounds(self):
        if self.leftEndpoint[0] < 0:
            self.leftEndpoint[0] = 0
            self.rightEndpoint[0] = self.length
        if self.rightEndpoint[0] > Constant.SCREEN_WIDTH:
            self.rightEndpoint[0] = Constant.SCREEN_WIDTH
            self.leftEndpoint[0] = Constant.SCREEN_WIDTH - self.length

    def trackBall(self,ball,time):
        midpoint = self.leftEndpoint[0] + self.length / 2
        if ball.position[0] > midpoint:
            self.leftEndpoint[0] += self.velocity[0] * time
            self.rightEndpoint[0] += self.velocity[0] * time
        elif ball.position[0] < midpoint:
            self.leftEndpoint[0] -= self.velocity[0] * time
            self.rightEndpoint[0] -= self.velocity[0] * time

    def reflectRandom(self,ball):
        rand.seed()
        ballAngle = float(math.atan2(ball.velocity[1], ball.velocity[0]))  # angle with respect to the x axis
        flatBallAngle = ballAngle - self.surfaceAngle
        refTransBallVeloc = (math.cos(flatBallAngle), -math.sin(flatBallAngle))
        transOutAngle = math.atan2(refTransBallVeloc[1], refTransBallVeloc[0])
        actualOutAngle = transOutAngle + self.surfaceAngle
        actualOutAngle += rand.choice([-1,1]) * (math.pi / 4) * rand.random()
        ball.velocity[0] = math.cos(actualOutAngle)
        ball.velocity[1] = math.sin(actualOutAngle)
        ball.speed *= self.speedMultiplier
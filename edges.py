from surface import Surface
from constants import Constant
import time

class Edge(Surface):

    def __init__(self, speed, leftEnd, rightEnd , color, width,reflector,speedMultiplier,defAngle):
        super().__init__(speed,leftEnd, rightEnd, color, width, reflector, speedMultiplier, defAngle)
        self.isTeleporter = False
        self.twin = Surface()


    def impact(self,ball):
        if ball.lastHitObject != id(self): #ensures the ball can't bounce twice off the same surface
            self.lastHitTime = time.time_ns()
            ball.lastHitObject = id(self)
            if self.isTeleporter:
                self.teleport(ball)
            else:
                self.reflect(ball)

    def teleport(self,ball):
        fraction = (ball.position[1] - self.leftEndpoint[1]) / self.length
        ball.position[0] = self.twin.leftEndpoint[0]
        ball.position[1] = fraction * self.twin.length + self.twin.leftEndpoint[1]
        ball.lastHitObject = id(self.twin)


    def makeTeleporter(self, twin):
        self.isTeleporter = True
        twin.isTeleporter = True
        self.twin = twin
        twin.twin = self
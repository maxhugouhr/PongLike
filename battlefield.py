from surfaceToChange import Surface
from ball import Ball
from player import Player
from constant import Constant
from enemy import Enemy
from edges import Edge


class Battlefield():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surfaces = []
        self.ball = Ball([int(100),int(100)], [float(0.5),float(0.5)], float(self.height/(2e9)), 5, (255,255,255))
        self.player = Player([float(Constant.SCREEN_WIDTH/1e9),float(Constant.SCREEN_WIDTH/1e9)], [Constant.SCREEN_WIDTH/2,Constant.SCREEN_HEIGHT - 100], [Constant.SCREEN_WIDTH/2 + 75,Constant.SCREEN_HEIGHT - 100], (0,0,255), 5, True,1.5,0)
        self.level = 0
        self.enemy = Enemy([float(Constant.SCREEN_WIDTH/1e9),float(Constant.SCREEN_WIDTH/1e9)], [Constant.SCREEN_WIDTH/2,100], [Constant.SCREEN_WIDTH/2 + 75,100], (255,0,0), 5, True,1,0)

    def addEdges(self):

        leftSurface = Surface([0,0],[0,0],[0, self.height],(255,255,255),0,True,1,0)
        rightSurface = Surface([0, 0],[self.width,0], [self.width,self.height], (255, 255, 255), 0, True, 1,0)
        topSurface = Surface([0,0], [0,0], [self.width,0], (255,255,255),3,True,1,0)
        bottomSurface = Surface([0, 0], [0, self.height], [self.width, self.height], (255, 255, 255), 3, True, 1, 0)
        self.surfaces.append(leftSurface)
        self.surfaces.append(rightSurface)
        self.surfaces.append(topSurface)
        self.surfaces.append(bottomSurface)

    def draw(self,img):
        for surf in self.surfaces:
            surf.draw(img)
        self.player.draw(img)
        self.ball.draw(img)
        self.enemy.draw(img)

    def moveAll(self,currentLoopTime, previousLoopTime):
        for surf in self.surfaces:
            surf.move(currentLoopTime - previousLoopTime)
        self.player.move(currentLoopTime - previousLoopTime)
        self.enemy.move(self.ball, currentLoopTime - previousLoopTime)
        self.ball.move(currentLoopTime - previousLoopTime, self.player)


    def checkHitboxes(self):
        for surf in self.surfaces:
            surf.checkHit(self.ball)
        self.player.checkHit(self.ball)
        self.enemy.checkHit(self.ball)
        self.player.grabBall(self.ball)

    def checkWinConditions(self):
        if self.ball.position[1] < -5:
            self.level += 1
            return 1
        if self.ball.position[1] > self.height + 5:
            print("you made it to level: ", self.level)
            exit()
        return 0

    def reset(self):
        self.surfaces.clear()
        self.ball.reset()
        self.player.reset()
        self.enemy.reset()

    def initializeLevel(self):
        if self.level == 0:
            self.initializeLevelZero()


    def initializeLevelZero(self):
        self.reset()
        leftEdge = Edge([0,0],[0,0],[0, self.height],(255,255,255),2,True,1,0)
        rightEdge = Edge([0, 0],[self.width - 2,0], [self.width - 2,self.height], (255, 255, 255), 2, True, 1,0)
        self.surfaces.append(leftEdge)
        self.surfaces.append(rightEdge)
        self.enemy.velocity = [float(Constant.SCREEN_WIDTH / 3e9), float(0)]



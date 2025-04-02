from reflector import Reflector
from ball import Ball
from player import Player
from constant import Constant
from enemy import Enemy


class Battlefield():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surfaces = []
        self.ball = Ball([int(100),int(100)], [float(0.5),float(0.5)], 0.0000015, 5, (255,255,255))
        self.player = Player(float(Constant.SCREEN_WIDTH/1e9), [Constant.SCREEN_WIDTH/2,Constant.SCREEN_HEIGHT - 100], [Constant.SCREEN_WIDTH/2 + 75,Constant.SCREEN_HEIGHT - 100], (0,0,255), 5)
        self.level = 0
        # self.enemy = Enemy([float(Constant.SCREEN_WIDTH/1e9),float(Constant.SCREEN_WIDTH/1e9)], [Constant.SCREEN_WIDTH/2,100], [Constant.SCREEN_WIDTH/2 + 75,100], (255,0,0), 5, True,1,0)

    def addEdges(self):

        leftSurface = Reflector([0,0],[0,self.height],(255,255,255),0)
        rightSurface = Reflector([self.width, 0],[self.width,self.height], (255, 255, 255), 0)
        topSurface = Reflector([0,0], [self.width,0],  (255,255,255),0)
        bottomSurface = Reflector([0, self.height], [self.width, self.height],(255, 255, 255), 0)
        self.surfaces.append(leftSurface)
        self.surfaces.append(rightSurface)
        self.surfaces.append(topSurface)
        self.surfaces.append(bottomSurface)

    def draw(self,img):
        for surf in self.surfaces:
            surf.draw(img)
        self.player.draw(img)
        self.ball.draw(img)
        #self.enemy.draw(img)

    def moveAll(self,currentLoopTime, previousLoopTime):
        for surf in self.surfaces:
            surf.move(currentLoopTime - previousLoopTime)
        self.player.move(currentLoopTime - previousLoopTime)
        #self.enemy.move(currentLoopTime - previousLoopTime)
        self.ball.move(currentLoopTime - previousLoopTime, self.player)


    def checkHitboxes(self):
        for surf in self.surfaces:
            surf.checkHit(self.ball)
        self.player.checkHit(self.ball)
        #self.enemy.checkHit(self.ball)
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
        #self.enemy.reset()

    def initializeLevel(self):
        if self.level == 0:
            self.initializeLevelZero()


    def initializeLevelZero(self):
        self.addEdges()



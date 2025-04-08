import threading
import time
from constant import Constant

class GameClock():

    def __init__(self, graphicsFrameRate, physicsFrameRate):
        self.graphicsFrameRate =graphicsFrameRate
        self.physicsFrameRate = physicsFrameRate
        self.graphicsFrameTime = 1.0 / self.graphicsFrameRate
        self.physicsFrameTime = 1.0 / self.physicsFrameRate

        self.physicsIsRunning = False
        self.graphicsIsRunning = False

        self.physicsThread = None
        self.graphicsThread = None

        self.callPhysicsEngine = None
        self.callGraphicsEngine = None

        self.physicsTime = 0.0
        self.graphicsTime = 0.0

    def setPhysicsEngine(self, physicsEngine):
        self.callPhysicsEngine = physicsEngine

    def setGraphicsEngine(self,graphicsEngine):
        self.callGraphicsEngine = graphicsEngine

    def physicsLoop(self):
        lastTime = time.perf_counter()

        while self.physicsIsRunning:
            currentTime = time.perf_counter()
            elapsedTime = currentTime - lastTime
            if elapsedTime >= self.physicsFrameTime:
                self.physicsTime += elapsedTime
                if self.callPhysicsEngine:
                    self.callPhysicsEngine(elapsedTime)
                lastTime = currentTime
            else:
                time.sleep(0.001)

    def graphicsLoop(self):
        lastTime = time.perf_counter()

        while self.graphicsIsRunning:
            currentTime = time.perf_counter()
            elapsedTime = currentTime - lastTime
            if elapsedTime >= self.graphicsFrameTime:
                self.graphicsTime += elapsedTime
                if self.callGraphicsEngine:
                    self.callGraphicsEngine()
                lastTime = currentTime
            else:
                time.sleep(0.001)


    def startPhysics(self):
        if not self.physicsIsRunning:
            self.physicsIsRunning = True
            self.physicsThread = threading.Thread(target=self.physicsLoop())
            self.physicsThread.daemon = True
            self.physicsThread.start()

    def stopPhysics(self):
        self.physicsIsRunning = False
        if self.physicsThread:
            self.physicsThread.join()


    def startGraphics(self):
        if not self.graphicsIsRunning:
            self.graphicsIsRunning = True
            self.graphicsThread = threading.Thread(target=self.graphicsLoop())
            self.graphicsThread.daemon = True
            self.graphicsThread.start()

    def stopGraphics(self):
        self.graphicsIsRunning = False
        if self.graphicsThread:
            self.graphicsThread.join()

    def start(self):
        self.startPhysics()
        self.startGraphics()

    def stop(self):
        self.stopPhysics()
        self.stopGraphics()



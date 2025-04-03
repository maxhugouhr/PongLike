import time
from constant import Constant

class GameClock():

    def __init__(self, desiredFrameRate, physicsPerFrame):
        self.desiredFrameRate = desiredFrameRate
        self.lastFrameEndTime = time.perf_counter()
        self.desiredFrameTime = int(1 / self.desiredFrameRate)
        self.physicsUpdatesPerFrame = physicsPerFrame
        self.desiredPhysicsTime = int(self.desiredFrameTime / self.physicsUpdatesPerFrame)


    def sync(self):
        currentTime = time.perf_counter()
        elapsedTime = currentTime - self.lastFrameEndTime
        targetNextFrameTime = currentTime + self.desiredFrameTime
        sleepTime = targetNextFrameTime - currentTime

        if sleepTime > Constant.SLEEP_TOLERANCE:
            time.sleep(sleepTime)


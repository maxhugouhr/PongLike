

class PhysicsEngine():

    def __init__(self, entitiesList, ball):
        self.physicsEntitiesList = entitiesList
        self.ball = ball

    def move(self,timeStep):
        for entity in self.physicsEntitiesList:
            entity.move(timeStep)

    def checkHit(self):
        for entity in self.physicsEntitiesList:
            entity.checkHit(self.ball)

    def callEngine(self,timeStep):
        self.move(timeStep)
        self.checkHit()
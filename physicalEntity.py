from abc import ABC, abstractmethod

class PhysicalEntity(ABC):

    @abstractmethod
    def move(self, time):
        pass

    @abstractmethod
    def checkHit(self,otherSurface):
        pass

    @abstractmethod
    def impact(self,otherSurface):
        pass
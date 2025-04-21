from abc import ABC, abstractmethod

class PhysicalEntity(ABC):

    @abstractmethod
    def move(self, time):
        pass

    @abstractmethod
    def checkHit(self,ball):
        pass

    @abstractmethod
    def impact(self,ball):
        pass
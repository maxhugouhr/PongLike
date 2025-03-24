from abc import ABC, abstractmethod, abstractproperty

class Surface(ABC):

    @abstractmethod
    def draw(self, image):
        pass

    @abstractmethod
    def move(self,time):
        pass

    @abstractmethod
    def impact(self,ball):
        pass

    @abstractmethod
    def checkHit(self,ball):
        pass
from abc import ABC, abstractmethod, abstractproperty

class gamePiece(ABC):

    @abstractmethod
    def draw(self, image):
        pass

    @abstractmethod
    def move(self, *args):
        pass


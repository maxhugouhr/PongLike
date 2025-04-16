from abc import ABC, abstractmethod

class GraphicalEntity(ABC):

    @abstractmethod
    def draw(self, imageToDraw, otherEntity):
        pass

class GraphicsEngine():

    def __init__(self, graphicsEntities,image):
        self.graphicsEntitiesList = graphicsEntities
        self.image = image

    def __call__(self):
        for entity in self.graphicsEntitiesList:
            entity.draw(self.image)
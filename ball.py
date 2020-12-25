from point import Point
import cv2 as cv

class Ball(Point):
    def __init__(self, speed=np.array((0.0,0.0)), position=np.array((0.0,0.0)),facing=0, radius=1, color=(255,255,255)):
        super(speed, position, facing)
        self.radius = radius
        self.color = color

    def draw(self,img):
        pg.draw.circle(img, self.color, (self.pos[0], self.pos[1]), self.radius)
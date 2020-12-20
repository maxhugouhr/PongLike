from point import Point
import cv2 as cv

class Ball(Point):
    def __init__(self, speed=np.array((0.0,0.0)), position=np.array((0.0,0.0)),facing=0, radius=1, color=(255,255,255)):
        super(speed, position, facing)
        self.radius = radius
        self.color = color

    def draw(self,img):
        cv.circle(img,self.pos,self.radius,self.color)
from surface import Surface

class Enemy(Surface):

    def __init__(self, speed, leftEnd, rightEnd , color, width,reflector,speedMultiplier,defAngle):
        super().__init__(speed,leftEnd, rightEnd, color, width, reflector, speedMultiplier, defAngle)
        self.level = 0
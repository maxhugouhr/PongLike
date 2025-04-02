import numpy as np

def reflectedAngle(ballVelocity, surfacePoint1, surfacePoint2):
    lineDirection = surfacePoint2 - surfacePoint1
    normalVector = np.array([-lineDirection[1], lineDirection[0]])
    normalVector = normalVector / np.linalg.norm(normalVector)
    dot = np.dot(ballVelocity, normalVector)
    reflectedVelocity = ballVelocity - 2*dot*normalVector
    reflectedVelocity = reflectedVelocity / np.linalg.norm(reflectedVelocity)
    return reflectedVelocity
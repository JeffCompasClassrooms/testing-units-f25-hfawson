import math

class Circle:

    def __init__(self, radius):
        if radius >= 0:    
            self.mRadius = radius
        else:
            self.mRadius = 0
        return

    def getRadius(self):
        return self.mRadius

    def setRadius(self, radius):
        if radius >= 0.0:
            self.mRadius = radius
            return True
        else:
            return False

    def getArea(self):
        return math.pi * self.mRadius * self.mRadius

    def getCircumference(self):
        return 2 * math.pi * self.mRadius

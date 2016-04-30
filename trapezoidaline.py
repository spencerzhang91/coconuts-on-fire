import math

class Circle:
    """
    A circle class.
    """
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def __repr__(self):
        return "(%f %f %f)" % (x, y, r)

def findPQ(c1: Circle, c2: Circle)->list:
    """
    This function finds the P point and Q point of two circles.
    """
    sin_alpha = (c1.r - c2.r) / oDist(c1, c2)
    cos_alpha = math.sqrt(oDist(c1, c2) - (c1.r - c2.r)**2) / oDist(c1, c2)
    sin_theta = (c1.y - c2.y) / oDist(c1, c2)
    cos_theta = (c1.x - c2.x) / oDist(c1, c2)


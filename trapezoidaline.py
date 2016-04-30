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
        return "(%f %f %f)" % (self.x, self.y, self.r)

class Point:
    """
    A point class
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "(%f, %f)" % (self.x, self.y)

def findTrapezoid(c1: Circle, c2: Circle)->list:
    """
    This function finds the trapezoid vertices of two circles.
    The line o1o2 is Ax + By + C = 0 (o1 and o2 are center of c1 and c2)

    """
    sin_a = (c1.r - c2.r) / oDist(c1, c2)
    cos_a = math.sqrt(oDist(c1, c2) - (c1.r - c2.r)**2) / oDist(c1, c2)
    sin_t = (c1.y - c2.y) / oDist(c1, c2)
    cos_t = (c1.x - c2.x) / oDist(c1, c2)
    A = sin_t / cos_t
    B = -1
    C = c1.y - A * c1.x

    # pc1, pc2, pc3, pc4 are vertex of the trapezoid we want.
    # And pc1 & pc3, pc2 & pc4 are symetric about line o1o2
    pc1 = Point(c1.r * (sin_a * cos_t + cos_a * sin_t),
                c1.r * (cos_a * cos_t - sin_a * sin_t))

    pc2 = Point(c2.r * (sin_a * cos_t + cos_a * sin_t),
                c2.r * (cos_a * cos_t - sin_a * sin_t))

    pc3 = symPoint(pc1, A, B, C)
    pc4 = symPoint(pc2, A, B, C) # just want to be simple and lazy here...
    return (pc1, pc2, pc3, pc4)

def drawTrapezoidalLine(v1:Point, v2:Point, v3:Point, v4:Point)->None:
    """
    This function actually draws the trapezoidal line.
    """
    raise NotImplementedError


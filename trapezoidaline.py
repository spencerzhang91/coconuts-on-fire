class Point:
    """
    A point class.
    """
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def __repr__(self):
        return "(%f %f %f)" % (x, y, r)

def findPQ(circle1: Circle, circle2: Circle)->list:
    """
    This function finds the P point and Q point of two circles.
    """
    pass
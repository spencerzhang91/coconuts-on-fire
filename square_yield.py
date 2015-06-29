# file squares_yield.py

class Squares:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        for value in range(self.start, self.stop+1):
            yield value ** 2

if __name__ == '__main__':
    S = Squares(1,5)
    for i in S:
        for j in S:
            print("%s:%s" % (i,j), end=' ')

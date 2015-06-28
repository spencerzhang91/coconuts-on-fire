# file squares_yield.py

class Squares:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        for value in range(self.start, self.stop+1):
            yield value ** 2

if __name__ == '__main__':
    for i in Squares(1,5):
        print(i, end=' ')

    

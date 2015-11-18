# file squares.py

class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        #self.value = 0
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2

if __name__ == '__main__':
    S = Squares(1,5)
    #Q = Squares(1,5)
    for i in S:
        for j in S:
            print("%s:%s" % (i,j), end=' ')

# This file along with three other file that starts with 'squares' in their file
# name is very helpful for understanding how iteration's working in operator
# overloading context.

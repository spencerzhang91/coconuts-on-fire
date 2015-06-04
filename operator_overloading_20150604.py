# file number.py -- operator overloading

class Number:
    def __init__(self, start):
        self.value = start

    def __sub__(self, other):
        return Number(self.value - other)

x = Number(5)
y = x -2
print(y.value)

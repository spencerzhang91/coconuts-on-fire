class Commuter1:
    def __init__(self, val):
        self.value = val

    def __add__(self, other):
        print('add#1', self.value, other)
        return self.value + other

    def __radd__(self, other):
        print('radd', self.value, other)
        #return other + self.value --seem equivalent to below
        return self.value + other

class Commuter2:
    def __init__(self, val):
        self.value = val

    def __add__(self, other):
        print('add#2', self.value, other)
        return self.value + other

    def __radd__(self, other):
        return self.__add__(other)

class Commuter3:
    def __init__(self, val):
        self.value = val

    def __add__(self, other):
        print('add#3', self.value, other)
        return self.value + other

    def __radd__(self, other):
        return self + other

class Commuter4:
    def __init__(self, val):
        self.value = val

    def __add__(self, other):
        print("add#4", self.value, other)
        return self.value + other
    # In fact, there's no need to define a __radd__, just share existing __add__ would do:
    __radd__ = __add__ 

class Commuter5:
    def __init__(self, val):
        self.value = val

    def __add__(self, other):
        if isinstance(other, Commuter5):
            other = other.value
        return Commuter5(self.value + other)

    def __radd__(self, other):
        return self.__add__(other)

    def __str__(self):
        return '<Commuter5: %s>' % self.value

# to find out why 3 is equivalent to 2
class Commuter6:
    def __init__(self, val):
        self.value = val

    def __add__(self, other):
        print("add#6", self.value, other)
        return self

    __radd__ = __add__

if __name__ == "__main__":
    for klass in (Commuter1, Commuter2, Commuter3, Commuter4, Commuter5, Commuter6):
        print('-'*60)
        x = klass(88)
        y = klass(99)
        print(x + 1)
        print(1 + y)
        print(x + y)

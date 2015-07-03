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
        print('add#3', self.value + other)
        return self.value + other

    def __radd__(self, other):
        return self + other



if __name__ == "__main__":
    x = Commuter1(10)
    y = Commuter1(88)
    #
    print(x + 5)
    print(5 + y)

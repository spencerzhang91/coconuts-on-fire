class Commuter1:
    def __init__(self, val):
        self.value = val

    def __add__(self, other):
        print('add', self.value, other)
        return self.value + other

    def __radd__(self, other):
        print('radd', self.value, other)
        return other + self.value

if __name__ == "__main__":
    x = Commuter1()

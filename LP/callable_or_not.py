class Prod:
    def __init__(self, value):
        self.value = value

    def __call__(self, other):
        return self.value * other

class Prod2:
    def __init__(self, value):
        self.value = value

    def comp(self, other):
        return self.value * other



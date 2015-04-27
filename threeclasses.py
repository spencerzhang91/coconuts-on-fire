class Firstclass:
    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)


class Secondclass(Firstclass):
    def display(self):
        print('Current value = "%s"' % self.data)


class Thirdclass(Secondclass):
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return Thirdclass(self.data + other)

    def __str__(self):
        return '[Thirdclass: %s]' % self.data

    def mul(self, other):
        self.data *= other


def uppername(obj):
    return obj.name.upper()


a = Thirdclass('abc')

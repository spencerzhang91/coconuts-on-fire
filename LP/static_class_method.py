# Test code for understanding the difference between instance method, static
# method and class method.
class Methods:
    numInstances = 0
    def __init__(self):
        Methods.numInstances += 1

    def print1(self):
        print('Instance method: %d' % Methods.numInstances)

    def print2():
        print("Normal instanceless method: %d" % Methods.numInstances)

    @staticmethod
    def print3():
        print('Static method: %d' % Methods.numInstances)

    def print4(cls):
        print('Class method: %d' % Methods.numInstances)

    print4 = classmethod(print4)

if __name__ == '__main__':

    a = Methods()
    b = Methods()
    c = Methods()

    a.print1()
    Methods.print2()
    c.print3()
    c.print4()



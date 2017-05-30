# Test code for understanding the difference between instance method, static
# method and class method.
class Spam:
    numInstances = 0
    def __init__(self):
        self.count()

    def count(cls):
        cls.numInstances += 1
    count = classmethod(count)

    def print1(self):
        print('Instance method: %d' % Spam.numInstances)

    def print2():
        print("Normal instanceless method: %d" % Spam.numInstances)

    @staticmethod
    def print3():
        print('Static method: %d' % Spam.numInstances)

    def print4(cls):
        print('Number of instances: %s %s' % (cls.numInstances, cls))

    print4 = classmethod(print4)

class Sub(Spam):
    def print4(cls):
        print('Extra stuff...', cls)
        Spam.print4()
    print4 = classmethod(print4)

class Other(Spam):
    numInstances = 0
    def __init__(self):
        Other.numInstances += 1

if __name__ == '__main__':

    x = Sub()
    y = Spam()
    # test calls below:
    print(x.numInstances, y.numInstances, Sub.numInstances)
    y.print4()
    x.print4()
"""
Extra stuff... <class '__main__.Sub'>
Number of instances: 2 <class '__main__.Spam'>
Extra stuff... <class '__main__.Sub'>
Number of instances: 2 <class '__main__.Spam'>
Number of instances: 2 <class '__main__.Spam'>
Number of instances: 1 <class '__main__.Other'>
"""

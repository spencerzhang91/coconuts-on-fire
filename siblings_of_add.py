class Adder:
    def __init__(self, value=0):
        self.data = value

    def __add__(self, other):
        return self.data + other


if __name__ == '__main__':
    x = Adder(5)
    x = x + 2
    print(x)
    x = 2 + x
    print(x)

    
# this piece of code reviews that in python the __add__ method can not handle addition operation when
# when the instance is on the right side of the operand.
# Have to copy and paste the code to the shell instead of directly run here to observe the outcome.

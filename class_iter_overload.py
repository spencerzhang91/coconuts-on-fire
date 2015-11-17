class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        else:
            self.value += 1
            return self.value ** 2

if __name__ == '__main__':
    x = Squares(1, 10)
    for i in x:
        print(i)


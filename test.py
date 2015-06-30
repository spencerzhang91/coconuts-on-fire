class Itera:
    def __init__(self, wrapped):
        self.value = wrapped

    def __iter__(self):
        self.offset = 0
        return self

    def __next__(self):
        if self.offset >= len(self.value):
            raise StopIteration
        item = self.value[self.offset]
        self.offset += 1
        return item

test = Itera('abcdefg')
for i in range(3):
    for item in test:
        print("%s" % item)

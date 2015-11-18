class Indexer:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

if __name__ == '__main__':
    test = Indexer([1,2,3,4,5])
    print(test[3])
    test[3] = 100
    print(test[3])

    print(test[1:3])
    
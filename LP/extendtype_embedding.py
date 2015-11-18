'''
form L.P. page 980
'''
class Set:
    def __init__(self, value = []):
        self.data = []
        self.concat(value)

    def intersect(self, other):
        res = []
        for x in self.data:
            if x in other:
                res.append(x)
        return Set(res)

    def union(self, other):
        res = self.data[:]                 # copy of my list
        for x in other:
            if x not in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:
            if x not in self.data:
                self.data.append(x)

    def __len__(self):
        return len(self.data)              # len(self), if self
    def __getitem__(self, key):
        return self.data[key]              # self[i], self[i:j]
    def __and__(self, other):
        return self.intersect(other)
    def __or__(self, other):
        return self.union(other)
    def __repr__(self):
        return 'Set:' + repr(self.data)    # print(self)...
    def __iter__(self):
        return iter(self.data)             # for x in self...

if __name__ == '__main__':
    x = Set([1,2,3,4])
    print(x)
    print(x.union(Set([3,4,5])))
    print(x | Set([22,3]))


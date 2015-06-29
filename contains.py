# file contains.py of Learing Python(5th Edition) P907

class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, i):
        print('get[%s]:' % i, end=' ')
        return self.data[i]

    def __iter__(self):
        print('iter=> ', end=' ')
        self.ix = 0
        return self

    def __next__(self):
        print('next:', end=' ')
        if self.ix == len(self.data):
            raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

    def __contains__(self, x):
        print('contains: ', end=' ')
        return x in self.data
        

if __name__ == '__main__':
    X = Iters([1,2,3,4,5])
    print(1 in X)
    
    for i in X:
        print(i, end=' | ')
    print()
    print([i ** 2 for i in X])
    print(list(map(bin, X)))

    I = iter(X)
    while True:
        try:
            print(next(I), end=' @ ')
        except StopIteration:
            break
    print()
    print(X[:-1], end='\n')
    

    

# Below is the outcome of test code and explanations
'''
[1] contains:  True
[2] iter=>  next: 1 | next: 2 | next: 3 | next: 4 | next: 5 | next: 
[3] iter=>  next: next: next: next: next: next: [1, 4, 9, 16, 25]
[4] iter=>  next: next: next: next: next: next: ['0b1', '0b10', '0b11', '0b100', '0b101']
[5] iter=>  next: 1 @ next: 2 @ next: 3 @ next: 4 @ next: 5 @ next: 
[6] get[slice(None, -1, None)]: [1, 2, 3, 4]

In line [1], which is the result of "print(1 in X)", shows that the membership check first uses
method "__contains__". However when comment this method out, then comes the "__iter__" and "__next__"
method.

In line [2], which is the result of the code from line 33 and line 34, indicates that as for "for"
statement, the "__iter__" has priority over "__contains__". It is not saying that in this case the
membership is not practised, but just not printed.
'''

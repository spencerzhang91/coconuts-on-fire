class Vector:
    def __init__(self, x, y):
        self.vertax = [x, y]

    def __getitem__(self, index):
        return self.vertax[index]

    def __setitem__(self, index, value):
        self.vertax[index] = value
        
    def __add__(self, other):
        return Vector(self.vertax[0] + other[0], self.vertax[1] + other[1])

    def __repr__(self):
        return str(self.vertax)


a = Vector(1,1)
b = Vector(2,1)
print(a[0])
print(a)
print(b)
c = a + [3,3]
print(c)
print(type(c))
d = c + a
print(d)
a[1] = 3
print(a)
    

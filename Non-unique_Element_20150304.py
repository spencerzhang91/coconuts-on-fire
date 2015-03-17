def select(data):
    new = []
    for item in data:
        if data.count(item) > 1:
            new.append(item)
    return new

tl = [1,2,3,3,4,4,5,5,5,6,7,7,8,9,9]
a = select(tl)
print(a)

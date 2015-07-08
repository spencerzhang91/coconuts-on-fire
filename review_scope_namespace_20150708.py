class Alter1:
    def half(self, array, k):
        print('A1: before:', array)
        # array = array[k:] + array[:k]
        temp = array[2:3]
        array = temp
        print('A1: after:', array, '\n')
        

class Alter2:
    def half(self, array, k):
        print('A2: array:', array)
        temp = array[k:] + array[:k]
        print('A2: temp:', temp)
        for i in range(len(array)):
            array[i] = temp[i]
        print('A2: array:', array, '\n')
        

l1 = [1,2,3,4]
l2 = [5,6,7,8]
l3 = [11,22,33,44]
l4 = [55,66,77,88]

test1 = Alter1()
test2 = Alter2()
test3 = Alter1
tobj3 = Alter1()
test4 = Alter2
tobj4 = Alter2()

f1 = test1.half
f2 = test2.half
f3 = test3.half
f4 = test4.half

print(type(f1), type(f2), type(f3), type(f4))
f1(l1, 2)
f2(l2, 2)
f3(tobj3, l3, 2)
f4(tobj4, l4, 2)

print('f1 ->', l1)
print('f2 ->', l2)
print('f3 ->', l3)
print('f4 ->', l4)


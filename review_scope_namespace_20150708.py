class Alter1:
    def half(self, array, k):
        array = array[k:] + array[:k]      
        print('l1 inside function:', id(array))
        

class Alter2:
    def half(self, array, k):
        temp = array[k:] + array[:k]
        
        for i in range(len(array)):
            array[i] = temp[i]
        print('l2 inside function:', id(array))


        
l1 = [1,2,3,4]
l2 = [5,6,7,8]

print('l1 Before alter:', l1, '; l1 id outside function call:', id(l1))
print('l2 Before alter:', l2, '; l2 id outside function call:', id(l2))
print('\n')
test1 = Alter1()
test2 = Alter2()

f1 = test1.half
f2 = test2.half

f1(l1, 2)
f2(l2, 2)
print('*' * 20, '\n')
print('l1 after alter:', l1)
print('l2 after alter:', l2)


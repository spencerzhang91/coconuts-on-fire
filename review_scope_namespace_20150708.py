class Alter1:
    def half(self, array, k):
        array = array[k:] + array[:k]      
        print('l1 inside function:', id(array))
        

class Alter1_1:
    def half(self, array, k):
        # global l3
        l3 = array[k:] + array[:k]
        print('l3 inside fucntion:', id(l3))

class Alter2:
    def half(self, array, k):
        temp = array[k:] + array[:k]
        
        for i in range(len(array)):
            array[i] = temp[i]
        print('l2 inside function:', id(array))


        
l1 = [1,2,3,4]
l2 = [5,6,7,8]
l3 = [9,10,11,12]

print('l1 Before alter:', l1, '; l1 id outside function call:', id(l1))
print('l2 Before alter:', l2, '; l2 id outside function call:', id(l2))
print('l3 Before alter:', l3, '; l3 id outside function call:', id(l3))
print('\n')
test1 = Alter1()
test2 = Alter2()
test1_1 = Alter1_1()

f1 = test1.half
f2 = test2.half
f1_1 = test1_1.half

f1(l1, 2)
f2(l2, 2)
f1_1(l3, 2)
print('*' * 20, '\n')
print('l1 after alter:', l1)
print('l2 after alter:', l2)
print('l3 after alter:', l3)


'''
l1 Before alter: [1, 2, 3, 4] ; l1 id outside function call: 5082504
l2 Before alter: [5, 6, 7, 8] ; l2 id outside function call: 54924872
l3 Before alter: [9, 10, 11, 12] ; l3 id outside function call: 54921544


l1 inside function: 54914056
l2 inside function: 54924872
l3 inside fucntion: 54919560
******************** 

l1 after alter: [1, 2, 3, 4]
l2 after alter: [7, 8, 5, 6]
l3 after alter: [9, 10, 11, 12]
>>> ================================ RESTART ================================
>>> 
l1 Before alter: [1, 2, 3, 4] ; l1 id outside function call: 35622280
l2 Before alter: [5, 6, 7, 8] ; l2 id outside function call: 55614088
l3 Before alter: [9, 10, 11, 12] ; l3 id outside function call: 54984776


l1 inside function: 54993928
l2 inside function: 55614088
l3 inside fucntion: 54985736
******************** 

l1 after alter: [1, 2, 3, 4]
l2 after alter: [7, 8, 5, 6]
l3 after alter: [11, 12, 9, 10]
'''


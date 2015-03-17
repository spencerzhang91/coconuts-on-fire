def median(data):
    median = None
    data.sort()
    if len(data) % 2 == 0:
        i = len(data) // 2
        j = i + 1
        median = (data[i-1] + data[j-1]) / 2
    else:
        i = len(data) // 2 + 1
        median = data[i-1]

    return median

l1 = [1,2,3,4,5]
l2 = [1,2,3,4,5,6]
test1 = median(l1)
test2 = median(l2)
print(test1, test2)

        
'''
Implementation below seems much clearer than mine and shorter.

def median(data):
​
    data = sorted(data)
    half = int(len(data)/2)
    return data[half] if len(data)%2!=0 else (data[half-1]+data[half])/2

'''
'Very interesting...'

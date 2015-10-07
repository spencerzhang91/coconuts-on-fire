def insert_sort(array):
    '''
    Implementation of insertion sort
    The array will be sorted ascendingly
    '''
    count = len(array)
    for i in range(1, count):
        key = array[i]
        j = i - 1
        while j >= 0:
            if array[j] > key:
                array[j+1] = array[j]
                array[j] = key
            j -= 1
    return array

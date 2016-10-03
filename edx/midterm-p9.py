def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    copyList = []
    for item in aList:
        if type(item) != list:
            copyList.append(item)
        else:
            return flatten(item)
    return copyList

List = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flattened = flatten(List)

print(List)
print(flattened)
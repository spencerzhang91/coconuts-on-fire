def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    if not aList:
        return []
    for item in aList:
        if type(item) != list:
            return [item] + flatten(aList[1:])
        else:
            return flatten(item) + flatten(aList[1:])



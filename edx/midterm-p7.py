def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    intersection = {}
    difference = {}
    shorterDict = (lambda x, y: x if len(x) <= len(y) else y)(d1, d2)
    longerDict = (lambda x, y: x if len(x) > len(y) else y)(d1, d2)
    for key_s in shorterDict:
        if key_s in longerDict:
            intersection[key_s] = (lambda x,y: x > y)(d1[key_s], d2[key_s])
        else:
            difference[key_s] = shorterDict[key_s]
    for key_l in longerDict:
        if key_l not in intersection:
            difference[key_l] = longerDict[key_l]
    return (intersection, difference)

    
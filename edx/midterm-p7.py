def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    intersection = {}
    difference = {}
    shorterDict = (lambda x, y: x if len(x) <= len(y) else y)(d1, d2)
    longerDict = (lambda x, y: x if len(x) > len(y) else y)(d1, d2)
    for key in shorterDict:
        if key in longerDict:
            pass

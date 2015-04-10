file = open(r'E:\规划与建筑学\27\研究生（2014-2017）\研一（下）\四会多规合一\relics.csv')

def Cities(csv):
    '''
    A function to drag out x and y coordinates from a csv file(n roww 2 col) and
    convert them into complex numbers and store into a frozen set.
    '''
    assembly = []
    for item in csv:
        a = item.rstrip()        
        pair = tuple(map(lambda x: float(x), a.split(',')))
        coor = complex(*pair)
        assembly.append(coor)
    
    return frozenset(assembly)


res = Cities(file)
print(res)

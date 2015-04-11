import csv

# file_xy是景点经纬度的csv文件，file_value是景点热度的csv文件
file_xy = open(r'J:\四会多规合一\四会景点坐标.csv')
file_value = open(r'J:\四会多规合一\四会景点热度.csv')



def nodes_reader(file):
    '''
    A function to drag out x and y coordinates from a csv file
    (n row 2 col) and convert them into complex numbers and store
    into a frozen set. It's extended to work with more than 2 colums
    and can omit empty rows.
    '''
    assembly = []
    readerxy = csv.reader(file, delimiter=',', skipinitialspace=True)
    filter_num = first_n(file_value)#Attention value below this will be omited.
    print('firstn:', filter_num)
    for row in readerxy:
        if row[0] != '':
            latitude = float(row[1])# latitude as Y coordinate
            longitude = float(row[2])# longitude as X coordinate
            coor = complex(longitude, latitude)
            if float(row[3]) >= filter_num:
                assembly.append(coor)
    print('length:', len(assembly))
    return frozenset(assembly)


def first_n(file):
    value_list = []
    readerv = csv.reader(file, delimiter=',', skipinitialspace=True)
    for row in readerv:
        if row[1] != 0:
            value_list.append(float(row[1]))
    value_list.sort()
    n = 10
    return value_list[(len(value_list)-1)-n]# 这里的n是要打算从中取n个景点
    



    
test = nodes_reader(file_xy)
print(test)


        
    
    

import time
path = open(r'D:\BaiduYunDownload\2013 New York Taxi Data\tripData2013\trip_data_1.csv')

def openner(path):
    for item in path:
            yield item


a = openner(path)
newfile = open(r'D:\BaiduYunDownload\2013 New York Taxi Data\tripData2013\part_of_data1.txt','w')
time0 = time.clock()
for i in range(1000000):
    row = str(list(next(a).split(','))[-6:])
    row = row.replace("'","")
    row = row.replace("[","")
    row = row.replace("]","")
    row = row[:-2]
    newfile.write(row + '\n')
        
newfile.close()
time1 = time.clock()

print(time1 - time0)

# newfile.write(str(row[-6:]))

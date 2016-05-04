# developing a spyder using baidu place api to collect geojson data
import re
from urllib import request
import json
import geojson
import csv

p_title = re.compile(r'<a href=.*>(.*)</a>')

page = '0'
size = '1'
detail = '2' # this parameter affects level of detail

url = 'http://api.map.baidu.com/place/v2/search?\
ak=IniXfqhsWAyZQpkmh5FtEVv0&output=json&query=%E6\
%97%A5%E6%96%99&page_size='+size+'&page_num='+page+'&scope\
='+detail+'&region=%E5%B9%BF%E5%B7%9E'

with request.urlopen(url) as response:
    html = response.read()
# decode html page to string
txt = html.decode('utf-8')
print(txt)
# following steps extract data according to format provided by baidu
# type(dict_raw) == 'class dict'
dict_raw = json.JSONDecoder().decode(txt)


results = dict_raw['results'][0]
trans = json.JSONEncoder().encode(results)
data = json.JSONDecoder().decode(trans)



file = open(r'D:\GITHUB\Pytoys\d.csv', 'w')
temp = []
for key in sorted(data):
    temp.append(data[key])

writer = csv.writer(file, dialect='excel')

writer.writerow(temp)
file.close()
# current phase(before AUG): perfectly convert json to geojson


"""
A simple script that uses Baidu Place API to search certain kinds of place
in a range of circular space.
This API can be called maximum 2000 times per day.
"""

import requests, json

mykey = "IniXfqhsWAyZQpkmh5FtEVv0" # my developer key
city = "北京"
place = "公园"

payload_city = {'ak': mykey,
            'output': 'json',
            'query': place,
            'page_size': 10,
            'page_num': 0,
            'scope': 2,
            'regrion': city}

basicAPI = "http://api.map.baidu.com/place/v2/search"
test = "http://api.map.baidu.com/place/v2/search?query=百度大厦&region=深圳&city_limit=true&output=json&ak=IniXfqhsWAyZQpkmh5FtEVv0"
res = requests.get(basicAPI, params=payload_city)
print(res.url)
print(res.text)

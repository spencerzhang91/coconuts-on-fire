"""
A simple script that uses Baidu Place API to search certain kinds of place
in a range of circular space.
This API can be called maximum 2000 times per day.
"""

import requests, json

key = "IniXfqhsWAyZQpkmh5FtEVv0"
city = "韶关"
place = "餐厅"

api_url = ("http://api.map.baidu.com/place/v2/search" +
          "?q=%s&region=%d&output=json&ak=%d" % (query, city, key))

print(api_url)
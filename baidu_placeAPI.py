"""
A simple script that uses Baidu Place API to search certain kinds of place
in a range of circular space.
This API can be called maximum 2000 times per day.
"""

import requests, json

key = "IniXfqhsWAyZQpkmh5FtEVv0"
city = "韶关"
query = "餐厅"

api_url = ("http://api.map.baidu.com/place/v2/search" +
          "?q=%s&region=%s&output=json&ak=%s" % (query, city, key))

print(len(api_url))
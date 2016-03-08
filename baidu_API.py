"""
A simple script that uses Baidu Place API to search certain kinds of place
in a range of circular space.
This API can be called maximum 2000 times per day.
"""

import requests, json
import psycopg2

mykey = "IniXfqhsWAyZQpkmh5FtEVv0" # my developer key
city = "韶关"
place = "公园"

cord1 = (39.915, 116.404)
cord2 = (39.975, 116.414)
radius = 500 # meters

payload_city = {
    'ak': mykey,
    'output': 'json',
    'query': place,
    'page_size': 10,
    'page_num': 0,
    'scope': 2,
    'region': city
}

payload_rect = {
    'ak': mykey,
    'output': json,
    'query': place,
    'page_size': 10,
    'page_num': 0,
    'scope': 2,
    'bounds': "%s, %s, %s, %s" % (*cord1, *cord2)
    'location': cord1,
    'radius': radius
}

payload_circ = {
    'ak': mykey,
    'output': json,
    'query': place,
    'page_size': 10,
    'page_num': 0,
    'scope': 2,
}

basicAPI = "http://api.map.baidu.com/place/v2/search"

res = requests.get(basicAPI, params=payload_city)
jsonobj = json.loads(res.text)
print(type(jsonobj))
print(type(res.text))
print(json.dumps(jsonobj, sort_keys=False, indent=4))

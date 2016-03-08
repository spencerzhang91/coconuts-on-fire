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

payload_city = {
    'ak': mykey,
    'output': 'json',
    'query': place,
    'page_size': 10,
    'page_num': 0,
    'scope': 2,
    'region': city
}

payload_circ = {
    'ak': mykey,

}
basicAPI = "http://api.map.baidu.com/place/v2/search"

res = requests.get(basicAPI, params=payload_city)
jsonobj = json.loads(res.text)
print(type(jsonobj))
print(type(res.text))
print(json.dumps(jsonobj, sort_keys=False, indent=4))


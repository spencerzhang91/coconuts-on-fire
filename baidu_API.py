"""
A simple script that uses Baidu Place API to search certain kinds of place
in a range of circular space.
This API can be called maximum 2000 times per day.
"""

import requests, json
# import psycopg2
class ConvertFailure(Exception):
    def __str__(self):
        return "Convertion Failed."


mykey = "IniXfqhsWAyZQpkmh5FtEVv0" # my developer key
city = "韶关"
place = "公园"

coor1 = (39.915, 116.404)
coor2 = (39.975, 116.414)
radius = 500 # meters

city_params = {
    # parameters for place api
    'ak': mykey,
    'output': 'json',
    'query': place,
    'page_size': 10,
    'page_num': 0,
    'scope': 2,
    'region': city
}

rect_params = {
    # parameters for place api
    'ak': mykey,
    'output': 'json',
    'query': place,
    'page_size': 10,
    'page_num': 0,
    'scope': 2,
    'bounds': "%s, %s, %s, %s" % (*coor1, *coor2),
    'location': coor1,
    'radius': radius
}

circ_params = {
    # parameters for place api
    'ak': mykey,
    'output': 'json',
    'query': place,
    'page_size': 10,
    'page_num': 0,
    'scope': 2,
}

geocoder_params = {
    # parameters for geocoder api
    'ak': mykey,
    'output': 'json',
    'address': None
}

placeAPI = "http://api.map.baidu.com/place/v2/search"
geocoder = "http://api.map.baidu.com/geocoder/v2/"

res_city = requests.get(placeAPI, params=city_params)
res_rect = requests.get(placeAPI, params=rect_params)
res_circ = requests.get(placeAPI, params=circ_params)

# print(res_city.url)

jsonobj = json.loads(res_city.text)
print(type(jsonobj))
print(type(res_city.text))
# print(json.dumps(jsonobj, sort_keys=False, indent=4))

# Below this line defines a series of Baidu geo-data API calling functions
def addr2coor(addresses: str)->tuple:
    '''
    This function converts addresses to a (longitude, latitude) coordinate.
    '''
    for address in addresses:
        geocoder_params['address'] = address
        res = requests.get(geocoder, params=geocoder_params)
        res.raise_for_status()
        coor = json.loads(requests.get(geocoder, params=geocoder_params).text)
        # print(coor)
        if coor['status'] == 0:
            location = coor['result']['location']
            yield (address, location['lng'], location['lat'])
        else:
            raise ConvertFailure


def rescounter(function)->tuple:
    """A addr2coor wraper"""
    pass

if __name__ == '__main__':

    address_list = ["天安门", "故宫", "奥林匹克公园", "广州塔"]
    cor = addr2coor(address_list)
    for item in cor:
        print(item)

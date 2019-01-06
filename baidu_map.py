#coding:utf-8
import requests

import json

def locatebyLatLng(lat, lng, pois=0):
    '''
    根据经纬度查询地址
    '''
    items = {'location': str(lat) + ',' + str(lng), 'ak': 'wnYnjPTPDFZmtTZA2p7GaBtRGSo5EUtg', 'output': 'json'}
    res = requests.get('http://api.map.baidu.com/geocoder/v2/', params=items)
    result = res.json()
    #print(result)
    #print('--------------------------------------------')
    #result = result['result']['formatted_address'] + ',' + result['result']['sematic_description']
    result = result['result']['addressComponent']['province']
    return result

a = locatebyLatLng(37.895487,120.798784)

test_dict = [{"name":a,"value":123}]

print json.dumps(test_dict, encoding='UTF-8', ensure_ascii=False)

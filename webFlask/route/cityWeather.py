# -*- coding: utf-8 -*-
from urllib import request
from urllib.parse import quote


def citywea(area,city,date,prov):
    city = quote(city, 'utf-8')
    prov= quote(prov, 'utf-8')
    host = 'http://iweather.market.alicloudapi.com'
    path = '/history'
    method = 'GET'
    appcode = 'f4d3ac24150d48e089cffaad95f7069d'
    querys = 'area='+area+'&city='+city+'&date='+date+'&prov='+prov
    bodys = {}
    url = host + path + '?' + querys

    resp = request.Request(url)
    resp.add_header('Authorization', 'APPCODE ' + appcode)
    response = request.urlopen(resp)
    content = response.read().decode('utf-8')
    print(content)

citywea("","湛江","202010","广东")
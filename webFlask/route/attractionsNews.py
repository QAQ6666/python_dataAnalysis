# -*- coding: utf-8 -*-
import json
from urllib import request
from urllib.parse import quote

import ssl

def attractionsNew(province):
    host = 'https://scenicspot.market.alicloudapi.com'
    path = '/lianzhuo/scenicspot'
    method = 'GET'
    appcode = 'f4d3ac24150d48e089cffaad95f7069d'
    province = quote(province, 'utf-8')
    #querys = 'city=%E6%B5%8E%E5%8D%97&page=1&province=%E5%B1%B1%E4%B8%9C&spot=%E4%BA%94%E9%BE%99%E6%BD%AD'

    querys= 'province='+province

    url = host + path + '?' + querys

    resp = request.Request(url)
    resp.add_header('Authorization', 'APPCODE ' + appcode)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    response = request.urlopen(resp, context=ctx)
    content = response.read().decode('utf-8')
    content = json.loads(content)
attractionsNew("广东省")
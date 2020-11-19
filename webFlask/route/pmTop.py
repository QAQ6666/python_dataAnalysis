# -*- coding: utf-8 -*-
from urllib import request
import ssl
import json

def getpmtop():
    host = 'https://ali-pm25.showapi.com'
    path = '/pm25-top'
    appcode = 'f4d3ac24150d48e089cffaad95f7069d'
    url = host + path

    resp = request.Request(url)
    resp.add_header('Authorization', 'APPCODE ' + appcode)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    response = request.urlopen(resp, context=ctx)
    content = response.read().decode('utf-8')
    content = json.loads(content)
    return (content['showapi_res_body']['list'][0:25])

#for obj  in getpmtop():
 #  print(obj)
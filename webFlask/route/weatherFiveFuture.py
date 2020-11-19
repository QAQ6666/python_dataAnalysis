# -*- coding: utf-8 -*-
import requests


def cityFivef(city):
    url = 'http://t.weather.itboy.net/api/weather/city/'+city
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    s = (requests.get(url,headers=headers))
    s.encoding = "UTF-8"
    s = s.json()
    return s['data']['forecast']



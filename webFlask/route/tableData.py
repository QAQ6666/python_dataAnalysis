# -*- coding: utf-8 -*-
import requests


def watchCityCode():
    url = "https://www.zhipin.com/wapi/zpCommon/data/cityGroup.json"
    # 发送get请求
    s = (requests.get(url)).json()
    chardict  = {}
    for arr in s['zpData']['cityGroup']:
        chardict[arr['firstChar']] = arr['cityList']
    return chardict

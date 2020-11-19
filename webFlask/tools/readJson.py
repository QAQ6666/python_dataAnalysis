# -*- coding: utf-8 -*-
import json
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
def strmatch(str):
    with open("../resources/cityCode.txt", "r", encoding="utf-8") as f:
        # 为a+模式时，因为为追加模式，指针已经移到文尾，读出来的是一个空字符串。
        ftext = f.read()  # 一次性读全部成一个字符串
        obj = json.loads(ftext)
        f.close()  # 关闭文件
        for s in obj:
             f = fuzz.partial_ratio(str, s['city_name'])
             if(f > 50):
                 return s['city_code']


# -*- coding: utf-8 -*-
import json
import tushare as ts
pro = ts.pro_api('cc32d4a4cf73d2ffcb763bf6b27c6ae24c87573a6cfc6c8321ae6f13')

df = pro.stock_company(exchange='SZSE', fields='ts_code,chairman,manager,secretary,reg_capital,setup_date,province')
print(df)
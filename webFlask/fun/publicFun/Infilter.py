# -*- coding: utf-8 -*-
from tools import Inverification


def getinFilter(username,Password):
    if not Inverification.account_name_fomart(username):
        msg = "用户名不合法"
        return msg
    if not Inverification.account_pwd_fomart(Password):
        msg = '密码组合不合法'
        return msg
    return False

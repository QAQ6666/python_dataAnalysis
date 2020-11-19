# -*- coding: utf-8 -*-
import re

NUM_LETTER = re.compile("^(?!\d+$)[\da-zA-Z_]+$")     #数字和字母组合，不允许纯数字
FIRST_LETTER = re.compile("^[a-zA-Z]")           #只能以字母开头
LenBig = re.compile('^(?![A-Z]+$)(?![a-z]+$)(?!\d+$)(?![\W_]+$)\S{8,}$')

def account_name_fomart(name):
    if NUM_LETTER.search(name):
       if FIRST_LETTER.search(name):
           return True
    return False
def account_pwd_fomart(pwd):
    if LenBig.search(pwd):
        return True
    return False


# -*- coding: utf-8 -*-

class User:
    name = ''
    pwd = ''

    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd

    def getName(self):
        return self.name

    def getPwd(self):
        return self.pwd

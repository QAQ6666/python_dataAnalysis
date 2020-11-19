# -*- coding: utf-8 -*-
from tools import sqlDb, Ciphertext
from entity import UserEntity


def LogVerification(name, pwd):
    result = sqlDb.selectData("select * from  user where name = '" + name + "'")
    if not result:
        return False
    #拿到字符串密码，但里边是字节，先对字符串转字节，利用密文算法转为原密码字节，在对字节转字符串
    password = Ciphertext.des_decrypt('testtest', str.encode(result[0][2]))
    password = password.decode()

    if (password == pwd):
        u1 = UserEntity.User(name, result[0][2])
        return u1.getPwd()
    else:
        return False

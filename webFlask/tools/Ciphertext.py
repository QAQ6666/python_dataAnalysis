# -*- coding: utf-8 -*-
import binascii
from pyDes import des, CBC, PAD_PKCS5


def des_encrypt(secret_key, s):
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en)


def des_decrypt(secret_key, s):
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    return de


#secret_str = des_encrypt('testtest', 'asd123456')
#clear_str = des_decrypt('testtest',str.encode('67a37b1e942f7d8acba6157e25b095ac'))
#print(clear_str.decode())
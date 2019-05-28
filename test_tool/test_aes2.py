# -*- coding=utf-8-*-

from Crypto.Cipher import AES
import os
from Crypto import Random
import base64

"""
aes加密算法
padding : PKCS5
"""

class AESUtil:

    __BLOCK_SIZE_16 = BLOCK_SIZE_16 = AES.block_size

    @staticmethod
    def encryt(str, key):
        cipher = AES.new(bytes(key,'utf-8'), AES.MODE_ECB)
        x = AESUtil.__BLOCK_SIZE_16 - (len(str) % AESUtil.__BLOCK_SIZE_16)
        if x != 0:
            str = str + chr(x)*x
        msg = cipher.encrypt(str.encode())
        print ('类型： ',type(msg))
        msg = base64.urlsafe_b64encode(msg).replace('=', '')
        return msg

    @staticmethod
    def decrypt(enStr, key):
        cipher = AES.new(key, AES.MODE_ECB)
        enStr += (len(enStr) % 4)*"="
        decryptByts = base64.urlsafe_b64decode(enStr)
        msg = cipher.decrypt(decryptByts)
        paddingLen = ord(msg[len(msg)-1])
        return msg[0:-paddingLen]

if __name__ == "__main__":
    print (AESUtil.encryt("512345", "1234567812345678"))
    print (AESUtil.decrypt("1MbqzdK0IzP8vchDgRlzvw", "1234567812345678"))
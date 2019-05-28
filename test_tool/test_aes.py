#!/usr/bin/env python        #
# -*- coding: utf-8 -*-      #
# @Time    : 2018-03-29 8:53 #
# @author  : xuejf           #
# @email   :171521952@qq.com #
# -------------------------- #
###预处理密码和明文->初始化AES->加密->转码->输出结果

from Crypto.Cipher import AES
from binascii import b2a_hex
from binascii import a2b_hex

# 补全字符
def align(str, isKey=False):
    # 如果接受的字符串是密码，需要确保其长度为16
    if isKey:
        if len(str) > 16:
            return str[0:16]
        else:
            return align(str)
    # 如果接受的字符串是明文或长度不足的密码，则确保其长度为16的整数倍
    else:
        zerocount = 16-len(str) % 16
        for i in range(0, zerocount):
            str = str + '\0'
        return str

# ECB模式加密
def encrypt_ECB(str, key):
    # 补全字符串
    str = align(str)
    key = align(key, True)
    # 初始化AES
    AESCipher = AES.new(key, AES.MODE_ECB)
    # 加密
    cipher = AESCipher.encrypt(str)
    return b2a_hex(cipher)

###解密的流程是：预处理密码->初始化AES->转码->解密->输出结果
# ECB模式解密
def decrypt_ECB(str, key):
    # 补全字符串
    key = align(key, True)
    # 初始化AES
    AESCipher = AES.new(key, AES.MODE_ECB)
    # 解密
    paint = AESCipher.decrypt(a2b_hex(str))
    # 去除/0
    paint = paint.rstrip('\0')
    return paint


# 先设置一段明文和密码
Text = 'Suprise！！****** *****r!'
key = 'mor'

# ECB模式加密
ciphertext = encrypt_ECB(Text, key)
print("ECB模式密文：" + ciphertext)
# ECB模式解密
plaintext = decrypt_ECB(ciphertext, key)
print("ECB模式明文：" + plaintext)


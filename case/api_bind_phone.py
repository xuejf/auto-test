#!/usr/bin/env python        #
# -*- coding: utf-8 -*-      #
# @Time    : 2018-03-29 8:53 #
# @author  : xuejf           #
# @email   :171521952@qq.com #
# -------------------------- #
import requests
import unittest
import json

###单元测试时导入工具
import sys
sys.path.append("..")
from test_tool.io_txt import *
import urllib.parse
from  config.config_g import *
"""
{
  "uid": "5825487",
  "secret": "117f280e021e13fd80a24676952c4bc3"
}
"""
class ApiTestCase(unittest.TestCase):
    def setUp(self):
        print("******************start test******************")
        ##设置访问api接口信息
        self.url = 'http://api.nhbia.net/v2_user/bind_phone?ysx_api_version=2.0'
        self.srcFile = 'en_v2_user_bind_phone.txt'
        self.retFile = 'r_v2_user_bind_phone.txt'
        ##设置配置文件目录信息
        self.inFile = cf._in_data_dir + self.srcFile
        self.outFile = cf._out_data_dir + self.retFile
        print(self.inFile)
        print(self.outFile)

    def test_1(self):
        '''
        http://api.nhbia.cn/v2_user/get_user_default_info?ysx_api_version=2.0
        '''
        # 1. 读取加密数据，
        en_str = read_txt(self.inFile)
        print(en_str)
        # 2. url编码数据，
        urllib.parse.quote(en_str, safe='')
        print(en_str)
        data = {'encrypt': en_str}
        print(data)

        headers = {"Content_Type": "application/x-www-form-urlencoded",
                   "Accept-Encoding": "gzip"
                   }
        res = requests.post(self.url, data=data, headers=headers)
        print(res.raw)  # 获得原始响应内容,需要stream=True
        if res.text[1:6]=="result":
            r_str = json.loads(res.text)
            print(r_str["result"])
            writetxt(self.outFile, r_str["result"])
        print(res.content)  # 获得二进制响应内容     # b''
        print(res.raise_for_status())  # 返回错误状态码 None
        self.assertEqual(200, res.status_code)

    def tearDown(self):
        print("****************** end test******************")
        pass

if __name__ == '__main__':
    unittest.main()
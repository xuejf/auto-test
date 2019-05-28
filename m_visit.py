#!/usr/bin/env python
# -*- coding: utf-8 -*-
###methods：方法模块；编写测试模块的用例方法
import time
import requests
from selenium import webdriver

br = webdriver.Chrome()
br.maximize_window()
br.get('http://manage.nhbia.cn')

def openLoginManage1():
    time.sleep(1)
    title = br.title
    return title

def openLoginManage2():
    time.sleep(1)
    #jg = br.find_elements_by_class_name("alert alert-info")
    jg = br.find_element_by_xpath("/html/body/div/div/div[2]/div/div").text
    print (type(jg))
    print (jg)
    return jg

def loginManage():
        # 头部信息
        # headers = {
        #     'Host': "localhost",
        #     'Accept-Language': "zh-CN,zh;q=0.8",
        #     'Accept-Encoding': "gzip, deflate",
        #     'Content-Type': "application/x-www-form-urlencoded",
        #     'Connection': "keep-alive",
        #     'Referer': "http://localhost/login",
        #     'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36"
        # }
        # data = {
        #     "_csrf": csrf,
        #     "username": "xiedj",
        #     "password": "***"
        # }
        #url = "http://localhost/login/checklogin"
        url = 'http://manage.nhbia.cn'
        d = {'username': 'admin', 'password': 'Lz@123'}
        r = requests.post(url, data=d)
        print(r.status_code)
        # response = requests.post(url, data=data, headers=headers)
        # return response.content
        #assertEqual(r.status_code, 200,"Login Success!")
        return r.status_code
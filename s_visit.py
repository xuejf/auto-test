#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
###import c_visit

######此处增加调试用例包.文件#######

import case.api_dis_partner_income
import case.v2_order_create_order
import case.v2_order_return_wx_info

###suite：测试套件模块；加载需要测试的具体用例
def suite1():
    # 创建测试套件
    suite = unittest.TestSuite()
    # 为套件添加测试用例
    #suite.addTest(c_visit.MyTestCase("test_OpenLoginManage1"))
    #suite.addTest(c_visit.MyTestCase("test_OpenLoginManage2"))
    #suite.addTest(c_visit.MyTestCase("test_LoginManage"))
    return suite

def suite2():
    # 创建测试套件
    suite = unittest.TestSuite()
    # 为套件添加测试用例，此处添加
    suite.addTest(case.v2_order_create_order.ApiTestCase("test_1"))
    suite.addTest(case.v2_order_return_wx_info.ApiTestCase("test_1"))
    #suite.addTest(case.v2_order_return_wx_info.ApiTestCase("test_1"))
    #suite.addTest(case.api_dis_partner_income.ApiTestCase("test_1"))
    return suite

def suite3():
    # 创建测试套件
    suite = unittest.TestSuite()
    # 为套件添加测试用例，此处添加

    return suite

def all_suite():
    #suite = unittest.TestSuite((suite1(),suite2(), suite3()))
    suite = unittest.TestSuite((suite2()))
    return suite

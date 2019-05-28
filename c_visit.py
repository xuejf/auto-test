#!/usr/bin/env python
# -*- coding: utf-8 -*-
###case：用例模块；编写测试模块的用例数据
import unittest
import m_visit


class MyTestCase(unittest.TestCase):

    # 初始化工作
    def setUp(self):
        pass

        # 退出清理工作

    def tearDown(self):
        pass

        # 具体的测试用例，一定要以test开头

    ##u'打开管理页面1'
    def test_OpenLoginManage1(self):
        self.assertMultiLineEqual(m_visit.openLoginManage1(), u'登录-游视秀')

    ## '打开管理页面2'
    def test_OpenLoginManage2(self):
        self.assertMultiLineEqual(m_visit.openLoginManage2(), u'请输入您的用户名和密码.')
    ##'登录'
    def test_LoginManage(self):
        self.assertEqual(m_visit.loginManage(), 200)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from HTMLTestRunner_PY3 import HTMLTestRunner
###HTMLTestRunner：测试报告模块；定义生成测试报告
def save_file():
    # 按照一定的格式获取当前的时间
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    # 确定生成报告的路径
    filePath = ".\out_report\\" + now + "pyResult.html"
    fp = open(filePath, 'wb')
    # 生成报告的Title,描述
    runner = HTMLTestRunner(stream=fp, title='娃娃机API接口测试报告', description='This  is Python  Report')
    return runner
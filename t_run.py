#!/usr/bin/env python
# -*- coding: utf-8 -*-
import r_gen
import s_visit
import unittest
from  config.config_g import *

if __name__ == '__main__':
    # 调用定义HTMLTestRunner的方法
    runner = r_gen.save_file()
    # 运行suite所组装的测试用例
    # runner = unittest.TextTestRunner()
    # 调用测试套件方法
    all_suite = s_visit.all_suite()
    # 执行测试套件
    runner.run(all_suite)


# 为了使程序更规范，且方便后期维护，故把程序分为四个模块：case、suite、HTMLTestRunner、methods
# case：用例模块；编写测试模块的用例数据
# suite：测试套件模块；加载需要测试的具体用例
# HTMLTestRunner：测试报告模块；定义生成测试报告
# methods：方法模块；编写测试模块的用例方法
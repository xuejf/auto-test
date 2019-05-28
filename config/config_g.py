#!/usr/bin/env python        #
# -*- coding: utf-8 -*-      #
# @Time    : 2018-03-29 8:53 #
# @author  : xuejf           #
# @email   :171521952@qq.com #
# -------------------------- #
from configparser import *


class ConfigFile ():
     #_in_data_dir = r'E:\work\auto_test2\in_data'
     #_out_data_dir = r'E:\work\auto_test2\out_data'
     _in_data_dir=""
     _out_data_dir=""
     def __init__(self):
          #print("enter __init__()")
          cf = ConfigParser()
          cf.read("init.conf", encoding="utf-8")
          #secs = cf.sections()
          #print(secs)
          #opts = cf.options("base")
          #kvs = cf.items("db")
          # read by type
          if(self._in_data_dir.strip()==""):
               self._in_data_dir = cf.get("base", "in_data_dir")
          if(self._out_data_dir.strip()==""):
               self._out_data_dir = cf.get("base", "out_data_dir")
          #print(self._in_data_dir)
          #print(self._out_data_dir)

cf=ConfigFile()


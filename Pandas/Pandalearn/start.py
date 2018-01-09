#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J
@license: Apache Licence  
@contact: 415900617@qq.com 
@site:  
@software: PyCharm 
@file: start.py 
@time: 2018/1/8 18:32 
@describe:

"""
import sys
from PandasDataFrame import RunMain
reload(sys)
sys.setdefaultencoding("utf-8")

def func():
    RunMain()



class Main():
    def __init__(self):
        func()


if __name__ == "__main__":
    Main() 
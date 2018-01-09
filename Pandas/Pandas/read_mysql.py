#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J
@license: Apache Licence  
@contact: 415900617@qq.com 
@site:  
@software: PyCharm 
@file: read_mysql.py 
@time: 2018/1/3 16:43 
@describe:pandas读取数据库

"""

import pandas as pd
import pymysql
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def func():

    mysql_cn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='student', charset="utf8")
    df = pd.read_sql('select * from tb_user_imei;', con=mysql_cn)
    print df[df.city=='保定']
    print df.index
    mysql_cn.close()


class Main():
    def __init__(self):
        func()


if __name__ == "__main__":
    Main() 
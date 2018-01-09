#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J
@license: Apache Licence  
@contact: 415900617@qq.com 
@site:  
@software: PyCharm 
@file: plot.py 
@time: 2018/1/4 15:07 
@describe:读取数据库信息并分析其话费总金额，利用pandas分析处理，并绘制
参考资料：http://blog.csdn.net/hustqb/article/details/54410670
"""
import random
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

import matplotlib.lines as mlines
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pymysql
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
mysql_cn = pymysql.connect(host='rm-bp12m295o6x312c6a.mysql.rds.aliyuncs.com', port=3306, user='wuhaojie',
                               passwd='aKjhadmvdsaAWDAf#lkmv', db='qiancheng', charset="utf8")
mysql_cn1 = mysql_cn
# 从数据库获取数据
def index_user():

    df = pd.read_sql('SELECT totalfee,user_id,yearmonth FROM qiancheng_phone_bill '
                     'WHERE user_id in (SELECT user_id FROM qiancheng_phone_bill) LIMIT 100;', con=mysql_cn)

    data = df['user_id']
    arr2 = []
    for i in data:
        arr2.append(i)
    a = {}
    for i in arr2:
        if arr2.count(i) > 1:
            a[i] = arr2.count(i)
    # print a.keys()
    mysql_cn.close()
    return a.keys()


def func2(s_user, j, f):
    # index_user()
    mysql_cn = pymysql.connect(host='rm-bp12m295o6x312c6a.mysql.rds.aliyuncs.com', port=3306, user='wuhaojie',
                               passwd='aKjhadmvdsaAWDAf#lkmv', db='qiancheng', charset="utf8")

    df = pd.read_sql('SELECT * from qiancheng_phone_bill WHERE user_id=%s'%s_user, con=mysql_cn)
    # print df.groupby('totalfee').max()
    print df['totalfee'].tolist()
    print "最大值", df['totalfee'].max()
    print "最小值", df['totalfee'].min()
    print "平均值", df['totalfee'].mean()  # 平均值
    print "总和", df['totalfee'].sum()
    print "最大值索引", df['totalfee'].idxmax()
    # print df.index
    mysql_cn.close()
    data = df['totalfee']
    arr1 = []
    for i in data:
        arr1.append(i)

    # return arr1
        # 图一

    s = pd.Series(arr1, index=df['yearmonth'].tolist())  # 要想多图合并必须用series
    s.plot(color=j[0], linestyle=f[0], style='*', grid='on')
    red_line = mlines.Line2D([], [], linestyle='--', color=j[0], markersize=2, label=u'通话总金额')
    plt.legend(handles=[red_line], loc='upper right')
    plt.ylabel('通话总金额')
    plt.xlabel('日期')


    return arr1

class Main():
    def __init__(self):
        # func()
        # func2()
        # index_user()
        b = []
        color_line = ['red', 'orange', 'green', 'blue', 'black']
        style_line = ['-', '--', '-.', ':']
        for i in index_user():
            print i
            j = random.sample(color_line, 1)
            f = random.sample(style_line, 1)
            b.append(func2(i, j, f))
        print b
        plt.show()

if __name__ == "__main__":
    Main() 
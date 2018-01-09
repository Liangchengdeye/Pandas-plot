#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J
@license: Apache Licence  
@contact: 415900617@qq.com 
@site:  
@software: PyCharm 
@file: plotBase.py 
@time: 2018/1/5 10:29 
@describe:画图基础
learnBy:http://blog.csdn.net/hustqb/article/details/54410670#fnref:1
"""
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
import matplotlib.lines as mlines
import pandas as pd
import matplotlib.pyplot as plt

# 用于导入中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# 将两张图合并为一张 需要使用Series不能用Dataframe
def func():

    # 导入数据
    df = pd.read_csv('tips.csv')
    data = df['total_bill']
    print data.max()
    data1 = df['tip']
    arr3 = []
    for i in data1:
        arr3.append(i)
    print max(arr3)
    arr1 = []
    for i in data:
        arr1.append(i)
    # 图一
    s = pd.Series(arr1)
    s.plot(color='r')
    plt.ylabel('total_bill')
    # plt.show()
    # 图二
    s = pd.Series(arr3)
    s.plot(secondary_y=True, style='--', color='green')
    plt.ylabel('tip')

    plt.grid(True)  # 显示网格
    blue_line = mlines.Line2D([], [], linestyle='-', color='green', markersize=2, label=u'tip')
    red_line = mlines.Line2D([], [], linestyle='--', color='red', markersize=2, label=u'total_bill')
    plt.legend(handles=[blue_line, red_line], loc='upper left')  # 图例位置
    plt.title('总账单-消费')
    plt.show()

def func2():
    # 最基本线形图绘制
    plt.plot([1, 3,8] ,'--*')  # --代表线性 *代表标记风格
    plt.ylabel('some numbers')
    # plt.show()

    df = pd.DataFrame(pd.np.random.randn(10, 4).cumsum(0), columns=list('ABCD'), index=pd.np.arange(0, 100, 10))
    df.plot()
    plt.xlabel('test')
    plt.show()
def zhuPlot():
    fig, axes = plt.subplots(2, 1)
    data = pd.Series(pd.np.random.randn(16), index=list('abcdefghijklmnop'))
    data.plot(kind='kde', ax=axes[0], color='r', alpha=0.7)
    data.plot(kind='barh', ax=axes[1], color='g', alpha=0.7)
    plt.show()
# 表格-两列图
def biaogePlot():
    df = pd.DataFrame(pd.np.random.rand(3,4), index=list('123'), columns=list('abcd'))
    print df
    df2 = pd.DataFrame(pd.np.random.rand(4,4), index=list('1234'), columns=list('abcd'))
    print df2
    fig, axes = plt.subplots(1, 2)
    df.plot(ax=axes[0])
    df2.plot(ax=axes[1])
    axes[0].set_title('333')
    axes[1].set_title('444')
    plt.show()
class Main():
    def __init__(self):
        # func()
        # func2()
        # zhuPlot()
        biaogePlot()

if __name__ == "__main__":
    Main()


#历年人口数据 http://s3.amazonaws.com/assets.datacamp.com/course/dasi/present.txt
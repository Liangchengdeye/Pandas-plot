#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J
@license: Apache Licence  
@contact: 415900617@qq.com 
@site:  
@software: PyCharm 
@file: Pandas_all.py 
@time: 2018/1/5 16:34 
@describe:pandas各类画图
learn_by:http://blog.csdn.net/luoyexuge/article/details/49069225
"""
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
import pandas as pd
from pylab import *

def func():

    # 画累和图 趋势走向图
    ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
    ts = ts.cumsum()
    ts.plot()
    plt.show()
    # 多条趋势走向图
    df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
    df = df.cumsum()
    df.plot()
    plt.show()

    # 画柱状图
    df2 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
    df2.plot(kind='bar')  # 分开并列线束
    df2.plot(kind='bar', stacked=True)  # 四个在同一个里面显示 百分比的形式
    df2.plot(kind='barh', stacked=True)  # 纵向显示
    df2.plot(kind='line')
    plt.show()

    df4 = pd.DataFrame({'a': np.random.randn(1000) + 1, 'b': np.random.randn(1000), 'c': np.random.randn(1000) - 1},
                       columns=list('abc'))
    df4.plot(kind='hist', alpha=0.5)
    df4.plot(kind='hist', stacked=True, bins=20)
    df4['a'].plot(kind='hist', orientation='horizontal', cumulative=True)  # cumulative是按顺序排序，加上这个
    plt.show()

    # Area Plot 面积图
    df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
    df.plot(kind='area')
    df.plot(kind='area', stacked=False)
    plt.show()

    # 散点图
    df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
    df.plot(kind='scatter', x='a', y='b')
    df.plot(kind='scatter', x='a', y='b', color='DarkBlue', label='Group 1')
    plt.show()

    # 饼图
    df = pd.DataFrame(3 * np.random.rand(4, 2), index=['a', 'b', 'c', 'd'], columns=['x', 'y'])
    df.plot(kind='pie', subplots=True, figsize=(8, 4))
    df.plot(kind='pie', subplots=True, autopct='%.2f', figsize=(8, 4))  # 显示百分比
    plt.show()

    # 画矩阵散点图
    df = pd.DataFrame(np.random.randn(1000, 4), columns=['a', 'b', 'c', 'd'])
    pd.plotting.scatter_matrix(df, alpha=0.2, figsize=(6, 6), diagonal='kde')
    plt.show()


class Main():
    def __init__(self):
        func()


if __name__ == "__main__":
    Main() 
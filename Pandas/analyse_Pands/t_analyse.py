#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J
@license: Apache Licence  
@contact: 415900617@qq.com 
@site:  
@software: PyCharm 
@file: t_analyse.py 
@time: 2018/1/3 17:19 
@describe:独立样本t检验

"""
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

import pandas as pd
from scipy.stats import ttest_ind, ttest_rel, stats
import numpy as np
from scipy.stats import chisquare


def func():

    IS_t_test = pd.read_csv('number.csv')
    Group1 = IS_t_test[IS_t_test['group'] == 1]['data']
    Group2 = IS_t_test[IS_t_test['group'] == 2]['data']
    print ttest_ind(Group1, Group2)  # 独立样本t检验
    # ttest_ind默认两组数据方差齐性的，如果想要设置默认方差不齐，可以设置equal_var = False
    print ttest_ind(Group1, Group2, equal_var=True)
    print ttest_ind(Group1, Group2, equal_var=False)
    # .配对样本t检验
    print ttest_rel(Group1, Group2)

    # w, p = stats.levene(*args)
    # # levene方差齐性检验。levene(*args, **kwds)  Perform Levene test for equal variances.如果p<0.05，则方差不齐
    # print w, p
    # 进行方差分析
    # f, p = stats.f_oneway(*args)
    # print f, p


def func2():
    #     卡方检验
    # 卡方检验就是统计样本的实际观测值与理论推断值之间的偏离程度，实际观测值与理论推断值之间的偏离程度就决定卡方值的大小，
    # 卡方值越大，越不符合；卡方值越小，偏差越小，越趋于符合，若两个值完全相等时，卡方值就为0，
    # 表明理论值完全符合。（from 百度百科2333）
    #
    #     单因素卡方检验
    observed = np.array([15, 95])
    # 观测值：110学生中化妆的女生95人，化妆的男生15人
    expected = np.array([55, 55])
    # 理论值：110学生中化妆的女生55人，化妆的男生55人
    print chisquare(observed, expected)
class Main():
    def __init__(self):
        func()
        func2()


if __name__ == "__main__":
    Main() 
#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J
@license: Apache Licence  
@contact: 415900617@qq.com 
@site:  
@software: PyCharm 
@file: PeoplePlot.py 
@time: 2018/1/5 18:37 
@describe:
人口男女比例
"""
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
import pandas as pd
import matplotlib.pyplot   as plt
def func():
    url = 'http://s3.amazonaws.com/assets.datacamp.com/course/dasi/present.txt'
    present = pd.read_table(url, sep=' ')
    print present.head()
    print present.shape
    print present.columns
    present_year = present.set_index('year')
    print present_year.head()
    present_year['boys'].plot()
    present_year['girls'].plot()
    plt.legend(loc='best')
    # loc 参数：   right
    #             center left
    #             upper right
    #             lower right
    #             best
    #             center
    #             lower left
    #             center right
    #             upper left
    #             upper center
    #             lower center
    # plt.show()
    # 累积的柱状图，则只需要指定stacked = True。
    present_year[:10].plot(kind='bar', stacked=False)  # kind参数：line, bar, barh, kde, density, scatter。
    present_year.plot(x='boys', y='girls', kind='scatter', color='r')
    plt.show()


class Main():
    def __init__(self):
        func()


if __name__ == "__main__":
    Main() 
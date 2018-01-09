#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J
@license: Apache Licence  
@contact: 415900617@qq.com 
@site:  
@software: PyCharm 
@file: read_web.py 
@time: 2018/1/3 16:27 
@describe:pandas读取网络资源或者读取本地文件
并操作所读取数据，相关方法查看相关函数实现

"""
# get_ipython().magic('matplotlib inline')
import pandas as pd



def func():
    data_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"  # 填写url读取
    # data_url = "hdfs://192.168.8.10:9000/user/hive/warehouse/trip/tips.csv"
    df = pd.read_csv(data_url)
    print df[df.day!= 'Sun'].head()
    # 提取不连续行和列的数据，这个例子提取的是第1,3,5行，第2,4列的数据
    print df.iloc[[1, 3, 5], [2, 4]]
    print df.iloc[3] #选取第3行
    # example:假设我们要筛选出小费大于$8的数据
    print df[df.tip > 8]

    print df.head()  # 打印数据前五行
    print df.tail()  # 打印数据后5行
    print df.columns  # 打印列名
    print df.index  # 打印行名
    print df.ix[10:20, 0:3]  # 打印10~20行前三列数据
    # 提取不连续行和列的数据，这个例子提取的是第1,3,5行，第2,4列的数据
    print df.iloc[[1, 3, 5], [2, 4]]
    # 专门提取某一个数据，这个例子提取的是第三行，第二列数据（默认从0开始算哈）
    print df.iat[3, 2]
    print "*"
    print df.drop(df.columns[[1, 2]], axis=1).head()  # 舍弃数据前两列
    # print df.drop(df.columns[[1, 2]], axis=0).head()  # 舍弃数据前两行
    print df.shape  # 打印维度
    print df.iloc[3]  # 选取第3行
    print df.iloc[2:4]  # 选取第2到第3行
    print df.iloc[0, 1]  # 选取第0行1列的元素
    # example:假设我们要筛选出小费大于$8的数据
    print df[df.tip > 8]
    # 数据筛选同样可以用”或“和”且“作为筛选条件，比如
    # 1
    print df[(df.tip > 7) | (df.total_bill > 50)]  # 筛选出小费大于$7或总账单大于$50的数据
    # 2
    print df[(df.tip > 7) & (df.total_bill > 50)]  # 筛选出小费大于$7且总账单大于$50的数据
    # 假如加入了筛选条件后，我们只关心day和time
    print df[['day', 'time']][(df.tip > 7) | (df.total_bill > 50)]
    print df.describe()  # 描述性统计
    print df.T  # 数据转置
    print df.sort_values(by='tip')  # 按tip列升序排序

    # example：统计性别
    count = df['sex'].value_counts()
    # 输出
    print count
    df['tip'].plot()

class Main():
    def __init__(self):
        func()


if __name__ == "__main__":
    Main() 
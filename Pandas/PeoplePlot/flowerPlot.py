#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J
@license: Apache Licence  
@contact: 415900617@qq.com 
@site:  
@software: PyCharm 
@file: flowerPlot.py 
@time: 2018/1/5 18:59 
@describe:鸢尾花数据

"""
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 要注意的是一旦导入了seaborn，matplotlib的默认作图风格就会被覆盖成seaborn的格式
sns.set(style="white", color_codes=True)
def func():
    url_2 = 'https://raw.github.com/pydata/pandas/master/pandas/tests/data/iris.csv'
    iris = pd.read_csv(url_2)
    iris1 = iris.copy()  # 复制一个数据集
    iris1['Id'] = range(0, len(iris['Name']))  # 追加一列
    print iris1.head()
    print iris.head()
    print iris['Name'].value_counts()  # 统计种类数量

    # 使用 .plot 做散点图
    iris.plot(kind="scatter", x="SepalLength", y="SepalWidth", color='r')  # 数据为萼片的长和宽 scatter散点图

    # 开始使用seaborn了它能同时显示直方图
    sns.jointplot(x="SepalLength", y="SepalWidth", data=iris, size=5)  # 联合分布 jointplot单个标量或者两个变量的画图

    # 我们还可以用seaborn's FacetGrid 标记不同的种类噢
        # Seaborn其实是在matplotlib的基础上进行了更高级的API封装，从而使得作图更加容易，
        # 在大多数情况下使用seaborn就能做出很具有吸引力的图，
        # 而使用matplotlib就能制作具有更多特色的图。应该把Seaborn视为matplotlib的补充，而不是替代物。
    sns.FacetGrid(iris, hue="Name", size=5)\
        .map(plt.scatter, "SepalLength", "SepalWidth")\
        .add_legend()  # hue英文是色彩的意思 # 注意这里的plt哦

    # 这图可以变现出密度的分布 --小提琴图
    sns.violinplot(x="Name", y="PetalLength", data=iris, size=6)

    # 通过这个曲线图可以看出不同特征值时的分布密度
    sns.FacetGrid(iris, hue="Name", size=6).map(sns.kdeplot, "PetalLength").add_legend()

    #  pairplot显示不同特征之间的关系
    sns.pairplot(iris1.drop("Id", axis=1), hue="Name", size=3)  # drop删除DataFrame的行或者列，axis=1为列
    # 修改参数dige_kind
    sns.pairplot(iris1.drop("Id", axis=1), hue="Name", size=3, diag_kind="kde")
    plt.show()
    # corr(x, y)
    # 相关系数，用来刻画二维随机变量两个分量间相互关联程度
    # -1 < corr(x, y) < 1, 也就是说相关系数介于 - 1到1之间
    # corr(x, y) = 0 则称X, Y不相关，不相关是指X, Y没有线性关系，但也有可能有其他关系，比如平方关系，立方关系等
    # corr(x, y) = 1, 则称X与Y完全正相关，corr(x, y) = -1, 则称X, Y完全负相关
    print iris.corr()
    # 在多变量概率统计中，散布矩阵是用来估计多维正态分布协方差的统计量。
    pd.plotting.scatter_matrix(iris, alpha=0.2, figsize=(6, 6), diagonal='kde')
    plt.show()
    # print iris.boxplot()  # 箱图 DataFrame提供了boxplot方法可以用来画箱图。
    iris.boxplot(by='Name', figsize=(8, 8))
    plt.show()
    # 直方图和概率密度分布
    print iris.ix[:, :-1].head()
    iris.ix[:, :-1].hist()  # hist直方图
    iris.plot(kind='kde')  # kde# 密度图
    plt.show()
    # 多变量的可视化
    pd.plotting.radviz(iris, 'Name')  # 径向坐标可视化（radviz）径向坐标可视化是基于弹簧张力最小化算法
    plt.show()
    pd.plotting.andrews_curves(iris, 'Name')  # 调和曲线图 调和曲线图的思想和傅立叶变换十分相似，是根据三角变换方法将 p 维空间的点映射到二维平面上的曲线上
    plt.show()
    pd.plotting.parallel_coordinates(iris, 'Name')  # 轮廓图的思想非常简单、直观，它是在横坐标上取 p 个点，
                                                    # 依次表示各个指标 (即变量)；横坐标上则对应各个指标的值
                                                    # (或者经过标准化变换后的值)，然后将每一组数据对应的点依次连接即可。
    plt.show()
class Main():
    def __init__(self):
        func()


if __name__ == "__main__":
    Main()

#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J
@license: Apache Licence  
@contact: 415900617@qq.com 
@site:  
@software: PyCharm 
@file: PandasDataFrame.py
@time: 2018/1/8 10:12 
@describe:pandas 常用函数杂烩集

"""
import sys


reload(sys)
sys.setdefaultencoding("utf-8")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
def func():
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    print s
    # 首先构造一组时间序列，作为我们第一维的下标：,从08号开始迭代6次到13号
    data = pd.date_range('20170108', periods=6)
    print data
    # 字典
    df2 = pd.DataFrame({'A': 1.,
                        'B': pd.Timestamp('20130102'),
                        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                        'D': np.array([3] * 4, dtype='int32'),
                        'E': pd.Categorical(["test", "train", "test", "train"]),
                        'F': 'foo'})

    print df2
    df = pd.DataFrame(np.random.randn(6, 4), index=data, columns=list('ABCD'))  # index行名,colimns列名
    # 默认情况下，如果不指定 `index` 参数和 `columns`，那么他们的值将用从 `0` 开始的数字替代。
    print df
    print df.head()      # 查看前五行
    print df.tail(3)     # 查看后三行
    print df.index       # 下标使用 `index` 属性查看
    print df.columns     # 列标使用 `columns` 属性查看
    print df.values      # 数据值使用 `values` 查看
    print df.describe()  # 查看简单的统计数据  std标准样差
    # ## 排序
    print df.sort_index(axis=0, ascending=True)           # 方法按照下标大小进行排序，`axis=0` 表示按第 0 维进行排序。
    print df.sort_index(ascending=False)                  # 对index进行排序
    print df.sort_index(axis=1, ascending=False)          # 对columns进行排序
    print df.sort_values(by='B', axis=0, ascending=True)  # 方法按照 `by` 的值的大小进行排序，例如按照 `B` 列的大小：
    # 虽然 `DataFrame` 支持 `Python/Numpy` 的索引语法，但是推荐使用 `.at, .iat, .loc, .iloc 和 .ix` 方法进行索引。
    print df.A
    print df[0:3]  # 切片读取三行
    print df['20170108':'20170110']
    # `loc` 可以方便的使用 `label` 进行索引：
    print df.loc[data[0]]  # 选取第一行
    # 多列数据：
    print df.loc[:, ['A', 'B']]
    # 选择多行多列：
    print df.loc['20170108':'20170109', ['A', 'B']]
    # 数据降维：
    print "数据降维", df.loc['20170109', ['A', 'B']]
    # 得到标量值：
    print df.loc[data[0], 'A']  # 取出第一行的A列元素
    print df.at[data[0], 'B']  # 使用at速度高于loc
    # ### 使用位置索引
    print df.iloc[3]  # 第3行数据
    # 连续切片
    print df.iloc[3:5, 0:3]  # 行 列
    # 索引不连续的部分：
    print df.iloc[[1, 2, 4], [0, 2]]
    # 索引整行：
    print df.iloc[1:3, :]
    # 索引整列：
    print df.iloc[:, 1:3]
    # 标量值
    print df.iat[1, 1]
    # ### 布尔型索引

    # 所有 `A` 列大于 0 的行：
    print df[df.A > 0]
    # 只留下所有大于 0 的数值
    print df[df > 0]

    # 使用 `isin` 方法做 `filter` 过滤：
    df2 = df.copy()
    df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
    print df2
    print df2[df2['E'].isin(['two', 'four'])]  # 过滤
    # ### 设定数据的值
    s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20170108', periods=6))
    print s1
    df['F'] = s1  # 添加一列信息，相当于合并
    print df
    # 使用at 或者 iat 修改单个值
    df.at[data[0], 'A'] = 1
    print df
    df.iat[0, 1] = 0  # 第 0 行 第 1 列 （从0开始）
    print df
    # 设定一整列：
    df.loc[:, 'D'] = np.array([5] * len(df))
    print df
    # 设定满足条件的数值：
    df2 = df.copy()
    df2[df2 > 0] = -df2
    print df2
    # ## 缺失数据
    df1 = df.reindex(index=data[0:4], columns=list(df.columns) + ['E'])
    df1.loc[data[0]:data[1], 'E'] = 1
    print df1
    # 丢弃所有缺失数据的行得到的新数据：
    print df1.dropna(how='any')
    # 填充丢失数据
    print df1.fillna(value=5)
    # 检查对视数据的位置
    print pd.isnull(df1)
    # ### 统计信息

    # 每一列的均值：
    print df.mean()
    # 每一行的均值：
    print df.mean(1)

    # 多个对象之间的操作，如果维度不对，`pandas` 会自动调用 `broadcasting` 机制：
    s = pd.Series([1, 3, 5, np.nan, 6, 8], index=data).shift(2)
    print s
    # 相减 `df - s`：
    print df.sub(s, axis='index')

    # ### apply 操作
    # 与 `R` 中的 `apply` 操作类似，接收一个函数，默认是对将函数作用到每一列上：
    print df.apply(np.cumsum)
    # 求每列最大最小值之差：
    print df.max()
    print df.apply(lambda x: x.max() - x.min())
    # 直方图
    s = pd.Series(np.random.randint(0, 7, size=10))
    print s
    # 直方图信息
    print s.value_counts()  # 统计个数
    # 绘制直方图信息
    g = s.hist()
    g.plot()
    plt.show()
    fig = g.get_figure()
    fig.savefig('apply.png')
    # ### 字符串方法
    # 当 `Series` 或者 `DataFrame` 的某一列是字符串时，我们可以用 `.str` 对这个字符串数组进行字符串的基本操作：
    s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
    print s.str.lower()

    # ## 合并
    # ### 连接
    df = pd.DataFrame(np.random.randn(10, 4))
    print df

    # 可以使用 `pd.concat` 函数将多个 `pandas` 对象进行连接：
    pieces = [df[:2], df[4:5], df[7:]]
    print pieces
    print pd.concat(pieces)  # pieces是一个很奇怪的list

    # ### 数据库中的 Join

    # `merge` 可以实现数据库中的 `join` 操作：
    left = pd.DataFrame({'key': ['foo', 'tom'], 'Lval': [1, 2]})
    print left
    right = pd.DataFrame({'key': ['foo', 'tom'], 'Rval': [4, 5]})
    print right
    print pd.merge(left, right, on='key')
    # append
    df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
    print df
    # 将第三行的值添加到最后：
    s = df.iloc[3]
    print df.append(s, ignore_index=True)  # ignore参数若为false则连序号也添加过去，若为true则追加序号为8

    # ### Grouping
    df33 = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                               'foo', 'bar', 'foo', 'foo'],
                         'B': ['one', 'one', 'two', 'three',
                               'two', 'two', 'one', 'three'],
                         'C': np.random.randn(8),
                         'D': np.random.randn(8)})

    print df33
    # 按照 `A` 的值进行分类：
    print df.groupby('A').sum()
    # 按照 `A, B` 的值进行分类：
    print df.groupby(['A', 'B']).sum()

    # ## 改变形状
    # ### Stack
    # 产生一个多 `index` 的 `DataFrame`：
    tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                         'foo', 'foo', 'qux', 'qux'],
                        ['one', 'two', 'one', 'two',
                         'one', 'two', 'one', 'two']]))
    index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
    df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
    print df
    # `stack` 方法将 `columns` 变成一个新的 `index` 部分：
    df2 = df[:4]
    stacked = df2.stack()
    print stacked
    # 可以使用 `unstack()` 将最后一级 `index` 放回 `column`
    print stacked.unstack()
    # 也可以指定其他的级别：
    print stacked.unstack(1)

    # ## 时间序列

    # 金融分析中常用到时间序列数据：
    rng = pd.date_range('3/6/2017 00:00', periods=5, freq='D')
    ts = pd.Series(np.random.randn(len(rng)), rng)
    print ts
    # 标准时间表示：
    ts_utc = ts.tz_localize('UTC')
    print ts_utc
    # 改变时区表示：
    print ts_utc.tz_convert('US/Eastern')

    # ## Categoricals
    df = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6], "raw_grade": ['a', 'b', 'b', 'a', 'a', 'e']})
    print df
    # 可以将 `grade` 变成类别：
    df["grade"] = df["raw_grade"].astype("category")
    print df["grade"]
    # 将类别的表示转化为有意义的字符：
    df["grade"].cat.categories = ["very good", "good", "very bad"]
    print df["grade"]
    # 添加缺失的类别：
    df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])
    print df["grade"]
    # 使用 `grade` 分组：
    print df.groupby("grade").size()

    # ## 绘图

    # 使用 `ggplot` 风格
    plt.style.use('ggplot')
    # `Series` 绘图：
    ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
    p = ts.cumsum().plot(title="timeseries, bokeh",
                       legend='top_left', label='趋势线')
    plt.xlabel('Date')
    plt.ylabel('Prices')

    # ts_pl = TimeSeries(ts.cumsum(), )
    # plt.show()  # 可以很方便的指定图例、xy周的标签，图面也漂亮了很多
    fig = p.get_figure()
    fig.savefig('timeseries.png')
    return "1"
class RunMain():
    def __init__(self):
        g=func()
        print g


if __name__ == "__main__":
    RunMain()
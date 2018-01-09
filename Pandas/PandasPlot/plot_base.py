#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J
@license: Apache Licence  
@contact: 415900617@qq.com 
@site:  
@software: PyCharm 
@file: plot_base.py 
@time: 2018/1/5 16:42 
@describe:

"""
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

# pylab 是 matplotlib 面向对象绘图库的一个接口。它的语法和 Matlab 十分相近

from    mpl_toolkits.mplot3d import Axes3D
from pylab import *
import matplotlib.pyplot   as plt
import pandas  as pd
def func():
    plt.figure()
    # 趋势累加图
    df = pd.DataFrame(np.random.randn(1000, 4), columns=list('ABCD'))
    df = df.cumsum()
    df.plot()
    plt.show()

    # print(ggplot(df,aes(x='A',y='B'))+geom_point())

    # 画简单的图形
    # 正弦余弦函数图形
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    c, s = np.cos(x), np.sin(x)
    plot(x, c, color="blue", linewidth=2.5, linestyle="-", label="cosine")  # label用于标签显示问题
    plot(x, s, color="red", linewidth=2.5, linestyle="--", label="sine")
    show()

    # 散点图

    n = 1024
    X = np.random.normal(0, 1, n)
    Y = np.random.normal(0, 1, n)
    scatter(X, Y)
    show()

    # # 条形图
    #
    #
    n = 12
    X = np.arange(n)
    Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
    Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
    bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
    bar(X, -Y2, facecolor='#ff9999', edgecolor='white')
    for x, y in zip(X, Y1):
        text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')
    ylim(-1.25, +1.25)
    show()

    # 饼图

    n = 20
    Z = np.random.uniform(0, 1, n)
    pie(Z), show()

    # 画三维图
    #
    fig = figure()
    ax = Axes3D(fig)
    x = np.arange(-4, 4, 0.1)
    y = np.arange(-4, 4, 0.1)
    x, y = np.meshgrid(x, y)
    R = np.sqrt(x ** 2 + y ** 2)
    z = np.sin(R)
    ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='OrRd')
    # cmap 可选参数：Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu,\
    #      BuPu_r, CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Greens_r, \
    #      Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired,\
    #      Paired_r, Pastel1, Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, \
    #      PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, Purples, \
    #      Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, \
    #      RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, Set3_r, \
    #      Spectral, Spectral_r, Vega10, Vega10_r, Vega20, Vega20_r, Vega20b, Vega20b_r, \
    #      Vega20c, Vega20c_r, Wistia, Wistia_r, YlGn, YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, \
    #      YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, afmhot_r, autumn, autumn_r, binary, binary_r, \
    #      bone, bone_r, brg, brg_r, bwr, bwr_r, cool, cool_r, coolwarm, coolwarm_r, copper, \
    #      copper_r, cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, \
    #      gist_gray, gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, \
    #      gist_rainbow, gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, \
    #      gnuplot, gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r, \
    #      inferno, inferno_r, jet, jet_r, magma, magma_r, nipy_spectral, nipy_spectral_r, \
    #      ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, rainbow_r, \
    #      seismic, seismic_r, spectral, spectral_r, spring, spring_r, summer, summer_r, tab10, \
    #      tab10_r, tab20, tab20_r, tab20b, tab20b_r, tab20c, tab20c_r, terrain, terrain_r, viridis, \
    #      viridis_r, winter, winter_r
    show()



def func2():
    # from numpy.random import random

    colors = ['b', 'c', 'y', 'm', 'r']

    lo = plt.scatter(random(10), random(10), marker='x', color=colors[0])
    ll = plt.scatter(random(10), random(10), marker='o', color=colors[0])
    l = plt.scatter(random(10), random(10), marker='o', color=colors[1])
    a = plt.scatter(random(10), random(10), marker='o', color=colors[2])
    h = plt.scatter(random(10), random(10), marker='o', color=colors[3])
    hh = plt.scatter(random(10), random(10), marker='o', color=colors[4])
    ho = plt.scatter(random(10), random(10), marker='x', color=colors[4])

    plt.legend((lo, ll, l, a, h, hh, ho),
               ('Low Outlier', 'LoLo', 'Lo', 'Average', 'Hi', 'HiHi', 'High Outlier'),
               scatterpoints=1,
               loc='lower left',
               ncol=3,
               fontsize=8)

    plt.show()
class Main():
    def __init__(self):
        func()
        func2()

if __name__ == "__main__":
    Main() 
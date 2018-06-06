#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2018/6/6 22:45
@author: Pete
@email: yuwp_1985@163.com
@file: accenoise.py
@software: PyCharm Community Edition
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import  MultipleLocator

# Environment Configuration
matplotlib.rcParams['font.size'] = 15
# matplotlib.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签
# matplotlib.rcParams['axes.unicode_minus'] = False # 用来正常显示负号

T1Result = (
    (0,      3.998,  3.998),
    (0.001,  5.443,  5.443),
    (0.0015, 6.48,   6.48),
    (0.002,  7.594,  7.594),
    (0.0025, 8.754,  8.754),
    (0.003,  9.944,  9.944),
    (0.0035, 11.154, 11.154),
    (0.004,  12.379, 12.379),
    (0.0045, 13.615, 13.615),
    (0.005,  14.859, 14.859),
    (0.0055, 16.11,  16.11),
    (0.006,  17.366, 17.366),
)

T2Result = (
    (0,      3.998,  3.998),
    (0.001,  5.443,  5.443),
    (0.0015, 6.48,   6.48),
    (0.002,  7.594,  7.594),
    (0.0025, 8.754,  8.754),
    (0.003,  9.944,  9.944),
    (0.0035, 11.154, 11.154),
    (0.004,  12.379, 12.379),
    (0.0045, 13.615, 13.615),
    (0.005,  14.859, 14.859),
    (0.0055, 16.11,  16.11),
    (0.006,  17.366, 17.366),
)

def showAvgPosError():
    # Plot the figures
    fig = plt.figure()
    avgAxes = fig.add_subplot(111)
    t2Array = np.array(T2Result)
    t1Array = np.array(T1Result)
    avgAxes.plot(t1Array[:, 0], t1Array[:, 1], "b-", marker="o", linewidth=2, label=u"$航位推算(T_1)$")
    avgAxes.plot(t1Array[:, 0], t1Array[:, 2], "r-", marker="^", linewidth=2, label=u"$本文提出的算法(T_1)$")
    avgAxes.set_xlabel(u"误差分布的标准差(米/平方秒)")
    avgAxes.set_ylabel(u"平均定位误差(米)")
    # avgAxes.set_xlim(0, 60)
    # avgAxes.set_ylim(0.5, 1.1)
    # avgAxes.xaxis.set_major_locator(MultipleLocator(10))
    # avgAxes.xaxis.set_minor_locator(MultipleLocator(5))
    # avgAxes.yaxis.set_major_locator(MultipleLocator(0.1))
    # avgAxes.yaxis.set_minor_locator(MultipleLocator(0.05))
    avgAxes.grid(True)
    avgAxes.legend(loc=3)
    plt.show()
    return

if __name__ == "__main__":
    showAvgPosError()
    print("Done.")
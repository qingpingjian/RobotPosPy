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
    (0,      3.998,  2.487),
    (0.001,  5.443,  2.639),
    (0.0015, 6.48,   2.663),
    (0.002,  7.594,  2.696),
    (0.0025, 8.754,  2.737),
    (0.003,  9.944,  2.787),
    (0.0035, 11.154, 2.844),
    (0.004,  12.379, 2.908),
    (0.0045, 13.615, 2.978),
    (0.005,  14.859, 3.054),
    (0.0055, 16.11,  3.135),
    (0.006,  17.366, 3.221),
)

T2Result = (
    (0,      6.576,  3.386),
    (0.001,  7.22,  3.42),
    (0.0015, 7.721,   3.48),
    (0.002,  8.304,  3.51),
    (0.0025, 8.947,  3.6),
    (0.003,  9.639,  3.73),
    (0.0035, 10.377, 3.85),
    (0.004,  11.146, 3.90),
    (0.0045, 11.927, 4.05),
    (0.005,  12.729, 4.22),
    (0.0055, 13.54,  4.39),
    (0.006,  14.364, 4.57),
)

def showAvgPosError():
    # Plot the figures
    fig = plt.figure()
    avgAxes = fig.add_subplot(111)
    t1Array = np.array(T1Result)
    t2Array = np.array(T2Result)
    avgAxes.plot(t1Array[:, 0], t1Array[:, 1], "b-", marker="^", linewidth=2, label=u"航位推算" + "$(T_1)$")
    avgAxes.plot(t1Array[:, 0], t1Array[:, 2], "r-", marker="o", linewidth=2, label=u"本文提出的算法" + "$(T_1)$")

    avgAxes.plot(t2Array[:, 0], t2Array[:, 1], "b-", marker="v", linewidth=2, label=u"航位推算" + "$(T_2)$")
    avgAxes.plot(t2Array[:, 0], t2Array[:, 2], "r-", marker="D", linewidth=2, label=u"本文提出的算法" + "$(T_2)$")

    avgAxes.set_xlabel(u"误差分布的标准差（米每平方秒）")
    avgAxes.set_ylabel(u"平均定位误差（米）")
    avgAxes.set_xlim(0, 0.006)
    avgAxes.set_ylim(0, 20)
    avgAxes.xaxis.set_major_locator(MultipleLocator(0.001))
    avgAxes.xaxis.set_minor_locator(MultipleLocator(0.0005))
    avgAxes.yaxis.set_major_locator(MultipleLocator(4))
    avgAxes.yaxis.set_minor_locator(MultipleLocator(2))
    avgAxes.grid(True, axis="y")
    avgAxes.legend(loc=2)

    plt.show()
    return

if __name__ == "__main__":
    showAvgPosError()
    print("Done.")
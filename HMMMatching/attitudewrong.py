#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2018/6/6 14:39
@author: Pete
@email: yuwp_1985@163.com
@file: attitudewrong.py
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
    (0, 1.000),
    (5, 1.000),
    (10, 1.000),
    (15, 1.000),
    (20, 1.000),
    (25, 1.000),
    (30, 0.950),
    (35, 0.950),
    (40, 0.950),
    (45, 0.900),
    (50, 0.850),
    (55, 0.850),
    (60, 0.700),
)

T2Result = (
    (0, 1.000),
    (5, 1.000),
    (10, 1.000),
    (15, 1.000),
    (20, 0.950),
    (25, 0.950),
    (30, 0.950),
    (35, 0.850),
    (40, 0.750),
    (45, 0.700),
    (50, 0.700),
    (55, 0.600),
    (60, 0.600),
)

def showAttitudeDetectPrecision():
    # Plot the figures
    fig = plt.figure()
    precisionAxes = fig.add_subplot(111)
    t2Array = np.array(T2Result)
    t1Array = np.array(T1Result)
    precisionAxes.plot(t1Array[:, 0], t1Array[:, 1], "b-", marker="o", linewidth=2, label="$T_1$")
    precisionAxes.plot(t2Array[:, 0], t2Array[:, 1], "r-", marker="^", linewidth=2, label="$T_2$")
    precisionAxes.set_xlabel(u"误差分布的标准差(度)")
    precisionAxes.set_ylabel(u"正确率")
    precisionAxes.set_xlim(0, 60)
    precisionAxes.set_ylim(0.5, 1.1)
    precisionAxes.xaxis.set_major_locator(MultipleLocator(10))
    precisionAxes.xaxis.set_minor_locator(MultipleLocator(5))
    precisionAxes.yaxis.set_major_locator(MultipleLocator(0.1))
    precisionAxes.yaxis.set_minor_locator(MultipleLocator(0.05))
    precisionAxes.grid(True)
    precisionAxes.legend(loc=3)
    plt.show()
    return

if __name__ == "__main__":
    showAttitudeDetectPrecision()
    print("Done.")
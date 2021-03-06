#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2018/3/6 下午11:19
@author: Pete
@email: yuwp_1985@163.com
@file: convergehistogram.py.py
@software: PyCharm Community Edition
"""

import math
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import sys

matplotlib.rcParams['font.size'] = 16

def drawHistogram(dataGroups, colors, patterns, labels, xTicks):

    fig = plt.figure()
    axCvg = fig.add_subplot(111)

    index = np.arange(len(dataGroups))
    bar_width = 0.2
    opacity = 0.2
    for i, dataGroup in enumerate(dataGroups):
        rectArray = axCvg.bar(index + i * bar_width, dataGroup, bar_width, alpha=opacity,
                              color=colors[i], hatch=patterns[i], edgecolor=colors[i], label=labels[i])
        for j, rect in enumerate(rectArray):
            h = rect.get_height()
            axCvg.text(rect.get_x() + rect.get_width() / 2, h,
                       "%.1f" % (dataGroup[j]) if math.fabs(dataGroup[j] - 180.5) > sys.float_info.epsilon else "$\infty$",
                       ha="center", va="bottom", fontsize="16")

    plt.ylabel(u'已运动距离（米）')
    plt.xticks(index + bar_width * 0.5, xTicks)
    plt.ylim(0,200)
    plt.legend(loc=2, fontsize="16")
    plt.grid(True, axis="y")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    semMatchValues = (61.9, 180.5)
    proposedValues = (63.8, 125.15)
    dataGroups = [semMatchValues, proposedValues]
    # colorList = ['#ff0000', '#0000ff', '#0007ff', '#550055', '#ff0033']
    colorList = [['#0000ff', '#0000ff'], ['#ff0000', '#ff0000']]
    patterns = ["/", "\\", "x", "o", "O", ".", "*", "-", "+", "|"]
    labels = [u'semMatch算法', u'本文提出的算法']
    xTicks = ['$T_1$', '$T_2$']
    drawHistogram(dataGroups, colorList, patterns, labels, xTicks)
    print("Done.")
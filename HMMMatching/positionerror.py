#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2018/6/6 18:38
@author: Pete
@email: yuwp_1985@163.com
@file: positionerror.py
@software: PyCharm Community Edition
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from matplotlib.ticker import  MultipleLocator

# Environment Configuration
matplotlib.rcParams['font.size'] = 15
# matplotlib.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签
matplotlib.rcParams['axes.unicode_minus'] = False # 用来正常显示负号

def showPosError():
    t1pdrErrorFilePath = "./TrajectoryOne/20180603164024_ground_pdr_error.csv"
    t1matchErrorFilePath = "./TrajectoryOne/20180603164024_ground_atmatch_error.csv"
    t1groundTruthFilePath = "./TrajectoryOne/20180603164024_ground.csv"

    t1DistDF = pd.read_csv(t1groundTruthFilePath)
    t1DistList = [gdt[2] for gdt in t1DistDF.values]
    t1PdrErrDF = pd.read_csv(t1pdrErrorFilePath)
    t1PdrErrList = t1PdrErrDF.values[:,0]
    t1MatchErrDF = pd.read_csv(t1matchErrorFilePath)
    t1MatchErrList = t1MatchErrDF.values[:,0]

    t2pdrErrorFilePath = "./TrajectoryFour/20180603165643_ground_pdr_error.csv"
    t2matchErrorFilePath = "./TrajectoryFour/20180603165643_ground_pdr_error.csv"
    t2groundTruthFilePath = "./TrajectoryFour/20180603165643_ground.csv"

    t2DistDF = pd.read_csv(t2groundTruthFilePath)
    t2DistList = [gdt[2] for gdt in t2DistDF.values]
    t2PdrErrDF = pd.read_csv(t2pdrErrorFilePath)
    t2PdrErrList = t2PdrErrDF.values[:,0]
    t2MatchErrDF = pd.read_csv(t2matchErrorFilePath)
    t2MatchErrList = t2MatchErrDF.values[:,0]

    # Plot the figures
    fig = plt.figure()
    t1Axes = fig.add_subplot(121)
    t1Axes.set_xlabel(u"运动距离(米)")
    t1Axes.set_ylabel(u"定位误差(米)")
    t1Axes.plot(t1DistList, t1PdrErrList, "b-", linewidth=2, label=u"航位推算")
    t1Axes.plot(t1DistList, t1MatchErrList, "r--", linewidth=2, label=u"本文提出的算法")
    # t1Axes.set_xlim(0, 60)
    # t1Axes.set_ylim(0.5, 1.1)
    # t1Axes.xaxis.set_major_locator(MultipleLocator(10))
    # t1Axes.xaxis.set_minor_locator(MultipleLocator(5))
    # t1Axes.yaxis.set_major_locator(MultipleLocator(0.1))
    # t1Axes.yaxis.set_minor_locator(MultipleLocator(0.05))
    t1Axes.grid(True)
    t1Axes.legend(loc=2)

    t2Axes = fig.add_subplot(122)
    t2Axes.set_xlabel(u"运动距离(米)")
    t2Axes.set_ylabel(u"定位误差(米)")
    t2Axes.plot(t2DistList, t2PdrErrList, "b-", linewidth=2, label=u"航位推算")
    t2Axes.plot(t2DistList, t2MatchErrList, "r--", linewidth=2, label=u"本文提出的算法")
    # t1Axes.set_xlim(0, 60)
    # t1Axes.set_ylim(0.5, 1.1)
    # t1Axes.xaxis.set_major_locator(MultipleLocator(10))
    # t1Axes.xaxis.set_minor_locator(MultipleLocator(5))
    # t1Axes.yaxis.set_major_locator(MultipleLocator(0.1))
    # t1Axes.yaxis.set_minor_locator(MultipleLocator(0.05))
    t2Axes.grid(True)
    t2Axes.legend(loc=2)

    plt.show()
    pass

if __name__ == "__main__":
    showPosError()
    print("Done.")
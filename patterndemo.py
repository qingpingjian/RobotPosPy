#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2018/4/12 10:29
@author: Pete
@email: yuwp_1985@163.com
@file: patterndemo.py
@software: PyCharm Community Edition
"""
import math
import matplotlib
import matplotlib.pyplot as plt

from matplotlib.ticker import  MultipleLocator, FormatStrFormatter

from comutil import *
from dataloader import loadAcceData, loadGyroData

# Environment Configuration
matplotlib.rcParams['font.size'] = 15
# matplotlib.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签
matplotlib.rcParams['font.sans-serif'] = ["simsun"] # 用来正常显示中文标签
matplotlib.rcParams['axes.unicode_minus'] = False # 用来正常显示负号

if __name__ == "__main__":
    sensorFilePath = ("./Examples/PatternDetect/20170622153925_acce.csv",
                      "./Examples/PatternDetect/20170622153925_gyro.csv")

    # Load accelerometer data from files
    acceTimeList, acceValueList = loadAcceData(sensorFilePath[0], combineFlag = True)
    windowSize = 7
    acceVotList, acceVarList = varOfAcce(acceTimeList, acceValueList, windowSize)

    # Stationary
    timeListForStat = acceVotList[51:341]
    timeListForStat = [t - timeListForStat[0] for t in timeListForStat]
    valueListForStat = acceVarList[51:341]

    # Forward or Backward
    timeListForWalk = acceVotList[1511:1801]
    timeListForWalk = [t - timeListForWalk[0] for t in timeListForWalk]
    valueListForWalk = acceVarList[1511:1801]

    gyroTimeList, gyroValueList = loadGyroData(sensorFilePath[1])
    windowSize = 21
    gyroTimeFltList, gyroValueFltList = slidingWindowFilter(gyroTimeList, gyroValueList, windowSize)

    # Normal motion
    timeListForNW = gyroTimeFltList[1101:1601]
    timeListForNW = [t - timeListForNW[0] for t in timeListForNW]
    valueListForNW = gyroValueFltList[1101:1601]

    # Turns
    timeListForTurns = gyroTimeFltList[2581:3081]
    timeListForTurns = [t - timeListForTurns[0] for t in timeListForTurns]
    valueListForTurns = gyroValueFltList[2581:3081]

    # Right and Left turn
    timeListForLeft = gyroTimeList[1781:2281]
    gyroListForLeft = gyroValueList[1781:2281]
    timeListForLeft = [t - timeListForLeft[0] for t in timeListForLeft]
    rotAngleListForLeft = rotationAngle(timeListForLeft, gyroListForLeft, normalize=False)
    rotDegreeListForLeft = [r * 180.0 / math.pi for r in rotAngleListForLeft]

    # Turn around
    timeListForUTurn = gyroTimeList[2581:3081]
    gyroListForUTurn = gyroValueList[2581:3081]
    timeListForUTurn = [t - timeListForUTurn[0] for t in timeListForUTurn]
    rotAngleListForUTurn = rotationAngle(timeListForUTurn, gyroListForUTurn, normalize=False)
    rotDegreeListForUTurn = [r * -180.0 / math.pi for r in rotAngleListForUTurn]

    fig = plt.figure()
    statSeparateAxe = fig.add_subplot(311)
    statSeparateAxe.set_ylim(0.0, 3.0)
    statSeparateAxe.yaxis.set_major_locator(MultipleLocator(1.0))
    statSeparateAxe.yaxis.set_major_formatter(FormatStrFormatter("%.1f"))
    statSeparateAxe.yaxis.set_minor_locator(MultipleLocator(0.5))
    statSeparateAxe.set_xticks([]) # Hidden the x ticks
    statSeparateAxe.set_ylabel(u"加速度方差")
    # statSeparateAxe.set_xlabel(u"时间(s)")
    statSeparateAxe.plot(timeListForStat, valueListForStat, color="red", lw=3, linestyle="--", label=u"静止")
    statSeparateAxe.plot(timeListForWalk, valueListForWalk, color="blue", lw=3, linestyle="-", label=u"直行")
    plt.legend(loc=2)

    walkSeparateAxe = fig.add_subplot(312)
    walkSeparateAxe.set_ylim(-3.0, 2.0)
    walkSeparateAxe.yaxis.set_major_locator(MultipleLocator(1.0))
    walkSeparateAxe.yaxis.set_major_formatter(FormatStrFormatter("%.1f"))
    walkSeparateAxe.yaxis.set_minor_locator(MultipleLocator(0.5))
    walkSeparateAxe.set_xticks([]) # Hidden the x ticks
    walkSeparateAxe.set_ylabel(u"角速度(rad/s)")
    # walkSeparateAxe.set_xlabel(u"时间(s)")
    walkSeparateAxe.plot(timeListForNW, valueListForNW, color="red", lw=3, linestyle="-", label=u"直行")
    walkSeparateAxe.plot(timeListForTurns, valueListForTurns, color="blue", lw=3, linestyle="--", label=u"转弯")
    plt.legend(loc="best")

    turnSeparateAxe = fig.add_subplot(313)
    turnSeparateAxe.set_ylim(-50, 200)
    turnSeparateAxe.yaxis.set_major_locator(MultipleLocator(50))
    turnSeparateAxe.yaxis.set_major_formatter(FormatStrFormatter("%d"))
    turnSeparateAxe.yaxis.set_minor_locator(MultipleLocator(25))
    # turnSeparateAxe.set_xticks([]) # Hidden the x ticks
    turnSeparateAxe.set_ylabel(u"旋转角度(rad)")
    turnSeparateAxe.set_xlabel(u"时间(s)")
    turnSeparateAxe.plot(timeListForLeft, rotDegreeListForLeft, color="blue", lw=3, label=u"左转")
    turnSeparateAxe.plot(timeListForUTurn, rotDegreeListForUTurn, color="red", lw=3, label=u"掉头", linestyle="--")
    plt.legend(loc=2)

    plt.show()

    print("Done.")
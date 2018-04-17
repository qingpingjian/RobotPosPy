#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2018/4/13 8:46
@author: Pete
@email: yuwp_1985@163.com
@file: robotpdr.py
@software: PyCharm Community Edition
"""
import matplotlib
import matplotlib.pyplot as plt

from comutil import *
from dataloader import loadAcceData, loadGyroData


# Environment Configuration
matplotlib.rcParams['font.size'] = 15
# matplotlib.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签
matplotlib.rcParams['font.sans-serif'] = ["simsun"] # 用来正常显示中文标签
matplotlib.rcParams['axes.unicode_minus'] = False # 用来正常显示负号

def simplePDR(startPattern, acceTimeList, acceValueList, gyroTimeList, gyroValueList):
    speedTimeList, speedValueList = motionSpeed(acceTimeList, acceValueList)
    rotTimeList, rotValueList = rotationAngle(gyroTimeList, gyroValueList)

    estLoc = [(startPattern[2], startPattern[3])]
    for i in range(len(speedTimeList)):

        pass
    pass

if __name__ == "__main__":
    sensorFilePath = ("./Examples/PDRTest/20170622153925_acce.csv",
                      "./Examples/PDRTest/20170622153925_gyro.csv")
    startPattern = (0.0, 0.0, 48.4, 2.1) # (init_speed, init_direction, init_x, init_y)
    # Load accelerometer data from files
    acceTimeList, acceValueList = loadAcceData(sensorFilePath[0], relativeTime=False)
    gyroTimeList, gyroValueList = loadGyroData(sensorFilePath[1], relativeTime=False)

    print("Done.")
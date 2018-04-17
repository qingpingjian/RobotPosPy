#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2018/4/12 10:20
@author: Pete
@email: yuwp_1985@163.com
@file: dataloader.py.py
@software: PyCharm Community Edition
"""
import math
import pandas as pd

TIMESTAMP_BASELINE = 1490000000000

def loadAcceData(filePath, relativeTime = True):
    acceDF = pd.read_csv(filePath)
    acceInfo = acceDF.ix[:,['timestamp', 'acce_x', 'acce_y', 'acce_z']]
    acceTimeList = []
    acceValueList = []
    for acceRecord in acceInfo.values:
        acceTimeList.append((acceRecord[0] - TIMESTAMP_BASELINE)/ 1000.0) # milliseconds to seconds
        xAxis = acceRecord[1]
        yAxis = acceRecord[2]
        # zAxis = acceRecord[3]
        acceValueList.append(xAxis)
    if relativeTime:
        acceTimeList = [(t - acceTimeList[0]) for t in acceTimeList]
    return acceTimeList, acceValueList


def loadGyroData(filePath, relativeTime = True):
    gyroDF = pd.read_csv(filePath)
    gyroInfo = gyroDF.ix[:, ["timestamp", "gyro_z"]]
    gyroTimeList = []
    gyroValueList = []
    for gyroRecord in gyroInfo.values:
        gyroTimeList.append((gyroRecord[0] - TIMESTAMP_BASELINE) / 1000.0) # milliseconds to seconds
        gyroValueList.append(gyroRecord[1])
    if relativeTime:
        gyroTimeList = [(t - gyroTimeList[0]) for t in gyroTimeList]
    return gyroTimeList, gyroValueList

if __name__ == "__main__":
    print("Done.")
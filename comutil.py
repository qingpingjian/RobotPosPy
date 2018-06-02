#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2018/4/12 11:09
@author: Pete
@email: yuwp_1985@163.com
@file: comutil.py.py
@software: PyCharm Community Edition
"""
import math
import numpy as np

from anglefunc import angleNormalize
from dataloader import loadAcceData, loadGyroData

def slidingWindowFilter(timeList, valueList, windowSize):
    midPos = (windowSize - 1) / 2
    currentIndex = 0
    dataLength = np.min((len(timeList), len(valueList)))
    timeFList = timeList[0:dataLength]
    valueFList = []
    valueFList.extend(valueList[currentIndex:currentIndex + midPos])
    valueFList.extend([np.mean(valueList[i - midPos : i + midPos + 1])
                       for i in range(currentIndex + midPos, dataLength - midPos)])
    valueFList.extend(valueList[dataLength - midPos:dataLength])
    return timeFList, valueFList

def varOfAcce(timeList, valueList, windowSize):
    midPos = (windowSize - 1) / 2
    votList = [timeList[i] for i in range(midPos, len(valueList) - midPos)]
    varList = [np.var(valueList[i - midPos:i + midPos + 1]) for i in range(midPos, len(valueList) - midPos)]
    return votList, varList

def motionSpeed(acceTimeList, acceValueList):
    """
    :param acceTimeList:
    :param acceValueList:  We use the x axis of accelerometer to derivate the motion speed
    :return:
    """
    acceAvgList = [acceValueList[0]]
    acceAvgList.extend([(acceValueList[i - 1] + acceValueList[i]) / 2.0 for i in range(1, len(acceValueList))])

    speedValueList = [0.0]
    for j in range(1, len(acceAvgList)):
        # TODO: 手机放到小车上之后会产生误差速度的累计误差怎么办？
        speedValueList.append((acceTimeList[j] - acceTimeList[j-1]) * (acceAvgList[j] if math.fabs(acceAvgList[j]) > 0.1268 else 0.0) + speedValueList[j-1])
    return acceTimeList, speedValueList

def rotationAngle(gyroTimeList, gyroValueList, normalize = True):
    """
    clockwise rotation return position values and keep rotation angle in [0, 2pi) based on normalize flag
    :param gyroTimeList: Gyroscope data timestamp
    :param gyroValueList: Gyroscope data list
    :param normalize: normalize flag
    :return: rotation angle in radian
    """
    # Between two timestamps, we use the average value as the real rate.
    avgList = [gyroValueList[0]]
    avgList.extend([(gyroValueList[i - 1] + gyroValueList[i]) / 2.0 for i in range(1, len(gyroValueList))])

    integrationList = [0.0]
    for j in range(1, len(avgList)):
        integrationList.append((gyroTimeList[j] - gyroTimeList[j - 1]) * avgList[j] + integrationList[j - 1])
    # clockwise rotation return position values and keep rotation angle in {0, 2pi) based on circularData flag
    rotValueList = [angleNormalize(-1.0 * rot) if normalize else (-1.0 * rot) for rot in integrationList]
    return gyroTimeList, rotValueList

def agTimeAlign(acceTimeList, gyroTimeList):
    a2gIndexList = []
    gyroStartIndex = 0
    for i in range(len(acceTimeList)):
        # if the accelerometer time is smaller than the first gyroscope time,
        # then the rotation angle should be initial angle.
        if acceTimeList[i] < gyroTimeList[0] or math.fabs(acceTimeList[i] - gyroTimeList[0]) < 0.002:
            a2gIndexList.append(0)
            continue
        # bigger than the last gyroscope time
        if acceTimeList[i] > gyroTimeList[-1] or math.fabs(acceTimeList[i] - gyroTimeList[-1]) < 0.002:
            a2gIndexList.append(len(gyroTimeList)-1)
            continue
        for j in range(gyroStartIndex, len(gyroTimeList)):
            if math.fabs(acceTimeList[i] - gyroTimeList[j]) < 0.002:
                a2gIndexList.append(j)
                gyroStartIndex = j + 1
                break
            baseTime = acceTimeList[i]
            # Now, the gyroscope should be determined
            if gyroTimeList[j] > baseTime:
                targetIndex = j if gyroTimeList[j] - baseTime < baseTime - gyroTimeList[j-1] else j - 1
                a2gIndexList.append(targetIndex)
                gyroStartIndex = targetIndex + 1
                break
    return a2gIndexList

if __name__ == "__main__":
    sensorFilePath = ("./Examples/PDRTest/20170622153925_acce.csv",
                      "./Examples/PDRTest/20170622153925_gyro.csv")
    # Load accelerometer data from files
    acceTimeList, acceValueList = loadAcceData(sensorFilePath[0], relativeTime=False)
    gyroTimeList, gyroValueList = loadGyroData(sensorFilePath[1], relativeTime=False)
    agTimeAlign(acceTimeList, gyroTimeList)
    print("Done.")
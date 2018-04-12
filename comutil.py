#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2018/4/12 11:09
@author: Pete
@email: yuwp_1985@163.com
@file: comutil.py.py
@software: PyCharm Community Edition
"""
import numpy as np

from anglefunc import angleNormalize

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

def rotationAngle(gyroTimeList, gyroValueList, normalize = True):
    """
    clockwise rotation return position values and keep rotation angle in {0, 2pi) based on normalize flag
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
    return [angleNormalize(-1.0 * rot) if normalize else (-1.0 * rot) for rot in integrationList]

if __name__ == "__main__":
    print("Done.")
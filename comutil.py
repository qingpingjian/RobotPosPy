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

def varOfAcce(timeList, valueList, windowSize):
    midPos = (windowSize - 1) / 2
    votList = [timeList[i] for i in range(midPos, len(valueList) - midPos)]
    varList = [np.var(valueList[i - midPos:i + midPos + 1]) for i in range(midPos, len(valueList) - midPos)]
    return votList, varList

if __name__ == "__main__":
    print("Done.")
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2018/6/4 17:00
@author: Pete
@email: yuwp_1985@163.com
@file: timediff.py
@software: PyCharm Community Edition
"""
import numpy as np

marker360List = [
    1528102619347,
    1528102624685,
    1528102625595,
    1528102626300,
    1528102626886,
    1528102641263,
    1528102641831,
    1528102642349,
    1528102690684,
    1528102691460
]

markerHuaweiList = [
    1528102617235,
    1528102622541,
    1528102623468,
    1528102624164,
    1528102624769,
    1528102639179,
    1528102639708,
    1528102640223,
    1528102688571,
    1528102689383
]

if __name__ == "__main__":
    print np.array(marker360List) - np.array(markerHuaweiList)
    print np.mean(np.array(marker360List) - np.array(markerHuaweiList), axis=0)
    print("Done.")
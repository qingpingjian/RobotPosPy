#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2018/3/1 22:32
@author: Pete
@email: yuwp_1985@163.com
@file: abstractmap.py
@software: PyCharm Community Edition
"""
"""
B <--> C <--> E      M <--> L
A <--> D <--> F <--> H <--> I
                     K <--> J
"""
#  0, 1, 2, 3, 4   go straight 0, left turn 1, right turn 2, left around 3, right around 4
building1305New = {
    "nodes":{"seg201":(1.3, 41.6, 3.14159,  1.3, 90.2, 0.0), # (AB)
             "seg202":(1.3, 90.2, 4.71239,  74.05, 90.2, 1.5708), # (BC)
             "seg203":(74.05, 90.2, 0.0,  74.05, 41.6, 3.14159), # (CD)
             "seg204":(74.05, 90.2, 4.71239, 81.25, 90.2, 1.5708),  # (CE)
             "seg205":(74.05, 41.6, 1.5708,  1.3, 41.6, 4.71239), # (DA)
             "seg206":(74.05, 41.6, 4.71239, 84.85, 41.6, 1.5708), # (DF)
             "seg207":(84.85, 41.6, 4.71239,  131.1, 41.6, 1.5708), # (FH)
             "seg208":(131.1, 41.6, 4.71239,  183.1, 41.6, 1.5708), # (HI)
             "seg209":(183.1, 41.6, 0.0,  183.1, 1.2, 3.14159), # (IJ)
             "seg210":(183.1, 1.2, 1.5708, 124.7, 1.2, 4.71239), # (JK)
             "seg211":(183.1, 41.6, 3.14159, 183.1, 90.25, 0.0), # (IL)
             "seg212":(183.1, 90.25, 1.5708, 124.7, 90.25, 4.71239), # (LM)
    },
    "edges": (("seg201", "seg201", 3),
              ("seg201", "seg201", 4),
              ("seg201", "seg202", 2, 1.3, 90.2),
              ("seg201", "seg205", 1, 1.3, 41.6),
              ("seg202", "seg202", 3),
              ("seg202", "seg202", 4),
              ("seg202", "seg201", 1, 1.3, 90.2),
              ("seg202", "seg203", 2, 74.05, 90.2),
              ("seg202", "seg204", 0, 74.05, 90.2),
              ("seg203", "seg203", 3),
              ("seg203", "seg203", 4),
              ("seg203", "seg202", 1, 74.05, 90.2),
              ("seg203", "seg204", 2, 74.05, 90.2),
              ("seg203", "seg205", 2, 74.05, 41.6),
              ("seg203", "seg206", 1, 74.05, 41.6),
              ("seg204", "seg204", 3),
              ("seg204", "seg204", 4),
              ("seg204", "seg202", 0, 74.05, 90.2),
              ("seg204", "seg203", 1, 74.05, 90.2),
              ("seg205", "seg205", 3),
              ("seg205", "seg205", 4),
              ("seg205", "seg206", 0, 74.05, 41.6),
              ("seg205", "seg203", 1, 74.05, 41.6),
              ("seg205", "seg201", 2, 1.3, 41.6),
              ("seg206", "seg206", 3),
              ("seg206", "seg206", 4),
              ("seg206", "seg205", 0, 74.05, 41.6),
              ("seg206", "seg203", 2, 74.05, 41.6),
              ("seg206", "seg207", 0, 84.85, 41.6),
              ("seg207", "seg207", 3),
              ("seg207", "seg207", 4),
              ("seg207", "seg206", 0, 84.85, 41.6),
              ("seg207", "seg208", 0, 131.1, 41.6),
              ("seg208", "seg208", 3),
              ("seg208", "seg208", 4),
              ("seg208", "seg207", 0, 131.1, 41.6),
              ("seg208", "seg209", 2, 183.1, 41.6),
              ("seg208", "seg211", 1, 183.1, 41.6),
              ("seg209", "seg209", 3),
              ("seg209", "seg209", 4),
              ("seg209", "seg208", 1, 183.1, 41.6),
              ("seg209", "seg211", 0, 183.1, 41.6),
              ("seg209", "seg210", 2, 183.1, 1.2),
              ("seg210", "seg210", 3),
              ("seg210", "seg210", 4),
              ("seg210", "seg209", 1, 183.1, 1.2),
              ("seg211", "seg211", 3),
              ("seg211", "seg211", 4),
              ("seg211", "seg209", 0, 183.1, 41.6),
              ("seg211", "seg208", 2, 183.1, 41.6),
              ("seg211", "seg212", 1, 183.1, 90.25),
              ("seg212", "seg212", 3),
              ("seg212", "seg212", 4),
              ("seg212", "seg211", 2, 183.1, 90.25),
              ),
}

import math
import numpy as np
import sys
from anglefunc import angleNormalize, isHeadingMatch

class DigitalMap(object):
    def __init__(self, mapGraph=building1305New, logFlag=True):
        self.mapGraph = mapGraph
        self.nodesDict = mapGraph.get("nodes")
        self.edgesArray = mapGraph.get("edges")
        self.logFlag = logFlag
        self.initProb = -4.5 if logFlag else math.exp(-4.5)  # -4.5 = -1.0*(3delta)^2 / (2delta^2) about 0.0111
        self.minProb = -15.0 if logFlag else math.exp(-15)  # 3.059023205018258e-07
        return

    def isRelated(self, onePoint, otherPoint):
        """
        If it is reachable from onePoint to otherPoint through normal walking or another activities
        return true, otherwise, return false
        :param onePoint:  The end point of last segment
        :param otherPoint:  the start point of current segment
        :return:  True or False
        """
        return math.fabs(onePoint[0] - otherPoint[0]) < sys.float_info.epsilon and \
                math.fabs(onePoint[1] - otherPoint[1]) < sys.float_info.epsilon

    def isSamePoint(self, onePoint, otherPoint):
        return math.fabs(onePoint[0] - otherPoint[0]) < sys.float_info.epsilon and \
                math.fabs(onePoint[1] - otherPoint[1]) < sys.float_info.epsilon

    def getAnotherPoint(self, segID, onePoint):
        segAttr = self.nodesDict.get(segID)
        firstPoint = (segAttr[0], segAttr[1])
        secondPoint = (segAttr[3], segAttr[4])
        return secondPoint if self.isSamePoint(onePoint, firstPoint) else firstPoint

    def getDirection(self, segID, referencePoint, headingFlag=True):
        """
        Get the heading direction, if headingFlag is True, the reference Point is in the front
        or it is in the back
        :param segID: segment identifiy, note that the user must be walking on the segment now
        :param referencePoint: the heading front point or the coming back point
        :param headingFlag: a flag value to indicate that the reference point location
        :return: heading direction
        """
        segAttr = self.nodesDict.get(segID)
        firstPoint = (segAttr[0], segAttr[1])
        heading = segAttr[2]
        if headingFlag: # Point is in the front, so the coming heading of point is the heading
            heading = segAttr[2] if self.isSamePoint(referencePoint, firstPoint) else segAttr[5]
        else:
            heading = segAttr[5] if self.isSamePoint(referencePoint, firstPoint) else segAttr[2]
        return heading

    def extendSegment(self, segID, endPoint):
        for edge in self.edgesArray:
            if len(edge) == 3:
                continue
            passedPoint = (edge[3], edge[4])
            if edge[0] == segID and edge[2] == 0 and self.isRelated(endPoint, passedPoint):
                return edge[1], self.getAnotherPoint(edge[1], passedPoint)

    def getSegmentLength(self, segIDArray):
        # TODO: Here, we donot check the segments are all in a straight narrow corridor
        length = 0.0
        # Try to sum all the length of input segments
        for segID in segIDArray:
            segAttr = self.nodesDict.get(segID)
            length = length + math.sqrt(math.pow(segAttr[0] - segAttr[3], 2) + math.pow(segAttr[1] - segAttr[4], 2))
        return length

    def extractSegmentByDir(self, walkingDir=0.0):
        """
        [startX, startY, endX, endY, ['s1', 's2', ..., 'sk'], probLastTime, probCurrent, pLastSegment, extendStatus]
        :param walkingDir: base direction to select segments candidate
        :return: segments candidate, the pLastProb is set to minProb firstly,
        and the extend status is set to zero, (0, 1, ..., possible counter num in a straight corridor)
        """
        normalWalkDir = angleNormalize(walkingDir)
        candidateList = []
        for id, attr in self.nodesDict.iteritems():
            firstAccessDir = attr[2]  # The accessible direction of the first endpoint
            secondAccessDir = attr[5]  # The accessible direction of the second endpoint
            if isHeadingMatch(normalWalkDir, firstAccessDir):
                # The second point is starting point and the first point is the next point
                candidateList.append([attr[3], attr[4], attr[0], attr[1], [id], self.initProb, self.initProb, self.minProb, 0])
            elif isHeadingMatch(normalWalkDir, secondAccessDir):
                candidateList.append([attr[0], attr[1], attr[3], attr[4], [id], self.initProb, self.initProb, self.minProb, 0])
        return candidateList

    def extractSegmentByDirAndStartPoint(self, walkingDir=0.0, startPoint=(1.2, 1.7)):
        """
        [startX, startY, endX, endY, ['s1', 's2', ..., 'sk'], probLastTime, probCurrent, pLastSegment, extendStatus]
        :param walkingDir: base direction to select segments candidate
        :return: segments candidate, the pLastProb is set to minProb firstly,
        and the extend status is set to zero, (0, 1, ..., possible counter num in a straight corridor)
        """
        normalWalkDir = angleNormalize(walkingDir)
        startX = startPoint[0]
        startY = startPoint[1]
        candidateList = []
        for id, attr in self.nodesDict.iteritems():
            firstAccessDir = attr[2]  # The accessible direction of the first endpoint
            secondAccessDir = attr[5]  # The accessible direction of the second endpoint
            if isHeadingMatch(normalWalkDir, firstAccessDir) and self.isSamePoint(startPoint, (attr[3], attr[4])):
                # The second point is starting point and the first point is the next point
                candidateList.append([attr[3], attr[4], attr[0], attr[1], [id], self.initProb, self.initProb, self.minProb, 0])
            elif isHeadingMatch(normalWalkDir, secondAccessDir) and self.isSamePoint(startPoint, (attr[0], attr[1])):
                candidateList.append([attr[0], attr[1], attr[3], attr[4], [id], self.initProb, self.initProb, self.minProb, 0])
        return candidateList

    def emissionProb(self, stepLength, stepNum, stepStd, segIDArray):
        travelDist = stepLength * stepNum
        distStd = stepStd * stepNum
        segLength = self.getSegmentLength(segIDArray)
        # TODO: the emission probability
        probValue = self.initProb
        if travelDist + 3 * distStd > segLength:
            probValue = math.exp((((travelDist - segLength) ** 2) / (2 * distStd ** 2)) * (-1.0))
            if self.logFlag:
                probValue = math.log(probValue)
        return probValue

    def nextCandidateByActivity(self, lastSeg, turnType, overPoint, currentProb):
        nextCandidate = None
        for edge in self.edgesArray:
            if edge[0] != lastSeg or edge[2] != turnType:
                continue
            if turnType == 3 or turnType == 4:  # turn around
                endPoint = self.getAnotherPoint(edge[1], overPoint)
                nextCandidate = [overPoint[0], overPoint[1], endPoint[0], endPoint[1], [edge[1]], self.initProb, self.initProb, currentProb, 0]
                break
            elif len(edge) == 5 and (turnType == 1 or turnType == 2): # left or right turn
                passedPoint = (edge[3], edge[4])
                if self.isRelated(overPoint, passedPoint):
                    endPoint = self.getAnotherPoint(edge[1], passedPoint)
                    nextCandidate = [passedPoint[0], passedPoint[1], endPoint[0], endPoint[1], [edge[1]], self.initProb, self.initProb, currentProb, 0]
                    break
        return nextCandidate

    def getSegmentSeparatePoint(self, firstSeg, secondSeg):
        # TODO: we do not need to find separete points between the same segment
        if firstSeg == secondSeg:
            print("I have received two same segments to separate, what's happeded ?")
            return None
        separatePoint = None
        for edge in self.edgesArray:
            if len(edge) > 3 and edge[0] == firstSeg and edge[1] == secondSeg:
                separatePoint = (edge[3], edge[4])
                break
        return separatePoint

    def selectSegment(self, locPoint, segIDArray):
        # Direction judgement
        targetSeg = segIDArray[0]
        attr = self.nodesDict.get(targetSeg)
        if math.fabs(attr[0] - attr[3]) < 0.1: # Have the same x coordinate
            yLoc = locPoint[1]
            for segID in segIDArray:
                segAttr = self.nodesDict.get(segID)
                if math.fabs(segAttr[1]-yLoc) + math.fabs(segAttr[4]-yLoc) < math.fabs(segAttr[1] - segAttr[4]) + 0.1:
                    targetSeg = segID
                    break
        else:
            xLoc = locPoint[0]
            for segID in segIDArray:
                segAttr = self.nodesDict.get(segID)
                if math.fabs(segAttr[0]-xLoc) + math.fabs(segAttr[3]-xLoc) < math.fabs(segAttr[0] - segAttr[3]) + 0.1:
                    targetSeg = segID
                    break
        return targetSeg


if __name__ == "__main__":
    # Emission Probability
    stepLength = 0.74
    stepStd = 0.1
    testMap = DigitalMap(logFlag=True)
    for segID, attr in testMap.nodesDict.iteritems():
        segLength = testMap.getSegmentLength([segID])
        probList = []
        for n in range(1, 40):
            probList.append(testMap.emissionProb(stepLength, n, stepStd, [segID]))
        # print segID,
        # print(probList)
        if probList[-1] <= testMap.minProb:
            print("Try to extend %s due to the current prob. %.5f" % (segID, probList[-1]))
    # testing selectSegment
    locPoint = (48.20655737704918, 10.7)
    segArray = ["seg20", "seg19", "seg18", "seg17"]
    print(testMap.selectSegment(locPoint, segArray))
    print("Done.")
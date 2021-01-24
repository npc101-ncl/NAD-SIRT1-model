#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 16:56:35 2021

@author: peter
"""

from python.visualisationTools import *
from python.utilityTools import *
from python.analysisTools import *

i = 2
name = "reConf9"
nameB = "reConf7"

def SVGet(TC):
    showValues = [j for j in TC[0].columns if "Time"!=j]
    for v in ["_k1","_V","_h","_Shalve","_k","_v"]:
        showValues = [j for j in showValues if not j.endswith(v)]
    showValues = [showValues[20*i:20*(i+1)] for i
                  in range(1+len(showValues)//20)]
    showValues = [j for j in showValues if len(j)>0]
    return showValues

RS = loadPick(['data',name,'runSwitches.p'], relative=True)

RSB = loadPick(['data',nameB,'runSwitches.p'], relative=True)

newParams = loadPick(['data',name,'new-params.p'], relative=True)

indexCutoff = range(min(3,
                        RSSClusterEstimation(GFID(newParams))[0]["size"]))

newParams = loadPick(['data',nameB,'new-params.p'], relative=True)

indexCutoffB = range(min(3,
                        RSSClusterEstimation(GFID(newParams))[0]["size"]))

timeCourses = loadPick(['data',name,'new-timeCourses'+
                        str(i)+'.p'], relative=True)
timeCoursesB = loadPick(['data',nameB,'new-timeCourses'+
                         str(i)+'.p'], relative=True)

showValues = SVGet(timeCourses)

showValuesB = SVGet(timeCoursesB)

tcvis = timeCourseVisualiser(timeCourses)
tcvisB = timeCourseVisualiser(timeCoursesB)

for j in showValues:
    tcvis.multiPlot(indexSelect = list(indexCutoff), varSelect = j,
                    compLines = RS['calDf'][i])
for j in showValuesB:
    tcvisB.multiPlot(indexSelect = list(indexCutoffB), varSelect = j,
                    compLines = RSB['calDf'][i])
    

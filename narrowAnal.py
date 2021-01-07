#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 14:16:14 2020

@author: peter
"""

from python.visualisationTools import *
from python.analysisTools import *
from python.utilityTools import *
import os, re, sys
import pandas as pd
import pickle
import seaborn as sns
import matplotlib.pyplot as plt

cmdDict, cmdFlag = getCmdLineArgs()

def showValsFunc(timeCourses,newParams):
    showValues = list(timeCourses[0].columns)
    showValues = [val for val in showValues
                  if not val in GFID(newParams).columns]
    showValues = [val for val in showValues
                  if not (val.endswith("_k1") or val.endswith("_V")
                  or val.endswith("_Shalve") or val.endswith("_h") 
                  or val.endswith("_v"))]
    showValues = [val for val in showValues
                  if not val in ["Time","quantity to number factor",
                                 "initial_NAD"]]
    return showValues 

name = [name[5:] for name in cmdDict if (name.startswith("name:") and 
        len(name)>5)]
if len(name)>0:
    name = name[0]
else:
    name = "reConf7"

RS = loadPick(["data",name,'runSwitches.p'], relative=True)

param = loadPick(["data",name,'narrow-params.p'], relative=True)

timeCourses = loadPick(["data",name,'narrow-timeCourses.p'],
                        relative=True)

PEVis = parameterEstimationVisualiser(param)
PEVis.waterFall(save=resolvePath(['figures',name,'narrow-waterfall.png'],
                                 relative=True),
                indexNames="parameters")
        
indexCutoff = range(min(100, RSSClusterEstimation(GFID(param))[0]["size"]))

showValues = list(timeCourses[0].columns)
print(showValues)
for myParam in list(GFID(param).columns):
    try:
        showValues.remove(myParam)
    except ValueError:
        pass
try:
    showValues.remove("NAD_fold_increase")
except ValueError:
    pass

showValues = [val for val in showValues
              if not (val.endswith("_k1") or val.endswith("_V")
              or val.endswith("_Shalve") or val.endswith("_h") 
              or val.endswith("_v"))]
showValues = [val for val in showValues
              if not val in ["Time","quantity to number factor",
                             "initial_NAD"]]

from python.analysisTools import *
temp = paramPCA(GFID(param).iloc[indexCutoff])

        
for i, myDF in zip(range(len(RS["calDf"])),RS["calDf"]):
    timeCourses = loadPick(["data",name,'narrow-timeCourses'+str(i)+'.p'],
                           relative=True)
    TCVis = timeCourseVisualiser(timeCourses)
    TCVis.multiPlot(indexSelect=list(indexCutoff),compLines=myDF,
                    varSelect=showValues,
                    save=resolvePath(['figures',name,'timeCourseCalW'+
                                      str(i)+'.png'],
                                     relative=True))

myComp = [i for i in range(len(temp['cumVarExp']))
          if temp['cumVarExp'][i]<=0.9]

for j in myComp:   
    for i, myDF in zip(range(len(RS["calDf"])),RS["calDf"]):
        timeCourses = loadPick(["data",name,'narrow-timeCourses'+str(i)+'.p'],
                               relative=True)
        TCVis = timeCourseVisualiser(timeCourses)
        tempMin = temp['newPoints'].iloc[:,j].min()
        tempMax = temp['newPoints'].iloc[:,j].max()
        tempColours = (temp['newPoints'].iloc[:,j]-tempMin)/(tempMax-tempMin)
        tempColours = list(tempColours)
        TCVis.multiPlot(indexSelect=list(indexCutoff),compLines=myDF,
                        varSelect=showValues, colourOverride=tempColours,
                        save=resolvePath(['figures',name,'timeCourseCalW'+
                                          str(i)+"-"+str(j)+'.png'],
                                         relative=True))


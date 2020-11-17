#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 13:09:12 2020

@author: peter
"""

import site, os, re
import pandas as pd
from python.pycotoolsHelpers import *
from python.utilityTools import *
import pickle
import time, sys

cmdDict, cmdFlags = getCmdLineArgs()

working_directory = os.path.dirname(os.path.abspath(__file__))

mySuperComputer = "slurm" in cmdFlags

if "name" in cmdDict.keys():
    name = cmdDict["name"]
else:
    name = "reConf7"
    
newParams = loadPick(['data', name,'new-params.p'],relative=True)
RS = loadPick(['data', name,'runSwitches.p'],relative=True)

if "row" in cmdDict.keys():
    selectedRow = int(cmdDict["row"])
    if selectedRow<0:
        selectedRow=0
    if len(GFID(newParams))<=selectedRow:
        selectedRow=len(GFID(newParams))-1
else:
    selectedRow = 0
    
if not mySuperComputer:
    addCopasiPath("/Applications/copasi")
    
run_dir = os.path.join(working_directory, 'copasiRuns', 'AICAR'+name)
if not os.path.isdir(run_dir):
    os.makedirs(run_dir)
    
myModel = modelRunner(RS["antimony_string"], run_dir)

myOverride = GFID(newParams).iloc[selectedRow]

if "points" in cmdDict.keys():
    points = int(cmdDict["points"])
else:
    points = 5
    
if "max" in cmdDict.keys():
    maxAICAR = int(cmdDict["max"])
else:
    maxAICAR = 4

AICARlevels = [maxAICAR*i/(points-1) for i in range(points)]

myOverrideC = []
for AICAR in AICARlevels:
    myOverrideB = myOverride.copy()
    myOverrideB["AICAR"] = AICAR
    myOverrideC.append(myOverrideB)

myOverrideC = pd.DataFrame(myOverrideC)
myOverrideC = myOverrideC.drop(columns=["RSS"])
myOverrideC = myOverrideC.reset_index()

timeCourse = myModel.runTimeCourse(24, adjustParams=myOverrideC,
                                   stepSize=0.25)

savePick(["data",name,"aicarTimeCourses.p"], timeCourse, relative=True)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 17:22:07 2020

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

# set bounds
myUpperBound=1000
myLowerBound=0.0001

mySuperComputer = "slurm" in cmdFlags

if "name" in cmdDict.keys():
    name = cmdDict["name"]
else:
    name = "reConf7"
    
if "points" in cmdDict.keys():
    points = int(cmdDict["points"])
    if points%2 == 0:
        points = points+1
else:
    points = 3
    
if "perLog10" in cmdDict.keys():
    perLog10 = float(cmdDict["perLog10"])
else:
    perLog10 = 1
    
if "lower" in cmdDict.keys():
    lowerAdjR = float(cmdDict["lower"])
    if lowerAdjR>=1:
        lowerAdjR = 0.1
else:
    lowerAdjR = 0.1
    
if "meth" in cmdDict.keys():
    methDict = cmdDict["meth"]
    methDict = [l.split(":") for l in methDict.split(",")]
    methDict = {l[0]:l[1] for l in methDict if len(l)==2}
    for mKey in methDict.keys():
        try:
            methDict[mKey] = float(methDict[mKey])
            if methDict[mKey].is_integer():
                methDict[mKey] = int(methDict[mKey])
        except:
            pass
else:
    methDict = None
    
if "depth" in cmdDict.keys():
    myDepth = cmdDict["depth"]
    try:
        myDepth = int(myDepth)
    except:
        myDepth = 3
else:
    myDepth = 3
    
data_dir = os.path.join(working_directory,'data', name)
newParams = loadPick(os.path.join(data_dir,'new-params.p'))
RS = loadPick(os.path.join(data_dir,'runSwitches.p'))

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
    
run_dir = os.path.join(working_directory,'copasiRuns', 'proLik'+name)
if not os.path.isdir(run_dir):
    os.makedirs(run_dir)

expPaths = []
for df, i in zip(RS['calDf'],range(len(RS['calDf']))):
    path = os.path.join(data_dir,'exp'+str(i)+'.csv')
    df.to_csv(path_or_buf = path)
    expPaths.append(path)

myModel = modelRunner(RS["antimony_string"], run_dir)

myOverride = GFID(newParams).iloc[selectedRow].to_dict()

myBase = lowerAdjR**(2/(-points+1))
myRange = [10**((i-(points-1)//2)/perLog10)
           for i in range(points)]

print("profile likelyhood begins")

if "estVarsPreOveride" in RS.keys():
    estVars = RS["estVarsPreOveride"]
else:
    estVars = RS["estVars"]

myPL = myModel.runProfileLikelyhood(expPaths, myRange, estVars,
                                    rocket=mySuperComputer, 
                                    overrideParam=myOverride,
                                    indepToAdd=RS["indep_cond"],
                                    upperParamBound=myUpperBound,
                                    lowerParamBound=myLowerBound,
                                    depth=myDepth,
                                    method = methDict)

print("profile likelyhood ends")

savePick(["data",name,"proLick-"+str(selectedRow)+".p"], myPL,
         relative=True)

RS = loadPick(os.path.join(data_dir,'runSwitches.p'))

RS["PL-"+str(selectedRow)]={"base":myBase, "range":myRange, "points":points}

savePick(os.path.join(data_dir,'runSwitches.p'),RS)

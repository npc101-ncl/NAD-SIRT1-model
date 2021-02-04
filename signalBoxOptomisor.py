#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:27:19 2021

@author: peter
"""

import site, os, re
import pandas as pd
from python.pycotoolsHelpers import *
from python.utilityTools import *
import pickle
import time, sys
import math

cmdDict, cmdFlags = getCmdLineArgs()
RS={}

signalSet = [{"preSignal":0,   "S_p":0.5*math.pi},
             {"preSignal":1,   "S_p":1.5*math.pi},
             {"preSignal":0.5, "S_f":1/(2*math.pi)},
             {"preSignal":0.5, "S_f":3/(2*math.pi)},
             {"preSignal":0.5, "S_f":9/(2*math.pi)}]

RS["signalSet"] = signalSet

duration = 20
intervals = 200
calChans = ["Sq2C1","Sq3C1"]

RS["duration"] = duration
RS["intervals"] = intervals
RS["calChans"] = calChans

calData = pd.DataFrame(data={'Time': [i*duration/intervals for i
                                      in range(intervals+1)]})

for chan in calChans:
    calData[chan]=0
    
iParamRanges = {"kD1_S":[0.1, 0.5, 1],
                "kD1_V":[0.1, 1, 10],
                "kD1_h":[1, 10, 100],
                "kD1_R":[0.1, 1, 10]}

iParamsDF = []
iParamLens = {k:len(v) for k,v in iParamRanges.items()}
k=1
for i in [v for k,v in iParamLens.items()]:
    k*=i
for i in range(k):
    tDict = {}
    j = i
    for k, v in iParamLens.items():
        tDict[k] = iParamRanges[k][j%v]
        j=j//v
    iParamsDF.append(tDict)
iParamsDF = pd.DataFrame(iParamsDF)

RS["iParamRanges"] = iParamRanges
RS["iParamsDF"] = iParamsDF

oParams = ["kD2_S", "kD2_V", "kD2_h", "kD2_R", "delay2I",
           "kD3_a", "kD3_h", "kD3_R", "delay3I"]

RS["oParams"] = oParams

myUpperBound=1000
myLowerBound=0.0001

secondsToRun = 60*60*47
endTime = time.time()+secondsToRun

mySuperComputer = "slurm" in cmdFlags

if "meth" in cmdDict.keys():
    myMeth = cmdDict["meth"]
else:
    myMeth = "particle_swarm_default"
    
if "name" in cmdDict.keys():
    name = cmdDict["name"]
else:
    name = "Hill_coop"
    
if "copys" in cmdDict.keys():
    myCopyNum = cmdDict["copys"]
else:
    myCopyNum = 3

antimony_string = loadTxt(["delayAntFile.txt"], relative=True)
run_dir = resolvePath(['copasiRuns', name+'-sigOpt'],relative=True)
calPath = resolvePath(['copasiRuns', name+'-sigOpt',"myCal.csv"],
                      relative=True)

RS["antimony_string"] = antimony_string

calData.to_csv(calPath,index=False)

myModel = modelRunner(antimony_string, run_dir)

calPaths = [calPath for _ in signalSet]

params = myModel.runParamiterEstimation(calPaths,
                                        copyNum=myCopyNum,
                                        rocket=mySuperComputer,
                                        estimatedVar=oParams,
                                        upperParamBound=myUpperBound,
                                        lowerParamBound=myLowerBound,
                                        method=myMeth,
                                        overrideParam=iParamsDF,
                                        indepToAdd=signalSet,
                                        endTime=endTime) 

params = GFID(params)
params = params[[col for col in params.columns if col!="RSS"]]

params = myModel.runParamiterEstimation(calPaths,
                                        copyNum=myCopyNum,
                                        rocket=mySuperComputer,
                                        estimatedVar=oParams,
                                        upperParamBound=myUpperBound,
                                        lowerParamBound=myLowerBound,
                                        method={'method':'hooke_jeeves'},
                                        overrideParam=params,
                                        indepToAdd=signalSet,
                                        randStartVal = False,
                                        endTime=endTime)

savePick(["data",name,"eqParams.p"], params, relative=True)
savePick(["data",name,"runSwitches.p"], RS, relative=True)
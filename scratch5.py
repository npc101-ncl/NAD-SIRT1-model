#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 14:13:10 2021

@author: peter
"""
from python.pycotoolsHelpers import *
from python.utilityTools import *
from python.debugTools import *
import re
import pandas as pd

name = "reConf12"

newParams = loadPick(['data', name, 'new-params.p'], relative=True)
newParams = GFID(newParams)
RS = loadPick(['data', name, 'runSwitches.p'], relative=True)

newParams={k:v for k,v in newParams.iloc[1].items() if k!="RSS"}
print(newParams)
print(RS["ICTrack"][10])
overide = newParams
overide.update(RS["ICTrack"][10])
overide["AICAR_treatment"] = overide.pop("AICAR")

antStrBD = getModelsAndFunctions(RS["antimony_string"])

antStrBD = getModelsAndFunctions(RS["antimony_string"])

antStr = [i["text"].splitlines() for i in antStrBD["models"]]
for i in range(len(antStr)):
    antStr[i][0]=antStr[i][0].replace("*","")
    antStr[i] = "\n".join(antStr[i])
antStr = "\n".join(antStr)
antStr = [i for i in antStr.splitlines()
          if not bool(re.match(r".*\bis\b.*", i))]
antStr = "\n".join(antStr)
antStr = ("\n".join([i["text"] for i in antStrBD["functions"]]) + 
          "\n" + antStr)

myDebug = modelDebugger(antStr)

debugReturn = myDebug.debug(0.0, float(RS["ICDuration"][10]),
                            int(RS["ICDuration"][10]*100+1),
                            isEular=True, overrides=overide)
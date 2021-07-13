#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 16:46:58 2021

@author: peter
"""

from python.utilityTools import *
import re

cmdDict, cmdFlags = getCmdLineArgs()

if "name" in cmdDict.keys():
    name = cmdDict["name"]
else:
    name = "reConf11"
    
mySuperComputer = "slurm" in cmdFlags
    
# add path to copasiSE to path varaiable if not on rocket clustor
if not mySuperComputer:
    addCopasiPath("/Applications/copasi")

RS = loadPick(['data', name, 'runSwitches.p'],relative=True)

newParam = loadPick(['data', name, 'new-params.p'],relative=True)


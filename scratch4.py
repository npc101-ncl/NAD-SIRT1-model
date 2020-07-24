#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 10:51:38 2020

@author: peter
"""

import site, os, re
import pandas as pd
from python.pycotoolsHelpers import *
import pickle
import time, sys

cmdLineArg = sys.argv[1:]

name = [name[5:] for name in cmdLineArg if (name.startswith("name:") and 
        len(name)>5)]
if len(name)>0:
    name = name[0]
else:
    name = "reConf5"
    
antFile = [antFile[4:] for antFile in cmdLineArg
           if (antFile.startswith("ant:") and len(antFile)>4)]
if len(antFile)>0:
    antFile = antFile[0]
else:
    antFile = None


working_directory = os.path.dirname(os.path.abspath(__file__))

data_dir = os.path.join(working_directory,'data', name)

file = open(os.path.join(data_dir,'runSwitches.p'),'rb')
RS = pickle.load(file)
file.close()

f = open(os.path.join(data_dir,'new-params.p'), "rb" )
newParams = pickle.load(f)
f.close()

secondsToRun = 60*60*47
endTime = time.time()+secondsToRun

mySuperComputer = "slurm" in cmdLineArg

if not mySuperComputer:
    addCopasiPath("/Applications/copasi")
    
run_dir = os.path.join(working_directory,'copasiRuns', 'sensNew_'+name)
if not os.path.isdir(run_dir):
    os.makedirs(run_dir)
    
if antFile is None:
    antimony_string = RS["antimony_string"]    
else: 
    antFile = open(os.path.join(working_directory,antFile), "r")
    antimony_string = antFile.read()
    antFile.close()
    
myModel = modelRunner(antimony_string, run_dir)

df = newParams[next(iter(newParams))]
mySens = myModel.getSensativitys(adjustParams=df, setIndex=[0,1])
   
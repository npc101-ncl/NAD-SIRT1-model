#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 16:44:16 2020

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
    name = "reConf3"
    
antFile = [antFile[4:] for antFile in cmdLineArg
           if (antFile.startswith("ant:") and len(antFile)>4)]
if len(antFile)>0:
    antFile = antFile[0]
else:
    antFile = "modAntFile.txt"


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
    
run_dir = os.path.join(working_directory,'copasiRuns', 'f3a4'+name)
if not os.path.isdir(run_dir):
    os.makedirs(run_dir)
    
antFile = open(os.path.join(working_directory,antFile), "r")
antimony_string = antFile.read()
antFile.close()

fig3ICCont = {"AICAR":1}
fig3ICGI = {"AICAR":1, "PARP1":2.5}

if __name__ == "__main__":
    
    myModel = modelRunner(antimony_string, run_dir)
    
    myModel.clearRunDirectory()
    df=newParams[next(iter(newParams))].copy()
    for myVar, myVal in fig3IC.items():
        df[myVar] = myVal
    timeCourse = myModel.runTimeCourse(fig3Dur,
                                       adjustParams=df,
                                       #rocket=mySuperComputer,
                                       stepSize=0.25)
    file = open(os.path.join(data_dir, 
                             'fig3-timeCourses.p'),'wb')
    pickle.dump(timeCourse, file)
    file.close()
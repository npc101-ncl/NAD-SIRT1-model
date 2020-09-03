#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 17:57:39 2020

@author: peter
"""

import site, os, re
import pandas as pd
from python.pycotoolsHelpers import *
from python.analysisTools import *
from python.utilityTools import *
import pickle
import time, sys

cmdLineArg = sys.argv[1:]

name = [name[5:] for name in cmdLineArg if (name.startswith("name:") and 
        len(name)>5)]
if len(name)>0:
    name = name[0]
else:
    name = "reConf6"
    
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

myClust = RSSClusterEstimation(GFID(newParams))
myClust = myClust[0]["size"]

secondsToRun = 60*60*47
endTime = time.time()+secondsToRun

mySuperComputer = "slurm" in cmdLineArg

if not mySuperComputer:
    addCopasiPath("/Applications/copasi")
    
run_dir = os.path.join(working_directory,'copasiRuns', 'sens'+name)
if not os.path.isdir(run_dir):
    os.makedirs(run_dir)
    
if antFile is None:
    antimony_string = RS["antimony_string"]    
else: 
    antFile = open(os.path.join(working_directory,antFile), "r")
    antimony_string = antFile.read()
    antFile.close()

myPaths = []
for i, df in zip(range(len(RS['calDf'])),RS['calDf']):
    path = os.path.join(run_dir,"exp"+str(i)+".csv")
    df.to_csv(path, index = False)
    myPaths.append(path)

myList1 = []
myList2 = []
for index in range(myClust):
    myDF = newParams[next(iter(newParams))].iloc[[index]]
    
    contSec = len(myDF)
    
    myModel = modelRunner(antimony_string, run_dir)
    
    steps = 10
    adj = [(i+1)*0.01/steps for i in range(steps)]
    
    myDF = myModel.makeSensAnalDF({col:adj for col in myDF.columns
                                   if col != "RSS"}, myDF)
    
    myRSS = myModel.getRSSforParamiters(myDF, RS["indep_cond"], myPaths)
    
    myDF['RSS'] = myRSS
    
    myDF2 = myDF.copy()
    tempDS = myDF.iloc[0]
    myDF2 = (myDF2-tempDS)/tempDS
    myDF2 = pd.melt(myDF2, id_vars = ['RSS'])
    myDF2 = myDF2[myDF2["value"] != 0.0]
    myDF2 = myDF2[pd.isnull(myDF2["value"])==False]
    myDF2 = myDF2.sort_values(by=['RSS'])
    myDF2 = myDF2.rename(columns={"value":"paramiter change%",
                                  "RSS":"RSS change%"})  
    myDF["index"] = index
    myDF2["index"] = index
    myList1.append(myDF)
    myList2.append(myDF2)

myDF = pd.concat(myList1)
myDF2 = pd.concat(myList2)
myDF.to_csv(os.path.join(data_dir,"sensativity.csv"))
myDF2.to_csv(os.path.join(data_dir,"sensativity2.csv"))

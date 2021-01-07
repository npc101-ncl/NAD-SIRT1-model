#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 15:40:11 2020

@author: peter
"""

import site, os, re
import pandas as pd
from python.pycotoolsHelpers import *
from python.visualisationTools import *
from python.utilityTools import *
import pickle
import time, sys

cmdLineArg = sys.argv[1:]

name = [name[5:] for name in cmdLineArg if (name.startswith("name:") and 
        len(name)>5)]
if len(name)>0:
    name = name[0]
else:
    name = "reConf7"
    
antFile = [antFile[4:] for antFile in cmdLineArg
           if (antFile.startswith("ant:") and len(antFile)>4)]
if len(antFile)>0:
    antFile = antFile[0]
else:
    antFile = "modAntFile3CM.txt"

working_directory = os.path.dirname(os.path.abspath(__file__))

data_dir = os.path.join(working_directory,'data', name)

file = open(os.path.join(data_dir,'runSwitches.p'),'rb')
RS = pickle.load(file)
file.close()
    
secondsToRun = 60*60*47
endTime = time.time()+secondsToRun

f = open(os.path.join(data_dir,'new-params.p'), "rb" )
newParams = pickle.load(f)
f.close()


mySuperComputer = "slurm" in cmdLineArg

if not mySuperComputer:
    addCopasiPath("/Applications/copasi")
    
run_dir = os.path.join(working_directory,'copasiRuns', 'mito'+name)
if not os.path.isdir(run_dir):
    os.makedirs(run_dir)
    
antFile = open(os.path.join(working_directory,antFile), "r")
antimony_string = antFile.read()
antFile.close()

antFile = open(os.path.join(working_directory,"modAntFile3B.txt"), "r")
antimony_string2 = antFile.read()
antFile.close()

myModel = modelRunner(antimony_string, run_dir)

myModel.clearRunDirectory()
df = GFID(newParams).copy()
df = df.drop(columns="RSS")
res = {}

timeCourse = myModel.runTimeCourse(24*365*60,
                                   adjustParams=df,
                                   #rocket=mySuperComputer,
                                   subSet = [0],
                                   stepSize=24*365,
                                   genReactions=False)

test = timeCourse[0].iloc[-1] + 9*(timeCourse[0].iloc[-1]-
                 timeCourse[0].iloc[-2])
print(test.to_dict())

TCV = timeCourseVisualiser(timeCourse)

TCV.multiPlot(varSelect=['AMPK', 'AMPK-P', 'PGC1a', 'PGC1a-P',
                         'PGC1a_deacet', 'SIRT1_activity', 'SIRT1',
                         'NAD', 'Delay_in_NAD_increase', 'PARP1',
                         'Deacetylation_Delay', 'AICAR_Delay', 'AICAR',
                         'Glucose', 'GlucoseDelay', 'NAD_NegReg', 'NR-NMN',
                         'AMPK_driven_NAD_source',
                         'AMPK_driven_NegReg_source', 'Glucose_source',
                         'Damage', 'Mito_old', 'Mitophagy', 'Mito_new',
                         'Mito_turnover'],
              save=resolvePath(["figures",name,"mitoFail.png"],
                               relative=True))



# time = 335750

for j in range(len(df)):
    """
    timeCourse = myModel.runTimeCourse(24,
                                       adjustParams=df,
                                       #rocket=mySuperComputer,
                                       subSet = [j],
                                       stepSize=1)
    
    if len(timeCourse[0]==1):
        res[str(j)]={}
        for i in df.columns:
            df2 = df.drop(columns=i)
            myModel.clearRunDirectory()
            timeCourse = myModel.runTimeCourse(24,
                                               adjustParams=df2,
                                               #rocket=mySuperComputer,
                                               subSet = [j],
                                               stepSize=1)
            if len(timeCourse[0])>1:
                res[str(j)][i] = df.iloc[j][i]
    """

"""
myModel = modelRunner(antimony_string, run_dir)

myModel.clearRunDirectory()
df = GFID(newParams).copy()
df = df.drop(columns="RSS")
timeCourse = myModel.runTimeCourse(24*365*80,
                                   adjustParams=df,
                                   #rocket=mySuperComputer,
                                   stepSize=24*365)
file = open(os.path.join(data_dir, 
                         'mito-timeCourses-base.p'),'wb')
pickle.dump(timeCourse, file)
file.close()

print(timeCourse[0].squeeze().to_string())

#mito disconect

myModel.clearRunDirectory()
df = GFID(newParams).copy()
df = df.drop(columns="RSS")
df["Mitochondrial_stress_signal_V"] = 0
df["Induced_PGC1a_deacetylation_k1"] = 0
df["PGC1a_acetylation_k1"] = 0
df["Basal_PGC1a_deacetylation_v"] = 0
df["SIRT1"] = 0
timeCourse = myModel.runTimeCourse(24*365*80,
                                   adjustParams=df,
                                   #rocket=mySuperComputer,
                                   stepSize=24*365)
file = open(os.path.join(data_dir, 
                         'mito-timeCourses-discon.p'),'wb')
pickle.dump(timeCourse, file)
file.close()

myModel.clearRunDirectory()
df = GFID(newParams).copy()
df = df.drop(columns="RSS")
df["PARP1"] = 2.5
timeCourse = myModel.runTimeCourse(24*365*80,
                                   adjustParams=df,
                                   #rocket=mySuperComputer,
                                   stepSize=24*365)
file = open(os.path.join(data_dir, 
                         'mito-timeCourses-highPARP.p'),'wb')
pickle.dump(timeCourse, file)
file.close()

myModel.clearRunDirectory()
df = GFID(newParams).copy()
df = df.drop(columns="RSS")
timeCourse = myModel.runTimeCourse(24*365*80,
                                   adjustParams=df,
                                   #rocket=mySuperComputer,
                                   stepSize=24*365)

oddDict = {}
normDict = {}

for TC in timeCourse:
    if len(TC)==1:
        ds = TC.squeeze()
        for i in [k for k,v in ds.items() if (v==0) or (v>1000)]:
            if i in oddDict.keys():
                oddDict[i]=oddDict[i]+1
            else:
                oddDict[i]=1
    if len(TC)>1:
        ds = TC.iloc[0]
        for i in [k for k,v in ds.items() if (v==0) or (v>1000)]:
            if i in normDict.keys():
                normDict[i]=normDict[i]+1
            else:
                normDict[i]=1
"""
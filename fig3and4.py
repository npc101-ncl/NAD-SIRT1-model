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
    name = "reConf6"
    
antFile = [antFile[4:] for antFile in cmdLineArg
           if (antFile.startswith("ant:") and len(antFile)>4)]
if len(antFile)>0:
    antFile = antFile[0]
else:
    antFile = None

testRun = False

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
    
if antFile is None:
    antimony_string = RS["antimony_string"]    
else: 
    antFile = open(os.path.join(working_directory,antFile), "r")
    antimony_string = antFile.read()
    antFile.close()
    
antStrBD = getModelsAndFunctions(antimony_string)
antimony_string_fig3 = antStrBD["models"][0]["text"]
antimony_string_fig3 = antimony_string_fig3.splitlines()
antimony_string_fig3 = (antimony_string_fig3[:-1]+
                        ["\tat (Time>12): AICAR_treatment=1.0"]+
                        antimony_string_fig3[-1:])
antimony_string_fig3 = "\n".join(antimony_string_fig3)
antimony_string_fig3 = ("\n".join([i["text"] for i 
                                   in antStrBD["functions"]])+
                        "\n"+antimony_string_fig3)

fig3ICCont = {"PARP1":1}
fig3ICGI = {"PARP1":2.5}
fig3Dur = 12

figAlphaICCont = {}
figAlphaICNoSirt = {"SIRT1":0}

fig4Dur1 = 24
fig4Dur2 = 12
fig4ICCont = {}
fig4ICGI = {"PARP1":2.5}
fig4ICGINR = {"PARP1":2.5, "NR-NMN":500}
fig4ICGIPJ = {"PARP1":0}
fig4IC = {"cont":fig4ICCont, "GI":fig4ICGI, "GINR":fig4ICGINR, 
          "GIPJ":fig4ICGIPJ}

if __name__ == "__main__":
    
    myModel = modelRunner(antimony_string_fig3, run_dir)
    
    myModel.clearRunDirectory()
    df=newParams[next(iter(newParams))].copy()
    if testRun:
        df = df.head()
    for myVar, myVal in fig3ICCont.items():
        df[myVar] = myVal
    timeCourse = myModel.runTimeCourse(fig3Dur+12,
                                       adjustParams=df,
                                       #rocket=mySuperComputer,
                                       stepSize=0.25)
    timeCourse = [tc[tc["Time"]>=12] for tc in timeCourse]
    for tc in timeCourse:
        tc["Time"]=tc["Time"]-12
    if not testRun:
        file = open(os.path.join(data_dir, 
                                 'fig3Cont-timeCourses.p'),'wb')
        pickle.dump(timeCourse, file)
        file.close()
    
    myModel.clearRunDirectory()
    df=newParams[next(iter(newParams))].copy()
    if testRun:
        df = df.head()
    for myVar, myVal in fig3ICGI.items():
        df[myVar] = myVal
    timeCourse = myModel.runTimeCourse(fig3Dur+12,
                                       adjustParams=df,
                                       #rocket=mySuperComputer,
                                       stepSize=0.25)
    timeCourse = [tc[tc["Time"]>=12] for tc in timeCourse]
    for tc in timeCourse:
        tc["Time"]=tc["Time"]-12
    if not testRun:
        file = open(os.path.join(data_dir, 
                                 'fig3GI-timeCourses.p'),'wb')
        pickle.dump(timeCourse, file)
        file.close()
    myModel = modelRunner(antimony_string, run_dir)
    myStr = ""
    for ICName, myIC in fig4IC.items():
        myModel.clearRunDirectory()
        df=newParams[next(iter(newParams))].copy()
        if testRun:
            df = df.head()
        for myVar, myVal in myIC.items():
            df[myVar] = myVal
        timeCourse = myModel.runTimeCourse(fig4Dur1,
                                           adjustParams=df,
                                           #rocket=mySuperComputer,
                                           stepSize=0.25)
        myStr = myStr + "fig4 round 0 "+ICName + "\n"
        myStr = myStr + timeCourse[0].iloc[[0,-1]].to_string() + "\n"
        df = pd.DataFrame([TC.iloc[-1].to_dict() for TC in timeCourse])
        for myVar, myVal in myIC.items():
            df[myVar] = myVal
        df = df.drop(columns="SIRT1_activity")
        timeCourse = myModel.runTimeCourse(fig4Dur2,
                                           adjustParams=df,
                                           #rocket=mySuperComputer,
                                           stepSize=0.25)
        myStr = myStr + "fig4 round 1 no aicar " +ICName + "\n"
        myStr = myStr + timeCourse[0].iloc[[0,-1]].to_string() + "\n"
        if not testRun:
            file = open(os.path.join(data_dir, 
                                     "fig4"+ICName+"-timeCourses.p"),'wb')
            pickle.dump(timeCourse, file)
            file.close()
        
        myDict = myIC.copy()
        myDict["AICAR"] = 1
        
        for myVar, myVal in myDict.items():
            df[myVar] = myVal
        timeCourse = myModel.runTimeCourse(fig4Dur2,
                                           adjustParams=df,
                                           #rocket=mySuperComputer,
                                           stepSize=0.25)
        myStr = myStr + "fig4 round 1 aicar "+ICName+"AIC" + "\n"
        myStr = myStr + timeCourse[0].iloc[[0,-1]].to_string() + "\n"
        if not testRun:
            file = open(os.path.join(data_dir, 
                                     "fig4"+ICName+"AIC-timeCourses.p"),'wb')
            pickle.dump(timeCourse, file)
            file.close()
    
    myModel.clearRunDirectory()
    df=newParams[next(iter(newParams))].copy()
    if testRun:
        df = df.head()
    for myVar, myVal in figAlphaICCont.items():
        df[myVar] = myVal
    timeCourse = myModel.runTimeCourse(24,
                                       adjustParams=df,
                                       #rocket=mySuperComputer,
                                       stepSize=0.25)
    if not testRun:
        file = open(os.path.join(data_dir, 
                                 'figAlphaCont-timeCourses.p'),'wb')
        pickle.dump(timeCourse, file)
        file.close()
    
    myModel.clearRunDirectory()
    df=newParams[next(iter(newParams))].copy()
    if testRun:
        df = df.head()
    for myVar, myVal in figAlphaICNoSirt.items():
        df[myVar] = myVal
    timeCourse = myModel.runTimeCourse(24,
                                       adjustParams=df,
                                       #rocket=mySuperComputer,
                                       stepSize=0.25)
    if not testRun:
        file = open(os.path.join(data_dir, 
                                 'figAlphaNoSirt-timeCourses.p'),'wb')
        pickle.dump(timeCourse, file)
        file.close()
        
    
    text_file = open(os.path.join(data_dir, 'temp.txt'), "w")
    n = text_file.write(myStr)
    text_file.close()
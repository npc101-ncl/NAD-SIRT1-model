#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 18:13:35 2020

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
    
secondsToRun = 60*60*47
endTime = time.time()+secondsToRun

f = open(os.path.join(data_dir,'new-params.p'), "rb" )
newParams = pickle.load(f)
f.close()


mySuperComputer = "slurm" in cmdLineArg

if not mySuperComputer:
    addCopasiPath("/Applications/copasi")
    
run_dir = os.path.join(working_directory,'copasiRuns', 'val'+name)
if not os.path.isdir(run_dir):
    os.makedirs(run_dir)
    
antFile = open(os.path.join(working_directory,antFile), "r")
antimony_string = antFile.read()
antFile.close()

validationPath = os.path.join(working_directory, "oldModel",
                              "NAD_model_files")

data_file = os.path.join(validationPath,
                            "All_data_NAD_model.xlsx")

val_data = pd.read_excel(data_file,sheet_name='Sheet1',skiprows=2)

ready = True
val_temp = []
for i in range(len(val_data)):
    if ready and (not val_data.iloc[i].isnull().all()):
        ready = False
        val_temp.append(pd.DataFrame(val_data.iloc[i]).transpose())
    elif not ready and (not val_data.iloc[i].isnull().all()):
        val_temp[-1] = val_temp[-1].append(val_data.iloc[i],
                ignore_index=True)
    else:
        ready = True
        
val_data = [{"df":df} for df in val_temp]

for i in range(len(val_data)):
    val_data[i]["df"]["GlucoseLevel"]=0
    val_data[i]["df"]["AICARLevel"]=0
    val_data[i]["df"]["NRLevel"]=0
    val_data[i]["df"]["PARPLevel"]=1
    val_data[i]["df"]["SIRT"]=1
    for j, treatment in zip(range(len(val_data[i]["df"])),
                            val_data[i]["df"]["Treatment"]):
        ycol = val_data[i]["df"].columns.get_loc("GlucoseLevel")
        if "5mM glucose" in treatment:
            val_data[i]["df"].iloc[j,ycol] = 5
        elif "25mM Glucose" in treatment:
            val_data[i]["df"].iloc[j,ycol] = 25
        ycol = val_data[i]["df"].columns.get_loc("AICARLevel")
        if "0.1mM AICAR" in treatment:
            val_data[i]["df"].iloc[j,ycol] = 0.2
        elif "0.5mM AICAR" in treatment:
            val_data[i]["df"].iloc[j,ycol] = 1
        elif "2mM AICAR" in treatment:
            val_data[i]["df"].iloc[j,ycol] = 4
        ycol = val_data[i]["df"].columns.get_loc("NRLevel")
        if "50  µM of N" in treatment:
            val_data[i]["df"].iloc[j,ycol] = 50
        elif "100  µM of N" in treatment:
            val_data[i]["df"].iloc[j,ycol] = 100
        elif "200  µM of N" in treatment:
            val_data[i]["df"].iloc[j,ycol] = 200
        elif "0.2mM N" in treatment:
            val_data[i]["df"].iloc[j,ycol] = 200
        elif "500  µM of N" in treatment:
            val_data[i]["df"].iloc[j,ycol] = 500
        elif "0.5mM N" in treatment:
            val_data[i]["df"].iloc[j,ycol] = 500
        elif "0.5m MNR" in treatment:
            val_data[i]["df"].iloc[j,ycol] = 500
        elif "1000  µM of N" in treatment:
            val_data[i]["df"].iloc[j,ycol] = 1000
        elif "1mM N" in treatment:
            val_data[i]["df"].iloc[j,ycol] = 1000
        elif "10mM N" in treatment:
            val_data[i]["df"].iloc[j,ycol] = 10000
        ycol = val_data[i]["df"].columns.get_loc("PARPLevel")
        if "ATM -/-" in treatment:
            val_data[i]["df"].iloc[j,ycol] = 3.22
        ycol = val_data[i]["df"].columns.get_loc("SIRT")
        if "SIRT1" in treatment:
            val_data[i]["df"].iloc[j,ycol] = 0
    val_data[i]["hasGlucose"]=any([j!=0 for j
            in val_data[i]["df"]["GlucoseLevel"]])
    val_data[i]["hasAICAR"]=any([j!=0 for j
            in val_data[i]["df"]["AICARLevel"]])
    val_data[i]["hasNMN"]=any([("NMN" in i) for i
            in val_data[i]["df"]["Treatment"]])
    val_data[i]["isSirtVar"]=any([("SIRT1" in i) for i
            in val_data[i]["df"]["Treatment"]])
    val_data[i]["isREV1-"]=any([("REV1 -/-" in i) for i
            in val_data[i]["df"]["Treatment"]])
            
for i in range(len(val_data)):
    for col in val_data[i]["df"].columns:
        if (val_data[i]["df"][col] == val_data[i]["df"][col].iloc[0]).all():
            val_data[i][col]=val_data[i]["df"][col].iloc[0]

def getDataSet(data,criteria):
    retVal = []
    for i, DS in zip(range(len(data)),data):
        valid = True
        for key, val in criteria.items():
            if key in DS:
                if str(DS[key]) != str(val):
                    valid = False
                    break
            else:
                valid = False
                break
        if valid == True:
            retVal.append(i)
    if len(retVal)==1:
        retVal=retVal[0]
    return retVal

diagrams = [{"name":"S6","crit":{'Reference':"Park et al. 2011"}},
            {"name":"S7","crit":{'Reference':"Ouchi et al. 2005"}},
            {"name":"S8","crit":{'Reference':"Egawa et al. 2014",
                                 "Timepoint (hr)":24}},
            {"name":"S9","crit":{'Reference':"Hall et al. 2018"}},
            {"name":"S10","crit":{'Reference':"Canto et al. 2009",
                                  "Timepoint (hr)":4}},
            {"name":"S11","crit":{'Reference':"Fulco et al. 2008",
                                  "Species":"NAD",
                                  "hasAICAR":True}},
            {"name":"S12","crit":{'Reference':"Canto et al. 2009",
                                  "Species":"PGC1a_deacet",
                                  "hasAICAR":True,
                                  "Timepoint (hr)":12}},
            {"name":"S13","crit":{'Reference':"Park et al. 2014"}},
            {"name":"S14","crit":{'Reference':"Gerhart-Hines et al. 2007"}},
            {"name":"S15","crit":{'Reference':"Fulco et al. 2008",
                                  'Species':"NAD",
                                  'hasGlucose':True}},
            {"name":"S16","crit":{'Reference':"Canto et al. 2012",
                                  'hasNMN':True}},
            {"name":"S17","crit":{'Reference':"Ryu et al. 2016"}},
            {"name":"S18","crit":{'Reference':"Fletcher et al. 2017"}},
            {"name":"S19","crit":{'Reference':"Hsu and Burkholder. 2016"}},
            {"name":"S20","crit":{'Reference':"Higashida et al. 2013",
                                  'Species':"AMPK-P"}},
            {"name":"S21","crit":{'Reference':"Fakouri et al. 2017"}},
            {"name":"S22","crit":{'Species':"PGC1a_deacet",
                                  "isSirtVar":True}},
            {"name":"S23","crit":{'Reference':"Fang et al. 2016",
                                  "Species":"NAD"}},
            {"name":"S24","crit":{'Reference':"Fang et al. 2016",
                                  "Species":"PGC1a_deacet"}}] 

for i in range(len(diagrams)):
    diagrams[i]["DS"]=getDataSet(val_data,diagrams[i]["crit"])
    
def genIC(DS):
    if isinstance(DS,list):
        if len(DS)==0:
            return None, None
        if DS[0]["Reference"]!="Fakouri et al. 2017":
            newDS = DS[0].copy()
            for i in range(1,len(DS)):
                newDS["df"] = pd.concat([newDS["df"],DS[i]["df"]],
                     ignore_index=True)
            return genIC(newDS)
        else:
            newDS = [i for i in DS if i["Species"]=="NAD"][0].copy()
            df = DS[0]["df"].copy()
            for i in range(1,len(DS)):
                df = pd.concat([df,DS[i]["df"]],
                     ignore_index=True)
            df = df[df["Treatment"] == "REV1 -/- MEFs"]
            df.index = df["Species"]
            df = df["Fold-change Measurement"]
            Fakouri_data = df.to_dict()
            myModel = modelRunner(antimony_string, run_dir)
            tempParams = myModel.extractModelParam()
            Fakouri_data["AMPK total"] = (tempParams["AMPK-P"]+
                         tempParams["AMPK"])*Fakouri_data["AMPK total"]
            Fakouri_data["AMPK ratio"] = (Fakouri_data["AMPK-P"]*
                        tempParams["AMPK-P"]/(tempParams["AMPK"]+
                                  tempParams["AMPK-P"]))
            Fakouri_data["AMPK_P"] = (Fakouri_data["AMPK ratio"]*
                        Fakouri_data["AMPK total"])
            Fakouri_data["AMPK"] = (Fakouri_data["AMPK total"] - 
                        Fakouri_data["AMPK-P"])
            Fakouri_data["SIRT1"] = tempParams["SIRT1"]*Fakouri_data["SIRT1"]
            Fakouri_data["PGC1a_deacet"] = (tempParams["PGC1a_deacet"]*
                        Fakouri_data["PGC1a"])
            Fakouri_data["PGC1a_P"] = (tempParams["PGC1a-P"]*
                        Fakouri_data["PGC1a"])
            Fakouri_data["PGC1a"] = (tempParams["PGC1a"]*
                        Fakouri_data["PGC1a"])
            Fakouri_data["PARP"] = (tempParams["PARP1"]*
                        Fakouri_data["PARP1"])
            Fakouri_data["NAD"] = (tempParams["NAD"]*
                        Fakouri_data["NAD"])
            Fakouri_data.pop("AMPK total", None) 
            Fakouri_data.pop("AMPK ratio", None)
            Fakouri_data.pop("PARP1", None)
            Fakouri_data.pop("AMPK-P", None)
            ICList = [{},Fakouri_data]
            return ICList, newDS
    elif isinstance(DS,pd.Series):
        ICDict = {}
        if DS["GlucoseLevel"]==0:
            ICDict.update({"Glucose_source":0, "Glucose":0,
                           "GlucoseDelay":0})
        elif DS["GlucoseLevel"]==5:
            ICDict.update({"Glucose_source":5, "Glucose":0,
                           "GlucoseDelay":0})
        elif DS["GlucoseLevel"]==25:
            ICDict.update({"Glucose_source":25, "Glucose":0,
                           "GlucoseDelay":0})
        if DS["AICARLevel"]!=0:
            ICDict.update({"AICAR":DS["AICARLevel"]})
        if DS["NRLevel"]!=0:
            ICDict.update({"NR-NMN":DS["NRLevel"]})
        if DS["SIRT"]!=1:
            ICDict.update({"SIRT1":DS["SIRT"]})
        if DS["PARPLevel"]!=1:
            ICDict.update({"PARP1":DS["PARPLevel"]})
        return ICDict, None
    elif isinstance(DS,pd.DataFrame):
        ICList = []
        for _, row in DS.iterrows():
            ICList.append(genIC(row)[0])
        return ICList, None
    else:
        if "Timepoint (hr)" in DS:
            ICList = genIC(DS["df"])[0]
            if DS["Timepoint (hr)"]=="steady state":
                for i in range(len(ICList)):
                    for key, val in {"AICAR":"AICAR_treatment",
                                     "NR-NMN":"NR_NMN",
                                     "PARP1":"PARP"}.items():
                        if key in ICList[i]:
                            ICList[i][val] = ICList[i].pop(key)
            return ICList, DS
        else:
            ICList, _ = genIC(DS["df"])
            if len(ICList)>0:
                if all([IC == ICList[0] for IC in ICList]):
                    return ICList[0], DS
                else:
                    return None, None
            else:
                return None, None

ICTrack = []     
ICDuration = [] 
ICSS = []      
for i in range(len(diagrams)):
    DS = diagrams[i]["DS"]
    if isinstance(DS,int):
        DS = val_data[DS]
    elif isinstance(DS,list):
        DS = [val_data[i] for i in DS]
    IC, DS = genIC(DS)
    diagrams[i]["DS"] = DS
    maxTime = pd.to_numeric(DS["df"]["Timepoint (hr)"],
                            errors='coerce').max()
    if isinstance(IC,list):
        myList = []
        for ICentry in IC:
            for j in range(len(ICTrack)):
                if ICTrack[j] == ICentry:
                    myList.append(j)
                    ICDuration[j] = max(ICDuration[j], maxTime)
                    if "Timepoint (hr)" in DS:
                        ICSS[j] = (ICSS[j] or
                            DS["Timepoint (hr)"]=="steady state")
                    break
            else:
                myList.append(len(ICTrack))
                ICTrack.append(ICentry)
                ICDuration.append(maxTime)
                if "Timepoint (hr)" in DS:
                    ICSS.append(DS["Timepoint (hr)"]=="steady state")
                else:
                    ICSS.append(False)
        diagrams[i]["IC"] = myList
    else:
        for j in range(len(ICTrack)):
            if ICTrack[j] == IC:
                diagrams[i]["IC"] = j
                ICDuration[j] = max(ICDuration[j], maxTime)
                if "Timepoint (hr)" in DS:
                    ICSS[j] = (ICSS[j] or
                        DS["Timepoint (hr)"]=="steady state")
                break
        else:
            diagrams[i]["IC"] = len(ICTrack)
            ICTrack.append(IC)
            ICDuration.append(maxTime)
            if "Timepoint (hr)" in DS:
                ICSS.append(DS["Timepoint (hr)"]=="steady state")
            else:
                ICSS.append(False)
                
                
RS["ICSS"] = ICSS
RS["ICDuration"] = ICDuration
RS["ICTrack"] = ICTrack
RS["diagrams"] = diagrams

if __name__ == "__main__":
    
    myModel = modelRunner(antimony_string, run_dir)
    
    # paramiterisation check
    for i in range(len(RS["indep_cond"])):
        myModel.clearRunDirectory()
        df=newParams[next(iter(newParams))].copy()
        for myVar, myVal in RS["indep_cond"][i].items():
            df[myVar] = myVal
        timeCourse = myModel.runTimeCourse(RS["calDf"][i]["Time"].max(),
                                           adjustParams=df,
                                           #rocket=mySuperComputer,
                                           stepSize=0.25)
        file = open(os.path.join(data_dir, 
                                 'new-timeCourses'+str(i)+'.p'),'wb')
        pickle.dump(timeCourse, file)
        file.close()
        
    for i in range(len(ICTrack)):
        myModel.clearRunDirectory()
        df=newParams[next(iter(newParams))].copy()
        df = df.drop(columns="RSS")
        for myVar, myVal in ICTrack[i].items():
            df[myVar] = myVal
        if not pd.isnull(ICDuration[i]):
            print(df)
            print(ICDuration[i])
            timeCourse = myModel.runTimeCourse(ICDuration[i],
                                               adjustParams=df,
                                               #rocket=mySuperComputer,
                                               stepSize=0.25)
            file = open(os.path.join(data_dir, 
                                     'val-timeCourses'+str(i)+'.p'),'wb')
            pickle.dump(timeCourse, file)
            file.close()

        if ICSS[i]:
            #ss_sim = myModel.runSteadyStateFinder(params=df,
                                                  #rocket=mySuperComputer
            #                                      ) # rocket option
                                                    # aparently not working
                                                    
            ss_sim = myModel.runSteadyStateFinder_TC(params=df,
                                                     duration=100)
    
            file = open(os.path.join(data_dir,
                                     'val-steadStates'+str(i)+'.p'),'wb')
            pickle.dump(ss_sim, file)
            file.close()

    file = open(os.path.join(data_dir,'runSwitches.p'),'wb')
    pickle.dump(RS, file)
    file.close()
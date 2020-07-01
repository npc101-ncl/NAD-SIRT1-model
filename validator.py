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
                              "NAD_model_files",
                              "AMPK-NAD-PGC1a-SIRT1-manuscript",
                              "Raw_Literature_Data")

Fakouri_file = os.path.join(validationPath,
                            "SupplFig_21_Fakouri_et_al_2017.xlsx")

Fakouri_data = [pd.read_excel(Fakouri_file,sheet_name='Hoja1',skiprows=4*n,
                              usecols=[1,2],nrows=2) for n in range(6)]
Fakouri_data = {list(i.columns)[0]:i["Fold change"].iloc[1] for
                i in Fakouri_data}

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

validationIC = [{"AICAR":4, "Glucose_source":0, "Glucose":0,
                   "GlucoseDelay":0},
                {"AICAR":1, "Glucose_source":0, "Glucose":0,
                   "GlucoseDelay":0},
                {"AICAR":0.2, "Glucose_source":0, "Glucose":0,
                   "GlucoseDelay":0},
                {"Glucose_source":0, "Glucose":0, "GlucoseDelay":0},
                {},
                {"Glucose_source":5},
                {"AICAR":4},
                {"AICAR":4, "Glucose_source":5},
                {"NR-NMN":500, "Glucose_source":0, "Glucose":0,
                   "GlucoseDelay":0},
                {"NR-NMN":1000, "Glucose_source":0, "Glucose":0,
                   "GlucoseDelay":0},
                {"NR-NMN":200, "Glucose_source":0, "Glucose":0,
                   "GlucoseDelay":0},
                {"NR-NMN":10000, "Glucose_source":0, "Glucose":0,
                   "GlucoseDelay":0},
                Fakouri_data,
                {"SIRT1":0},
                {"PARP1":3.22},
                {"PARP1":3.22, "NR-NMN":500}]

associatedDuration = {"SupplFig_6_Park_et_al_2011.xlsx":12,
                      "SupplFig_7_Ouchi_et_al_2005.xlsx":25,
                      "SupplFig_8_Egawa_et_al_2014.xlsx":24,
                      "SupplFig_9_Hall_et_al_2018.xls":24,
                      "SupplFig_10_Canto_et_al_2009.xlsx":4,
                      "SupplFig_11_Fulco_et_al_2008.xlsx":24,
                      "SupplFig_12_Canto_et_al_2009.xlsx":12,
                      "SupplFig_13_Park_et_al_2012.xlsx":24,
                      "SupplFig_14_Gerhart-Hines_et_al_2007.xlsx":12,
                      "SupplFig_15_Fulco_et_al_2008.xlsx":24,
                      "SupplFig_16_Canto_et_al_2012.xlsx":24,
                      "SupplFig_17_Ryu_et_al_2016.xlsx":12,
                      "SupplFig_18_Fletcher_et_al_2017.xlsx":24,
                      "SupplFig_19_Hsu_and_Burkholder (2016).xlsx":24,
                      "SupplFig_20_Higashida_et_al_2013.xlsx":24,
                      "SupplFig_21_Fakouri_et_al_2017.xlsx":None,
                      "SupplFig_22_Higashida_et_al_2013.xlsx":24,
                      "SupplFig_23_Fang_et_al_2016.xlsx":48,
                      "SupplFig_24_Fang_et_al_2016.xlsx":48}

associatedDataFiles = [["SupplFig_6_Park_et_al_2011.xlsx",
                        "SupplFig_7_Ouchi_et_al_2005.xlsx",
                        "SupplFig_8_Egawa_et_al_2014.xlsx"],
                       ["SupplFig_8_Egawa_et_al_2014.xlsx",
                        "SupplFig_9_Hall_et_al_2018.xls",
                        "SupplFig_10_Canto_et_al_2009.xlsx",
                        "SupplFig_11_Fulco_et_al_2008.xlsx",
                        "SupplFig_12_Canto_et_al_2009.xlsx"],
                       ["SupplFig_8_Egawa_et_al_2014.xlsx"],
                       ["SupplFig_8_Egawa_et_al_2014.xlsx",
                        "SupplFig_16_Canto_et_al_2012.xlsx",
                        "SupplFig_18_Fletcher_et_al_2017.xlsx",
                        "SupplFig_17_Ryu_et_al_2016.xlsx",
                        "SupplFig_19_Hsu_and_Burkholder (2016).xlsx",
                        "SupplFig_20_Higashida_et_al_2013.xlsx",
                        "SupplFig_21_Fakouri_et_al_2017.xlsx",
                        "SupplFig_22_Higashida_et_al_2013.xlsx",
                        "SupplFig_23_Fang_et_al_2016.xlsx",
                        "SupplFig_24_Fang_et_al_2016.xlsx"],
                       ["SupplFig_13_Park_et_al_2012.xlsx",
                        "SupplFig_14_Gerhart-Hines_et_al_2007.xlsx",
                        "SupplFig_15_Fulco_et_al_2008.xlsx"],
                        ["SupplFig_13_Park_et_al_2012.xlsx",
                        "SupplFig_14_Gerhart-Hines_et_al_2007.xlsx",
                        "SupplFig_15_Fulco_et_al_2008.xlsx"],
                       ["SupplFig_13_Park_et_al_2012.xlsx"],
                       ["SupplFig_13_Park_et_al_2012.xlsx"],
                       ["SupplFig_16_Canto_et_al_2012.xlsx",
                        "SupplFig_18_Fletcher_et_al_2017.xlsx",
                        "SupplFig_23_Fang_et_al_2016.xlsx",
                        "SupplFig_24_Fang_et_al_2016.xlsx"],
                       ["SupplFig_17_Ryu_et_al_2016.xlsx"],
                       ["SupplFig_19_Hsu_and_Burkholder (2016).xlsx"],
                       ["SupplFig_20_Higashida_et_al_2013.xlsx"],
                       ["SupplFig_21_Fakouri_et_al_2017.xlsx"],
                       ["SupplFig_22_Higashida_et_al_2013.xlsx"],
                       ["SupplFig_23_Fang_et_al_2016.xlsx",
                        "SupplFig_24_Fang_et_al_2016.xlsx"],
                       ["SupplFig_23_Fang_et_al_2016.xlsx",
                        "SupplFig_24_Fang_et_al_2016.xlsx"]]

validationDuration = []
validationSS = []
for sim in associatedDataFiles:
    duration = 0
    doSteadyState = False
    for f in sim:
        if isinstance(associatedDuration[f],int):
            duration = max(duration,associatedDuration[f])
        else:
            doSteadyState = True
    if duration == 0:
        validationDuration.append(None)
    else:
        validationDuration.append(duration)
    doSteadyState = False # remove line after I debug steady state
    validationSS.append(doSteadyState)

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
        
    for i in range(len(validationIC)):
        myModel.clearRunDirectory()
        df=newParams[next(iter(newParams))].copy()
        df = df.drop(columns="RSS")
        for myVar, myVal in validationIC[i].items():
            df[myVar] = myVal
        if validationDuration[i] is not None:
            print(df)
            print(validationDuration[i])
            timeCourse = myModel.runTimeCourse(validationDuration[i],
                                               adjustParams=df,
                                               #rocket=mySuperComputer,
                                               stepSize=0.25)
            file = open(os.path.join(data_dir, 
                                     'val-timeCourses'+str(i)+'.p'),'wb')
            pickle.dump(timeCourse, file)
            file.close()

        if validationSS[i]:
            ss_sim = myModel.runSteadyStateFinder(params=df,
                                                  #rocket=mySuperComputer
                                                  ) # rocket option
                                                    # aparently not working
    
            file = open(os.path.join(data_dir,
                                     'val-steadStates'+str(i)+'.p'),'wb')
            pickle.dump(ss_sim, file)
            file.close()

    
    print(RS)
    
    RS["validationIC"] = validationIC
    RS["associatedDuration"] = associatedDuration 
    RS["associatedDataFiles"] = associatedDataFiles
    RS["validationDuration"] = validationDuration
    RS["validationSS"] = validationSS
    file = open(os.path.join(data_dir,'runSwitches.p'),'wb')
    pickle.dump(RS, file)
    file.close()

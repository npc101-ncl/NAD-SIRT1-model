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
RS={}

isLinked = "reconnect" in cmdLineArg
addS7 = "addS7" in cmdLineArg
ICReview = "ICReview" in cmdLineArg
RS["isLinked"] = isLinked
RS["addS7"] = addS7
RS["ICReview"] = ICReview

name = [name[5:] for name in cmdLineArg if (name.startswith("name:") and 
        len(name)>5)]
if len(name)>0:
    name = name[0]
else:
    name = "noName"

myMeth = [meth[5:] for meth in cmdLineArg if (meth.startswith("meth:") and 
          len(meth)>5)]
if len(myMeth)>0:
    myMeth = myMeth[0]
else:
    myMeth = "particle_swarm_default"
    
antFile = [antFile[4:] for antFile in cmdLineArg
           if (antFile.startswith("ant:") and len(antFile)>4)]
if len(antFile)>0:
    antFile = antFile[0]
else:
    antFile = "modAntFile.txt"
RS["antFile"] = antFile


working_directory = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(working_directory,"oldModel","NAD_model_files",
                        "AMPK-NAD-PGC1a-SIRT1-model",
                        "Parameter_Estimation_Data")
run_dir = os.path.join(working_directory,'copasiRuns', name+'-reparam')
if not os.path.isdir(run_dir):
    os.makedirs(run_dir)
    
oData_dir = os.path.join(working_directory,'data', name)
if not os.path.isdir(oData_dir):
    os.makedirs(oData_dir)
    
secondsToRun = 60*60*47
endTime = time.time()+secondsToRun

data_names = ["PE_0.5mM_AICAR_AMPK-P.txt",
              "PE_0.5mM_AICAR_NAD_and_PGC1aDeacet.txt",
              "PE_5mM_GlucRestric_NAD.txt",
              "PE_PARP_Inhib_PJ34_NAD.txt"]

if isLinked:
    if ICReview: # requires mod ant file 3+
        indep_cond = [{"AICAR":1, "Glucose_source":5.5, "Glucose":5.5,
                       "GlucoseDelay":0}, 
                      {"AICAR":1, "Glucose_source":0, "Glucose":25}, 
                      {"Glucose_source":5, "Glucose":25},
                      {"PARP1":0, "Glucose_source":25, "Glucose":25}]
    else:
        indep_cond = [{"AICAR":1, "Glucose_source":0, "Glucose":0,
                       "GlucoseDelay":0}, 
                      {"AICAR":1, "Glucose_source":0, "Glucose":0,
                       "GlucoseDelay":0}, 
                      {"Glucose_source":5},
                      {"PARP1":0}]
else:
    if ICReview:
        indep_cond = [{"AICAR":1, "Glucose_source":5.5, "Glucose":5.5,
                       "GlucoseDelay":0}, 
                      {"AICAR":1, "Glucose_source":0, "Glucose":25}, 
                      {"Glucose_source":5, "Glucose":25},
                      {"PARP1":0, "Glucose_source":25, "Glucose":25,
                       "AMPK_driven_NAD_source":0,
                       "AMPK_driven_NegReg_source":0}]
    else:
        indep_cond = [{"AICAR":1, "Glucose_source":0, "Glucose":0,
                       "GlucoseDelay":0}, 
                      {"AICAR":1, "Glucose_source":0, "Glucose":0,
                       "GlucoseDelay":0}, 
                      {"Glucose_source":5},
                      {"PARP1":0, "AMPK_driven_NAD_source":0,
                       "AMPK_driven_NegReg_source":0}]

RLD_path = os.path.join(working_directory,"oldModel","NAD_model_files",
                       "AMPK-NAD-PGC1a-SIRT1-manuscript",
                       "Raw_Literature_Data")
NR_file = os.path.join(RLD_path, "SupplFig_5_Canto_et_al_2012.xlsx")
S7_file = os.path.join(RLD_path, "SupplFig_7_Ouchi_et_al_2005.xlsx")

myKVars = ["AMPK_phosphorylation_k1", "AMPK_dephosphorylation_k1",
           "PGC1a_phosphorylation_k1", "PGC1a_dephosphorylation_k1",
           "Induced_PGC1a_deacetylation_k1", "PGC1a_acetylation_k1",
           "DUMMY_REACTION_Delay_in_NAD_Increase_k1",
           "DUMMY_REACTION_Delay_in_NAD_Increase_2_k1", 
           "NAD_synthesis_v", "NAD_utilisation_k1",
           "NAD_utilisation_by_PARP_k1", "NAD_increase_by_AMPK_Shalve", 
           "NAD_increase_by_AMPK_V", "NAD_increase_by_AMPK_h", 
           "Deacetylation_activity_Shalve", "Deacetylation_activity_V",
           "Deacetylation_activity_h",
           "DUMMY_REACTION_AICAR_stimulus_removal_k1",
           "AMPK_phosphorylation_induced_by_AICAR_k1",
           "DUMMY_REACTION_Delay_AICAR_stimulus_Shalve",
           "DUMMY_REACTION_Delay_AICAR_stimulus_V",
           "DUMMY_REACTION_Delay_AICAR_stimulus_h", 
           "Basal_PGC1a_deacetylation_v",
           "DUMMY_REACTION_PGC1a_Deacetylation_Limiter_k1",
           "Glucose_induced_AMPK_dephosphorylation_k1", 
           "Glucose_utilisation_k1", 
           "Glucose_DUMMY_REACTION_delay_Shalve",
           "Glucose_DUMMY_REACTION_delay_V",
           "Glucose_DUMMY_REACTION_delay_h",
           "Glucose_DUMMY_REACTION_delay_limiter_k1",
           "NAD_negative_regulation_k1",
           "DUMMY_REACTION_NegReg_disappearance_k1", 
           "NR_NMN_supplementation_Shalve", "NR_NMN_supplementation_V",
           "NR_NMN_supplementation_h"]

hardCodeSuspects2 = ["Induced_PGC1a_deacetylation_k1",
                     "NAD_increase_by_AMPK_Shalve",
                     "Deacetylation_activity_V",
                     "Basal_PGC1a_deacetylation_v",
                     "Glucose_DUMMY_REACTION_delay_limiter_k1",
                     "DUMMY_REACTION_NegReg_disappearance_k1",
                     "NR_NMN_supplementation_h"]

hardCodeSuspects = ["AMPK_dephosphorylation_k1",
                    "AMPK_phosphorylation_k1", 
                    "DUMMY_REACTION_Delay_in_NAD_Increase_2_k1",
                    "DUMMY_REACTION_Delay_in_NAD_Increase_k1",
                    "Deacetylation_activity_Shalve",
                    "Deacetylation_activity_h",
                    "Glucose_induced_AMPK_dephosphorylation_k1",
                    "Glucose_utilisation_k1",
                    "NAD_increase_by_AMPK_h",
                    "NR_NMN_supplementation_Shalve",
                    "PGC1a_acetylation_k1",
                    "PGC1a_dephosphorylation_k1",
                    "PGC1a_phosphorylation_k1"]

NR_data = pd.read_excel (NR_file,sheet_name='Hoja1',skiprows=1,
                         index_col=0,usecols=3,nrows=6)
#need to check units / interpritation of this file
NR_data["NR-NMN"] = NR_data.index # /1000 my inclination would be to convert
# to mols as thats defined as the unit but alvaro said he didn't do this in
# his suplimental materials so for now I wont either.
NR_data["NAD_fold_increase"] = NR_data["Fold change"]

myUpperBound=1000
myLowerBound=0.0
myCopyNum=100
mySuperComputer = "slurm" in cmdLineArg
if "removeHardCoded2" in cmdLineArg:
    removeHardCoded = 2
elif "removeHardCoded" in cmdLineArg:
    removeHardCoded = 1
else:
    removeHardCoded = 0
if not mySuperComputer:
    addCopasiPath("/Applications/copasi")
    
antFile = open(os.path.join(working_directory,antFile), "r")
antimony_string = antFile.read()
antFile.close()

if "SIRT_NAD_depleation_k1" in antimony_string:
    myKVars.append("SIRT_NAD_depleation_k1")

RS["antimony_string"] = antimony_string

if __name__ == "__main__":
    calPaths = []
    calDf = []
    for fName in data_names:
        dataFile = open(os.path.join(data_dir, fName), "r")
        df = pd.read_csv(dataFile,sep='\t')
        dataFile.close()
        pathRef = os.path.join(run_dir,re.sub("(^.*)\\.txt$","\\1.csv",
                                              fName))
        renameDict = dict(zip(list(df.columns),
                              [s.strip() for s in list(df.columns)]))
        df = df.rename(columns = renameDict)
        df.to_csv(path_or_buf = pathRef)
        calDf.append(df.copy())
        calPaths.append(pathRef)
    for index, row in NR_data.iterrows():
        df = pd.DataFrame([{"Time":0, "NAD_fold_increase":1},
                           {"Time":24,
                            "NAD_fold_increase":row["NAD_fold_increase"]}])
        pathRef = os.path.join(run_dir, "NR_effects"+str(index)+".csv")
        df.to_csv(path_or_buf = pathRef)
        calDf.append(df.copy())
        if ICReview:
            indep_cond.append({"NR-NMN":row["NR-NMN"], "Glucose_source":0, 
                               "Glucose":25})
        else:
            indep_cond.append({"NR-NMN":row["NR-NMN"]})
        calPaths.append(pathRef)
    if addS7:
        df = pd.read_excel(S7_file)
        df = df.drop(columns="AMPK-P")
        df = df.rename(columns={"Time (hr)":"Time", "Fold change":"AMPK-P"})
        pathRef = os.path.join(run_dir, "S7.csv")
        df.to_csv(path_or_buf = pathRef)
        calDf.append(df.copy())
        indep_cond.append({"AICAR":4, "Glucose_source":0, "Glucose":0,
                           "GlucoseDelay":0})
        calPaths.append(pathRef)
        
    RS["calDf"] = calDf
    RS["indep_cond"] = indep_cond
    
    myModel = modelRunner(antimony_string, run_dir)
    
    if removeHardCoded == 1:
        estVars = [var for var in myKVars if var not in hardCodeSuspects]
    elif removeHardCoded == 2:
        estVars = [var for var in myKVars if var not in hardCodeSuspects]
        estVars = [var for var in estVars if var not in hardCodeSuspects2]
    else:
        estVars = myKVars
    RS["estVars"] = estVars
    
    params = myModel.runParamiterEstimation(calPaths,copyNum=myCopyNum,
                                            rocket=mySuperComputer,
                                            estimatedVar=estVars,
                                            upperParamBound=myUpperBound,
                                            lowerParamBound=myLowerBound,
                                            method=myMeth,
                                            indepToAdd=indep_cond,
                                            endTime=endTime)   
    
    file = open(os.path.join(oData_dir,'new-params.p'),'wb')
    pickle.dump(params, file)
    file.close()
    
    timeCourse = myModel.runTimeCourse(24,
                                       adjustParams=params[
                                               next(iter(params))],
                                               stepSize=0.25) 
    
    file = open(os.path.join(oData_dir,'new-timeCourses.p'),'wb')
    pickle.dump(timeCourse, file)
    file.close()
    
    for i in range(len(indep_cond)):
        myModel.clearRunDirectory()
        df=params[next(iter(params))].copy()
        for myVar, myVal in indep_cond[i].items():
            df[myVar] = myVal
        timeCourse = myModel.runTimeCourse(24, adjustParams=df,
                                           stepSize=0.25)
        file = open(os.path.join(oData_dir,
                                 'new-timeCourses'+str(i)+'.p'),'wb')
        pickle.dump(timeCourse, file)
        file.close()
        
    file = open(os.path.join(oData_dir,'runSwitches.p'),'wb')
    pickle.dump(RS, file)
    file.close()
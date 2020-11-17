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

# switch to perform the paramiter estimations with all parts of the model
# conected
isLinked = "reconnect" in cmdLineArg

# calibrate using data from figgure s7
addS7 = "addS7" in cmdLineArg

# impliment modified initial conditions based a litrature reveiw of data
# sources
ICReview = "ICReview" in cmdLineArg

# the egawa et al 2014 paper was writen unclearly so this allows for the 2
# interpritations
EGAWA = "EGAWA" in cmdLineArg

# records switches for future refrence
RS["isLinked"] = isLinked
RS["addS7"] = addS7
RS["ICReview"] = ICReview
RS["EGAWA"] = EGAWA

# set run name
name = [name[5:] for name in cmdLineArg if (name.startswith("name:") and 
        len(name)>5)]
if len(name)>0:
    name = name[0]
else:
    name = "noName"

# set paramiter estimation methiod from comand line argument
myMeth = [meth[5:] for meth in cmdLineArg if (meth.startswith("meth:") and 
          len(meth)>5)]
if len(myMeth)>0:
    myMeth = myMeth[0]
else:
    myMeth = "particle_swarm_default"

# get antimoney file path from comand line    
antFile = [antFile[4:] for antFile in cmdLineArg
           if (antFile.startswith("ant:") and len(antFile)>4)]
if len(antFile)>0:
    antFile = antFile[0]
else:
    antFile = "modAntFile.txt"
RS["antFile"] = antFile

# get number of estimations to do from comand line
myCopyNum = [runs[5:] for runs in cmdLineArg if (runs.startswith("runs:") and 
          len(runs)>5)]
if len(myCopyNum)>0:
    myCopyNum = int(myCopyNum[0])
else:
    myCopyNum = 100

# set working rirectory, data directory and run directory
working_directory = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(working_directory,"oldModel","NAD_model_files",
                        "AMPK-NAD-PGC1a-SIRT1-model",
                        "Parameter_Estimation_Data")
run_dir = os.path.join(working_directory,'copasiRuns', name+'-reparam')
if not os.path.isdir(run_dir):
    os.makedirs(run_dir)

# set output data directory based on run name    
oData_dir = os.path.join(working_directory,'data', name)
if not os.path.isdir(oData_dir):
    os.makedirs(oData_dir)
    
# calculate time to perform emergency wind up of estimation
secondsToRun = 60*60*47
endTime = time.time()+secondsToRun

# data files pre extracted for 
data_names = ["PE_0.5mM_AICAR_AMPK-P.txt", # egawa et al 2014
              "PE_0.5mM_AICAR_NAD_and_PGC1aDeacet.txt", # canto et al 2009
              "PE_5mM_GlucRestric_NAD.txt", # canto et al 2010
              "PE_PARP_Inhib_PJ34_NAD.txt"] # bai et al 2011

# sets initial conditions based in switches
if isLinked:
    if ICReview: # requires mod ant file 3+
        indep_cond = [{"AICAR":1, "Glucose_source":5.5, "Glucose":5.5}, 
                      {"AICAR":1, "Glucose_source":25, "Glucose":25},
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
        indep_cond = [{"AICAR":1, "Glucose_source":5.5, "Glucose":5.5}, 
                      {"AICAR":1, "Glucose_source":25, "Glucose":25},
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
if EGAWA and ICReview:
    indep_cond[0]["Glucose_source"]=25
    indep_cond[0]["Glucose"]=25

# calibration using the NR (figure S5), and S7 (figure s7) data requres
# data from excel files so here are the paths
RLD_path = os.path.join(working_directory,"oldModel","NAD_model_files",
                       "AMPK-NAD-PGC1a-SIRT1-manuscript",
                       "Raw_Literature_Data")
NR_file = os.path.join(RLD_path, "SupplFig_5_Canto_et_al_2012.xlsx")
S7_file = os.path.join(RLD_path, "SupplFig_7_Ouchi_et_al_2005.xlsx")

# paramiters to estimate
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

# paramiters to remove from estimation in most cut down list of estimations
hardCodeSuspects2 = ["Induced_PGC1a_deacetylation_k1",
                     "NAD_increase_by_AMPK_Shalve",
                     "Deacetylation_activity_V",
                     "Basal_PGC1a_deacetylation_v",
                     "Glucose_DUMMY_REACTION_delay_limiter_k1",
                     "DUMMY_REACTION_NegReg_disappearance_k1",
                     "NR_NMN_supplementation_h"]

# a slightly more obvious list of paramiters to exclude from estermation
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

# import NR data from excel file
NR_data = pd.read_excel (NR_file,sheet_name='Hoja1',skiprows=1,
                         index_col=0,usecols=3,nrows=6)
#need to check units / interpritation of this file
NR_data["NR-NMN"] = NR_data.index # /1000 my inclination would be to convert
# to mols as thats defined as the unit but alvaro said he didn't do this in
# his suplimental materials so for now I wont either.
NR_data["NAD_fold_increase"] = NR_data["Fold change"]

# set bounds
myUpperBound=1000
myLowerBound=0.0001

# check to see if flag set for rocket clustor in comand line
mySuperComputer = "slurm" in cmdLineArg

# check comand line switch to filter down list of paramiters to estimate
if "removeHardCoded2" in cmdLineArg:
    removeHardCoded = 2
elif "removeHardCoded" in cmdLineArg:
    removeHardCoded = 1
else:
    removeHardCoded = 0
    
# add path to copasiSE to path varaiable if not on rocket clustor
if not mySuperComputer:
    addCopasiPath("/Applications/copasi")

# import antmony string    
antFile = open(os.path.join(working_directory,antFile), "r")
antimony_string = antFile.read()
antFile.close()

# difrent antimony strings have been used so add posable extra variable
# to paramiter estimation if its there.
if "SIRT_NAD_depleation_k1" in antimony_string:
    myKVars.append("SIRT_NAD_depleation_k1")

# save antimony string for refrence
RS["antimony_string"] = antimony_string

if __name__ == "__main__":
    calPaths = []
    calDf = []
    # import first 4 data files (time courses)
    for fName in data_names:
        # import individual data file
        dataFile = open(os.path.join(data_dir, fName), "r")
        df = pd.read_csv(dataFile,sep='\t')
        dataFile.close()
        # define new file path in run directory with same name but csv
        # extention
        pathRef = os.path.join(run_dir,re.sub("(^.*)\\.txt$","\\1.csv",
                                              fName))
        # strip all leading / trailing white space out of column names
        renameDict = dict(zip(list(df.columns),
                              [s.strip() for s in list(df.columns)]))
        df = df.rename(columns = renameDict)
        # save as csv file
        df.to_csv(path_or_buf = pathRef)
        # save dataframe and path for refrence
        calDf.append(df.copy())
        calPaths.append(pathRef)
    # convert data points in NR data to time serise and save them for
    # refrence / paramiter estimations
    for index, row in NR_data.iterrows():
        # define time course data frame from NR datapoint
        df = pd.DataFrame([{"Time":0, "NAD_fold_increase":1},
                           {"Time":24,
                            "NAD_fold_increase":row["NAD_fold_increase"]}])
        # save time course as csv in run directory
        pathRef = os.path.join(run_dir, "NR_effects"+str(index)+".csv")
        df.to_csv(path_or_buf = pathRef)
        # save data frame for refrence
        calDf.append(df.copy())
        # add initial condtions for NR experamental data based on switches
        if ICReview:
            indep_cond.append({"NR-NMN":row["NR-NMN"], "Glucose_source":25, 
                               "Glucose":25})
        else:
            indep_cond.append({"NR-NMN":row["NR-NMN"]}) 
        # save path to refrence
        calPaths.append(pathRef)
    # add data and initia conditions for S7 experaments if switch on
    if addS7:
        # import excel file
        df = pd.read_excel(S7_file)
        # drop and rename columns
        df = df.drop(columns="AMPK-P")
        df = df.rename(columns={"Time (hr)":"Time", "Fold change":"AMPK-P"})
        # resave as csv in run directory
        pathRef = os.path.join(run_dir, "S7.csv")
        df.to_csv(path_or_buf = pathRef)
        # save data for refrence 
        calDf.append(df.copy())
        # add independent conditions and save for later
        indep_cond.append({"AICAR":4, "Glucose_source":0, "Glucose":0,
                           "GlucoseDelay":0})
        calPaths.append(pathRef)
    
    # save experamental data and independent conditios for future refrence    
    RS["calDf"] = calDf
    RS["indep_cond"] = indep_cond
    
    # initialise model
    myModel = modelRunner(antimony_string, run_dir)
    
    # filter down list of variables to estimate
    if removeHardCoded == 1:
        estVars = [var for var in myKVars if var not in hardCodeSuspects]
    elif removeHardCoded == 2:
        estVars = [var for var in myKVars if var not in hardCodeSuspects]
        estVars = [var for var in estVars if var not in hardCodeSuspects2]
    else:
        estVars = myKVars
    RS["estVars"] = estVars
    
    # run parameter estimation
    params = myModel.runParamiterEstimation(calPaths,copyNum=myCopyNum,
                                            rocket=mySuperComputer,
                                            estimatedVar=estVars,
                                            upperParamBound=myUpperBound,
                                            lowerParamBound=myLowerBound,
                                            method=myMeth,
                                            indepToAdd=indep_cond,
                                            endTime=endTime)   
    
    # save paramiter estimation results
    file = open(os.path.join(oData_dir,'new-params.p'),'wb')
    pickle.dump(params, file)
    file.close()
    
    #run time course of model in neutral state just to see what happens
    timeCourse = myModel.runTimeCourse(24,
                                       adjustParams=params[
                                               next(iter(params))],
                                               stepSize=0.25) 
    
    # and save it
    file = open(os.path.join(oData_dir,'new-timeCourses.p'),'wb')
    pickle.dump(timeCourse, file)
    file.close()
    
    # run time courses to replicate experaments
    for i in range(len(indep_cond)):
        # clear directory
        myModel.clearRunDirectory()       
        # get paramitersas data frame
        df=params[next(iter(params))].copy()
        # add independant conditions to data frame
        for myVar, myVal in indep_cond[i].items():
            df[myVar] = myVal
        # run time course with paramiters
        timeCourse = myModel.runTimeCourse(24, adjustParams=df,
                                           stepSize=0.25)
        # and save it to file with enumerated file names
        file = open(os.path.join(oData_dir,
                                 'new-timeCourses'+str(i)+'.p'),'wb')
        pickle.dump(timeCourse, file)
        file.close()
    
    # save refrence file
    file = open(os.path.join(oData_dir,'runSwitches.p'),'wb')
    pickle.dump(RS, file)
    file.close()
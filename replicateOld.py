#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 11:26:06 2020

@author: peter
"""

import site, os, re
import pandas as pd
from python.pycotoolsHelpers import *
import pickle
import time

working_directory = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(working_directory,"oldModel","NAD_model_files",
                        "AMPK-NAD-PGC1a-SIRT1-model",
                        "Parameter_Estimation_Data")
run_dir = os.path.join(working_directory,'copasiRuns', 'reparam')
if not os.path.isdir(run_dir):
    os.makedirs(run_dir)

data_names = ["PE_0.5mM_AICAR_AMPK-P.txt",
              "PE_0.5mM_AICAR_NAD_and_PGC1aDeacet.txt",
              "PE_5mM_GlucRestric_NAD.txt",
              "PE_PARP_Inhib_PJ34_NAD.txt"]

indep_cond = [{"AICAR":1, "Glucose_source":0}, 
              {"AICAR":1, "Glucose_source":0}, 
              {"Glucose_source":5},
              {"PARP1":0, "AMPK_driven_NAD_source":0,
               "AMPK_driven_NegReg_source":0}]
    
duration = [24,12,36,24]

NR_file = os.path.join(working_directory,"oldModel","NAD_model_files",
                       "AMPK-NAD-PGC1a-SIRT1-manuscript",
                       "Raw_Literature_Data",
                       "SupplFig_5_Canto_et_al_2012.xlsx")

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

mySuperComputer=False
if not mySuperComputer:
    addCopasiPath("/Applications/copasi")
    
antFile = open(os.path.join(working_directory,"modAntFile.txt"), "r")
antimony_string = antFile.read()
antFile.close()

if __name__ == "__main__":
    calPaths = []
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
        calPaths.append(pathRef)
    for index, row in NR_data.iterrows():
        df = pd.DataFrame([{"Time":0, "NAD_fold_increase":1},
                           {"Time":24,
                            "NAD_fold_increase":row["NAD_fold_increase"]}])
        pathRef = os.path.join(run_dir, "NR_effects"+str(index)+".csv")
        df.to_csv(path_or_buf = pathRef)
        indep_cond.append({"NR-NMN":row["NR-NMN"]})
        duration.append(24)
        calPaths.append(pathRef)
    
    myModel = modelRunner(antimony_string, run_dir)
    
    df = pd.DataFrame(indep_cond)
    
    df = myModel.preProcessParamEnsam(df)
    
    timeCourse = myModel.runTimeCourse(duration, adjustParams=df,
                                       stepSize=0.25)
    file = open(os.path.join(working_directory,'old-timeCourses.p'),'wb')
    pickle.dump(timeCourse, file)
    file.close()
    #myModel.clearRunDirectory()
    
    timeCourse = myModel.runTimeCourse(24,stepSize=0.25) 
    
    file = open(os.path.join(working_directory,'old-timeCoursesN.p'),'wb')
    pickle.dump(timeCourse, file)
    file.close()
    #myModel.clearRunDirectory()
    

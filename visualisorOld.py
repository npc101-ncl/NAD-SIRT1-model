#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 13:18:07 2020

@author: peter
"""

from python.visualisationTools import *
from python.analysisTools import *
import os, re
import pandas as pd
import pickle
from  reparamerteriser import data_names, indep_cond
import seaborn as sns
import matplotlib.pyplot as plt

working_dir = os.path.abspath('')
data_dir = os.path.join(working_dir,"oldModel","NAD_model_files",
                        "AMPK-NAD-PGC1a-SIRT1-model",
                        "Parameter_Estimation_Data")
fig_dir = os.path.join(working_dir,'figures')
if not os.path.isdir(fig_dir):
    os.makedirs(fig_dir)

data_names = ["PE_0.5mM_AICAR_AMPK-P.txt",
              "PE_0.5mM_AICAR_NAD_and_PGC1aDeacet.txt",
              "PE_5mM_GlucRestric_NAD.txt",
              "PE_PARP_Inhib_PJ34_NAD.txt"]
    
NR_file = os.path.join(working_dir,"oldModel","NAD_model_files",
                       "AMPK-NAD-PGC1a-SIRT1-manuscript",
                       "Raw_Literature_Data",
                       "SupplFig_5_Canto_et_al_2012.xlsx")

NR_data = pd.read_excel (NR_file,sheet_name='Hoja1',skiprows=1,
                         index_col=0,usecols=3,nrows=6)
#need to check units / interpritation of this file
NR_data["NR-NMN"] = NR_data.index # /1000 my inclination would be to convert
# to mols as thats defined as the unit but alvaro said he didn't do this in
# his suplimental materials so for now I wont either.
NR_data["NAD_fold_increase"] = NR_data["Fold change"]

calDF = []
for fName in data_names:
    dataFile = open(os.path.join(data_dir, fName), "r")
    df = pd.read_csv(dataFile,sep='\t')
    dataFile.close()
    renameDict = dict(zip(list(df.columns),
                          [s.strip() for s in list(df.columns)]))
    df = df.rename(columns = renameDict)
    calDF.append(df)
for index, row in NR_data.iterrows():
    df = pd.DataFrame([{"Time":0, "NAD_fold_increase":1},
                       {"Time":24,
                        "NAD_fold_increase":row["NAD_fold_increase"]}])
    indep_cond.append({"NR-NMN":row["NR-NMN"]})
    calDF.append(df)
    
# graphing alvaros model
f = open(os.path.join(working_dir,'old-timeCourses.p'), "rb" )
timeCourses = pickle.load(f)
f.close()
TCVis = timeCourseVisualiser(timeCourses)
for myData, i in zip(calDF,range(len(calDF))):
    myVars = list(myData.columns)
    myVars.remove("Time")
    TCVis.multiPlot(indexSelect=i,compLines=myData,varSelect=myVars,
                    save=os.path.join(fig_dir,'timeCourseOld'+
                                      str(i)+'.png'),
                                      xlim=[None,max(myData["Time"])])

df = []
for i in range(4,len(timeCourses)):
    NRval = indep_cond[i]["NR-NMN"]
    simEndVal = timeCourses[i][timeCourses[i]["Time"]==24]
    simEndVal = simEndVal["NAD_fold_increase"].iloc[0]
    expEndVal = calDF[i][calDF[i]["Time"]==24]["NAD_fold_increase"].iloc[0]
    df.extend([{"NR":NRval, "variable":"experiment", "NAD":expEndVal},
               {"NR":NRval, "variable":"simulation", "NAD":simEndVal}])
df = pd.DataFrame(df)
plt.figure()
bp = sns.barplot(x="NR", y="NAD", hue="variable", data=df)
bp.get_figure().savefig(os.path.join(fig_dir,'NR_NAD_old.png'))
    
f = open(os.path.join(working_dir,'old-timeCoursesN.p'),'rb')
timeCourse = pickle.load(f)
f.close()
TCVis = timeCourseVisualiser(timeCourse)
myVars = list(timeCourse.columns)
myVars.remove("Time")
myVars = [myVars[x:x+15] for x in range(0,len(myVars),15)]
for subVars, i in zip(myVars,range(len(myVars))):
    TCVis.multiPlot(save=os.path.join(fig_dir,
                                      "timeCourseOldN"+str(i)+".png"),
        varSelect = subVars)

f = open(os.path.join(working_dir,'old-Fakouri.p'),'rb')
Fakouri = pickle.load(f)
f.close()
    
Fakouri_table = pd.DataFrame([{"Index":"WT", "catagory":"Simulation",
                               "NAD":Fakouri["modParams"]["NAD"]},
                              {"Index":"WT", "catagory":"Experament",
                               "NAD":1},
                              {"Index":"Rev1 -/-",
                               "catagory":"Simulation",
                               "NAD":Fakouri["sim"]["NAD"]},
                              {"Index":"Rev1 -/-",
                               "catagory":"Experament",
                               "NAD":Fakouri["data"]["NAD"]}])

plt.figure()
bp = sns.barplot(x="Index", y="NAD", hue="catagory", data=Fakouri_table)
bp.get_figure().savefig(os.path.join(fig_dir,'Fakouri_old.png'))
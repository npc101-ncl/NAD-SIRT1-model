#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 16:47:43 2020

@author: peter
"""

from python.visualisationTools import *
from python.analysisTools import *
import os, re, sys
import pandas as pd
import pickle

cmdLineArg = sys.argv[1:]

name = [name[5:] for name in cmdLineArg if (name.startswith("name:") and 
        len(name)>5)]
if len(name)>0:
    name = name[0]
else:
    name = "reConf3"

working_dir = os.path.abspath('')

fig_dir = os.path.join(working_dir,'figures',name)
if not os.path.isdir(fig_dir):
    os.makedirs(fig_dir)

data_dir = os.path.join(working_dir,'data', name)

file = open(os.path.join(data_dir,'runSwitches.p'),'rb')
RS = pickle.load(file)
file.close()
 
"""   
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
"""

"""    
# graphing alvaros model
f = open(os.path.join(data_dir,'old-timeCourses.p'), "rb" )
timeCourses = pickle.load(f)
f.close()
TCVis = timeCourseVisualiser(timeCourses)
for myData, i in zip(RS["calDf"],range(len(RS["calDf"]))):
    myVars = list(myData.columns)
    myVars.remove("Time")
    TCVis.multiPlot(indexSelect=i,compLines=myData,varSelect=myVars,
                    save=os.path.join(fig_dir,'timeCourseOld'+
                                      str(i)+'.png'))
"""
    
"""    
f = open(os.path.join(data_dir,'old-timeCoursesN.p'),'rb')
timeCourse = pickle.load(f)
f.close()
TCVis = timeCourseVisualiser(timeCourses)
myVars = list(timeCourse.columns)
myVars.remove("Time")
myVars = [myVars[x:x+15] for x in range(0,len(myVars),15)]
for subVars, i in zip(myVars,range(len(myVars))):
    TCVis.multiPlot(save=os.path.join(fig_dir,
                                      "timeCourseOldN"+str(i)+".png"),
        varSelect = subVars)
"""

f = open(os.path.join(data_dir,'new-params.p'), "rb" )
newParams = pickle.load(f)
f.close()

"""
oldParams = pd.read_csv(os.path.join(data_dir,'oldKVals.csv'))
"""

f = open(os.path.join(data_dir,'new-timeCourses.p'), "rb" )
timeCourses = pickle.load(f)
f.close()

"""
oldNames = list(oldParams.columns)
oldNames.remove('Unnamed: 0')
oldNames.remove('Glucose_input_v')
oldNames.remove('quantity to number factor')

compSerise = oldParams.filter(items=oldNames).squeeze()
"""

PEVis = parameterEstimationVisualiser(newParams)

PEVis.waterFall(save=os.path.join(fig_dir,'waterfall.png'),
                indexNames="parameters")

"""
PEVis.refPointVsRSS(compSerise, save=os.path.join(fig_dir,'divergence.png'),
                    indexNames="parameters")
"""

RSScutoff = min(GFID(newParams)["RSS"].iloc[9],
                RSSClusterEstimation(GFID(newParams))[0]["maxRSS"])
indexCutoff = range(min(10,
                        RSSClusterEstimation(GFID(newParams))[0]["size"]))
"""
praramStruct = clusterParameterEstimation(GFID(newParams),testDistance=2.5)
indexCutoff = [i for i in indexCutoff if i in praramStruct['0']]
"""

ordering=breakSeriesByScale(GFID(newParams).mean())

for i in range(len(ordering)):
    PEVis.violinPlot(paramSelect=ordering[i],
                     save=os.path.join(fig_dir,'violin'+str(i)+'.png'),
                     RSSSelect=RSScutoff)

showValues = list(timeCourses[0].columns)
for param in list(GFID(newParams).columns):
    try:
        showValues.remove(param)
    except ValueError:
        pass
try:
    showValues.remove("NAD_fold_increase")
except ValueError:
    pass

maxes = getTCSelectionMaxes(timeCourses, selectionList=list(indexCutoff), 
                            varSelection=showValues, valRemove=[0,1])

maxes = breakSeriesByScale(maxes,maxRunLength=25)

TCVis = timeCourseVisualiser(timeCourses)

for i in range(len(maxes)):
    TCVis.multiPlot(indexSelect=list(indexCutoff),varSelect=maxes[i],
                    save=os.path.join(fig_dir,'timeCourse'+str(i)+'.png'))

"""    
suspPar = pd.Series(data={key:value for key, value in
                          zip(compSerise.index,compSerise.values) if
                          math.modf(value)[0]==0.0})
    
suspPar.to_csv(path_or_buf=os.path.join(data_dir,
                                        'suspiciousParamiters.csv'))
"""

for i, myDF in zip(range(len(RS["calDf"])),RS["calDf"]):
    f = open(os.path.join(data_dir,
                          'new-timeCourses'+str(i)+'.p'),'rb')
    timeCourses = pickle.load(f)
    f.close()
    
    showValues = list(timeCourses[0].columns)
    showValues = [val for val in showValues
                  if not val in GFID(newParams).columns]
    showValues = [val for val in showValues
                  if not (val.endswith("_k1") or val.endswith("_V")
                  or val.endswith("_Shalve") or val.endswith("_h") 
                  or val.endswith("_v"))]
    showValues = [val for val in showValues
                  if not val in ["Time","quantity to number factor",
                                 "initial_NAD"]]             
    
    maxes = getTCSelectionMaxes(timeCourses,
                                selectionList=list(indexCutoff), 
                                varSelection=showValues, valRemove=[0,1])
    maxes = breakSeriesByScale(maxes,maxRunLength=25)
    TCVis = timeCourseVisualiser(timeCourses)
    TCVis.multiPlot(indexSelect=list(indexCutoff),compLines=myDF,
                    varSelect=showValues,
                    save=os.path.join(fig_dir,'timeCourseNew'+
                                      str(i)+'.png'))
    for j in range(len(maxes)):
        TCVis.multiPlot(indexSelect=list(indexCutoff),compLines=myDF,
                        varSelect=maxes[j],
                        save=os.path.join(fig_dir,'timeCourseNew'+
                                          str(i)+"-"+str(j)+'.png'))
        
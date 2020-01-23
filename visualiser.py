#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 16:47:43 2020

@author: peter
"""

from python.visualisationTools import *
from python.analysisTools import *
import os, re
import pandas as pd
import pickle

working_dir = os.path.abspath('')
fig_dir = os.path.join(working_dir,'figures')
if not os.path.isdir(fig_dir):
    os.makedirs(fig_dir)

f = open(os.path.join(working_dir,'new-params.p'), "rb" )
newParams = pickle.load(f)
f.close()

oldParams = pd.read_csv(os.path.join(working_dir,'oldKVals.csv'))

f = open(os.path.join(working_dir,'new-timeCourses.p'), "rb" )
timeCourses = pickle.load(f)
f.close()

oldNames = list(oldParams.columns)
oldNames.remove('Unnamed: 0')

newNames = [name.replace("(", "") for name in oldNames]
newNames = [name.replace(")", "") for name in newNames]
newNames = [name.replace(".", "_") for name in newNames]
newNames = [name.replace(" ", "_") for name in newNames]
newNames = [name.replace("/", "_") for name in newNames]
newNames = [name.replace("-", "_") for name in newNames]
newNames = [name.replace("Dummy_Reaction", "DUMMY_REACTION") for 
            name in newNames]
newNames = [name.replace("Delay_Reaction", "DUMMY_REACTION_Delay") for 
            name in newNames]
newNames = [name.replace("Stimulus", "stimulus") for 
            name in newNames]
newNames = [name.replace("_basal_", "_") for 
            name in newNames]
newNames = [name.replace("induced_phosphorylation",
                         "phosphorylation_induced") for name in newNames]
newNames = [name.replace("PGC1a_induced", "Induced_PGC1a") for
            name in newNames]
newNames = [name.replace("DUMMY_REACTION_Delay_Glucose_stimulus",
                         "Glucose_DUMMY_REACTION_delay") for name in newNames]
newNames = [name.replace("NegReg_Removal", "NegReg_disappearance") for
            name in newNames]
newNames = [name.replace("Removal", "removal") for
            name in newNames]

convDict = dict(zip(oldNames,newNames))

oldParams = oldParams.filter(items=oldNames)
oldParams = oldParams.rename(columns=convDict)

diffTable = newParams[next(iter(newParams))]

PEVis = parameterEstimationVisualiser(newParams)

PEVis.waterFall(save=os.path.join(fig_dir,'waterfall.png'))

RSScutoff = newParams[next(iter(newParams))]["RSS"].iloc[9]

ordering=breakSeriesByScale(newParams[next(iter(newParams))].mean())

for i in range(len(ordering)):
    PEVis.violinPlot(paramSelect=ordering[i],
                     save=os.path.join(fig_dir,'violin'+str(i)+'.png'),
                     RSSSelect=RSScutoff)

showValues = list(timeCourses[0].columns)
for param in list(newParams[next(iter(newParams))].columns):
    try:
        showValues.remove(param)
    except ValueError:
        pass
try:
    showValues.remove("NAD_fold_increase")
except ValueError:
    pass

maxes = getTCSelectionMaxes(timeCourses, selectionList=list(range(10)), 
                            varSelection=showValues, valRemove=[0,1])

maxes = breakSeriesByScale(maxes,maxRunLength=25)

TCVis = timeCourseVisualiser(timeCourses)

for i in range(len(maxes)):
    TCVis.multiPlot(indexSelect=list(range(10)),varSelect=maxes[i],
                    save=os.path.join(fig_dir,'timeCourse'+str(i)+'.png'))
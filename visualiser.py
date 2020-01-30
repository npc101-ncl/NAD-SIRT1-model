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
oldNames.remove('Glucose_input_v')
oldNames.remove('quantity to number factor')

compSerise = oldParams.filter(items=oldNames).squeeze()

PEVis = parameterEstimationVisualiser(newParams)

PEVis.waterFall(save=os.path.join(fig_dir,'waterfall.png'),
                indexNames="parameters")

PEVis.refPointVsRSS(compSerise, save=os.path.join(fig_dir,'divergence.png'),
                    indexNames="parameters")

RSScutoff = min(GFID(newParams)["RSS"].iloc[9],
                RSSClusterEstimation(GFID(newParams))[0]["maxRSS"])

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

maxes = getTCSelectionMaxes(timeCourses, selectionList=list(range(10)), 
                            varSelection=showValues, valRemove=[0,1])

maxes = breakSeriesByScale(maxes,maxRunLength=25)

TCVis = timeCourseVisualiser(timeCourses)

for i in range(len(maxes)):
    TCVis.multiPlot(indexSelect=list(range(10)),varSelect=maxes[i],
                    save=os.path.join(fig_dir,'timeCourse'+str(i)+'.png'))
    
suspPar = pd.Series(data={key:value for key, value in
                          zip(compSerise.index,compSerise.values) if
                          math.modf(value)[0]==0.0})
    
suspPar.to_csv(path_or_buf=os.path.join(working_dir,
                                        'suspiciousParamiters.csv'))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 16:38:20 2021

@author: peter
"""

from python.pycotoolsHelpers import *
from python.utilityTools import *
from python.visualisationTools import *
import re
import pandas as pd

cmdDict, cmdFlags = getCmdLineArgs()

def removeUnderScores(dfOrListLike):
    myDict ={"AMPK_P":"AMPK-P",
             "PGC1a_deacet":"deacylated PGC1a",
             "Mito_old":"old mitochondria",
             "_":" "}
    if isinstance(dfOrListLike,pd.DataFrame):
        df = dfOrListLike.copy()
        if len(df)>0:
            for col in df.columns:
                if isinstance(df[col].iloc[0],str):
                    df[col] = df[col].apply(removeUnderScores)
        df.columns = removeUnderScores(df.columns)
        return df
    elif isinstance(dfOrListLike,str):
        myStr = dfOrListLike
        for k,v in myDict.items():
            myStr = myStr.replace(k,v)
        return myStr
    else:
        return [removeUnderScores(i) for i in dfOrListLike]

if "name" in cmdDict.keys():
    name = cmdDict["name"]
else:
    name = "reConf12"
nameS = "reConf12R2"
if nameS is None:
    nameS = name
    
PECase = 0
# 1 works
    
mySuperComputer = "slurm" in cmdFlags

myLedLoc = (0.1,0.85) #'upper left'
myLedLoc2 = (0.05,0.85) #'upper left'
myLedLoc3 = (0.0475,0.85) #'upper left'

# add path to copasiSE to path varaiable if not on rocket clustor
if not mySuperComputer:
    addCopasiPath("/Applications/copasi")

RS = loadPick(['data', nameS, 'runSwitches.p'],relative=True)

newParams = loadPick(['data', nameS, 'new-params.p'],relative=True)

runDir = resolvePath(["copasiRuns",nameS+"-mitoSim"], relative=True)

mitoMod = modelRunner(antString=RS['mitoAntStr'],run_dir=runDir)

mitoMod.clearRunDirectory()
df = GFID(newParams).copy()
df = df.drop(columns="RSS")

df = pd.DataFrame([df.iloc[PECase] for _ in range(1)])
df.reset_index(drop=True, inplace=True)
df["Induced_PGC1a_deacetylation_k1"] = 0.0
df["PGC1a_acetylation_k1"] = 0.0
df["Basal_PGC1a_deacetylation_v"] = 0.0
df["SIRT1"] = 0.0

timeCourse2 = mitoMod.runTimeCourse(24*365*80,
                                   adjustParams=df,
                                   #rocket=mySuperComputer,
                                   #subSet = [0],
                                   stepSize=6.0,
                                   genReactions=False)

selVar = ['Mito_new', 'Mito_old', 'Damage', 'Mito_turnover',
          'Mitophagy', 'NAD', 'AICAR_treatment', 'PGC1a_deacet']

for TC in timeCourse2:
    TC["Time"] = TC["Time"]/(24*365)

mitoMod.clearRunDirectory()
df = GFID(newParams).copy()
df = df.drop(columns="RSS")

df = pd.DataFrame([df.iloc[PECase] for _ in range(2)])
df.reset_index(drop=True, inplace=True)
df["PARP"] = 1.0
df.iloc[1, df.columns.get_loc("PARP")] = 2.5
#df.iloc[2, df.columns.get_loc("PARP")] = 0.25

timeCourse = mitoMod.runTimeCourse(24*365*80,
                                   adjustParams=df,
                                   #rocket=mySuperComputer,
                                   #subSet = [0],
                                   stepSize=6.0,
                                   genReactions=False)

selVar = ['Mito_old']

for TC in timeCourse:
    TC["Time"] = TC["Time"]/(24*365)

timeCourse = timeCourse + timeCourse2

mitoVis = timeCourseVisualiser(removeUnderScores(timeCourse))

mitoVis.multiPlot(varSelect=removeUnderScores(selVar), style="ticks",
                  save = resolvePath(["figures", name, "mitoSimFig8.png"], 
                                     relative=True),
                  xAxisLabel = "Time (yr)", yAxisLabel = "%",
                  varAsAxis = True, wrapNumber=1, figsize = (6,5),
                  legend=["[1]","[2]","[3]"], legendLoc = myLedLoc)
print("begin next set")
mitoMod.clearRunDirectory()
df = GFID(newParams).copy()
df = df.drop(columns="RSS")

df = pd.DataFrame([df.iloc[PECase] for _ in range(2)])
df.reset_index(drop=True, inplace=True)
df["explosionRatePARP"] = 0.0
# df.iloc[1, df.columns.get_loc("explosionRatePARP")] = 0.000005/(24*365*80)
df.iloc[1, df.columns.get_loc("explosionRatePARP")] = 3*10**(-6)

timeCourse = mitoMod.runTimeCourse(24*365*80,
                                   adjustParams=df,
                                   #rocket=mySuperComputer,
                                   #subSet = [0],
                                   stepSize=6.0,
                                   genReactions=False)

selVar = ['Mito_old', 'PARP']

for TC in timeCourse:
    TC["Time"] = TC["Time"]/(24*365)
    
timeCourse = timeCourse + timeCourse2

mitoVis = timeCourseVisualiser(removeUnderScores(timeCourse))

mitoVis.multiPlot(varSelect=removeUnderScores(selVar), style="ticks",
                  save = resolvePath(["figures", name, "mitoSimS28.png"], 
                                     relative=True),
                  xAxisLabel = "Time (yr)", yAxisLabel = ["%","(AU)"],
                  varAsAxis = True, wrapNumber=3, figsize = (12,5),
                  legend=["[1]","[2]","[3]"], legendLoc = myLedLoc2)

print("begin next set")
mitoMod.clearRunDirectory()
df = GFID(newParams).copy()
df = df.drop(columns="RSS")

df = pd.DataFrame([df.iloc[PECase] for _ in range(2)])
df.reset_index(drop=True, inplace=True)
df["bleedRateAMPK"] = 0.0
#df.iloc[1, df.columns.get_loc("bleedRateAMPK")] = 0.00001/(24*365*80)
df.iloc[1, df.columns.get_loc("bleedRateAMPK")] = 10**(-6)

timeCourse = mitoMod.runTimeCourse(24*365*80,
                                   adjustParams=df,
                                   #rocket=mySuperComputer,
                                   #subSet = [0],
                                   stepSize=6.0,
                                   genReactions=False)

selVar = ['Mito_old', 'AMPK', 'AMPK_P']

for TC in timeCourse:
    TC["Time"] = TC["Time"]/(24*365)
    
timeCourse = timeCourse + timeCourse2

mitoVis = timeCourseVisualiser(removeUnderScores(timeCourse))

mitoVis.multiPlot(varSelect=removeUnderScores(selVar), style="ticks",
                  save = resolvePath(["figures", name, "mitoSimS30.png"], 
                                     relative=True),
                  xAxisLabel = "Time (yr)", yAxisLabel = ["%","(AU)","(AU)"],
                  varAsAxis = True, wrapNumber=3, figsize = (18,5),
                  legend=["[1]","[2]","[3]"], legendLoc = myLedLoc3)

print("begin next set")
mitoMod.clearRunDirectory()
df = GFID(newParams).copy()
df = df.drop(columns="RSS")

df = pd.DataFrame([df.iloc[PECase] for _ in range(2)])
df.reset_index(drop=True, inplace=True)
df["bleedRateSIRT"] = 0.0
#df.iloc[1, df.columns.get_loc("bleedRateSIRT")] = 0.000002/(24*365*80)
df.iloc[1, df.columns.get_loc("bleedRateSIRT")] = 10**(-6)

timeCourse = mitoMod.runTimeCourse(24*365*80,
                                   adjustParams=df,
                                   #rocket=mySuperComputer,
                                   #subSet = [0],
                                   stepSize=6.0,
                                   genReactions=False)

selVar = ['Mito_old', 'SIRT1']

for TC in timeCourse:
    TC["Time"] = TC["Time"]/(24*365)
    
timeCourse = timeCourse + timeCourse2

mitoVis = timeCourseVisualiser(removeUnderScores(timeCourse))

mitoVis.multiPlot(varSelect=removeUnderScores(selVar), style="ticks",
                  save = resolvePath(["figures", name, "mitoSimS29.png"], 
                                     relative=True),
                  xAxisLabel = "Time (yr)", yAxisLabel = ["%","(AU)"],
                  varAsAxis = True, figsize = (12,5),
                  legend=["[1]","[2]","[3]"], legendLoc = myLedLoc2)

print("begin next set")
mitoMod.clearRunDirectory()
df = GFID(newParams).copy()
df = df.drop(columns="RSS")

df = pd.DataFrame([df.iloc[PECase] for _ in range(2)])
df.reset_index(drop=True, inplace=True)
df["explosionRateGlucose"] = 0.0
#df.iloc[1, df.columns.get_loc("explosionRateGlucose")] = 0.5/(24*365*80)
df.iloc[1, df.columns.get_loc("explosionRateGlucose")] = 7

timeCourse = mitoMod.runTimeCourse(24*365*80,
                                   adjustParams=df,
                                   #rocket=mySuperComputer,
                                   #subSet = [0],
                                   stepSize=6.0,
                                   genReactions=False)

selVar = ['Mito_old', 'Glucose']

for TC in timeCourse:
    TC["Time"] = TC["Time"]/(24*365)
    
timeCourse = timeCourse + timeCourse2

mitoVis = timeCourseVisualiser(removeUnderScores(timeCourse))

mitoVis.multiPlot(varSelect=removeUnderScores(selVar), style="ticks",
                  save = resolvePath(["figures", name, "mitoSimS31.png"], 
                                     relative=True),
                  xAxisLabel = "Time (yr)", yAxisLabel = ["%","(AU)"],
                  varAsAxis = True, figsize = (12,5),
                  legend=["[1]","[2]","[3]"], legendLoc = myLedLoc2)

print("begin next set")
mitoMod.clearRunDirectory()
df = GFID(newParams).copy()
df = df.drop(columns="RSS")

df = pd.DataFrame([df.iloc[PECase] for _ in range(2)])
df.reset_index(drop=True, inplace=True)
df["NR_NMN"] = 0.0
df.iloc[1, df.columns.get_loc("NR_NMN")] = 100

timeCourse = mitoMod.runTimeCourse(24*365*80,
                                   adjustParams=df,
                                   #rocket=mySuperComputer,
                                   #subSet = [0],
                                   stepSize=6.0,
                                   genReactions=False)

selVar = ['Mito_old']

for TC in timeCourse:
    TC["Time"] = TC["Time"]/(24*365)

timeCourse = timeCourse + timeCourse2

mitoVis = timeCourseVisualiser(removeUnderScores(timeCourse))

mitoVis.multiPlot(varSelect=removeUnderScores(selVar),
                  save = resolvePath(["figures", name, "mitoSimS32.png"], 
                                     relative=True), style="ticks",
                  xAxisLabel = "Time (yr)", yAxisLabel = "%",
                  varAsAxis = True, wrapNumber=1, figsize = (6,5),
                  legend=["[1]","[2]","[3]"], legendLoc = myLedLoc)

"""
mitoMod.clearRunDirectory()
df = GFID(newParams).copy()
df = df.drop(columns="RSS")

df = pd.DataFrame([df.iloc[0] for _ in range(3)])
df.reset_index(drop=True, inplace=True)
df["myDose"] = 0.0
df.iloc[1, df.columns.get_loc("myDose")] = 1.0
df.iloc[2, df.columns.get_loc("myDose")] = 10.0

timeCourse = mitoMod.runTimeCourse(24*365*80,
                                   adjustParams=df,
                                   #rocket=mySuperComputer,
                                   #subSet = [0],
                                   stepSize=6,
                                   genReactions=False)

for TC in timeCourse:
    TC["Time"] = TC["Time"]/(24*365)

mitoVis = timeCourseVisualiser(timeCourse)

mitoVis.multiPlot(varSelect=selVar,
                  save = resolvePath(["figures", name, "mitoSim2.png"], 
                                     relative=True))
"""
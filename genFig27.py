#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 17:10:23 2021

@author: peter
"""

from python.pycotoolsHelpers import *
from python.utilityTools import *
from python.visualisationTools import *

cmdDict, cmdFlags = getCmdLineArgs()

if "name" in cmdDict.keys():
    name = cmdDict["name"]
else:
    name = "reConf12"
nameS = None #"reConf12R2"
if nameS is None:
    nameS = name
    
PECase = 0
    
mySuperComputer = "slurm" in cmdFlags
    
# add path to copasiSE to path varaiable if not on rocket clustor
if not mySuperComputer:
    addCopasiPath("/Applications/copasi")

RS = loadPick(['data', nameS, 'runSwitches.p'],relative=True)

newParams = loadPick(['data', nameS, 'new-params.p'],relative=True)

runDir = resolvePath(["copasiRuns",nameS+"-s27fig"], relative=True)

antStrBD = getModelsAndFunctions(RS["antimony_string"])

antStr = [i["text"].splitlines() for i in antStrBD["models"]]
for i in range(len(antStr)):
    antStr[i] = antStr[i][:-1]+["AICAR_new = 0.0;",
            "at (time>=24): AICAR_treatment=AICAR_new;"]+[antStr[i][-1]]
    antStr[i] = "\n".join(antStr[i])
antStr = "\n".join(antStr)
antStr = [i for i in antStr.splitlines()
          if not bool(re.match(r".*\bis\b.*", i))]
antStr = "\n".join(antStr)
antStr = ("\n".join([i["text"] for i in antStrBD["functions"]]) + 
          "\n" + antStr)

mitoMod = modelRunner(antString=antStr,run_dir=runDir)

mitoMod.clearRunDirectory()
df = GFID(newParams).copy()
df = df.drop(columns="RSS")

df = pd.DataFrame([df.iloc[PECase] for _ in range(6)])
df.reset_index(drop=True, inplace=True)
df["PARP"] = 1.0
df.iloc[1, df.columns.get_loc("PARP")] = 2.5
df.iloc[3, df.columns.get_loc("PARP")] = 2.5
df.iloc[4, df.columns.get_loc("PARP")] = 2.5
df.iloc[5, df.columns.get_loc("PARP")] = 2.5
df["AICAR_new"] = 0.0
df.iloc[2, df.columns.get_loc("AICAR_new")] = 1
df.iloc[3, df.columns.get_loc("AICAR_new")] = 1
df.iloc[4, df.columns.get_loc("AICAR_new")] = 1
df.iloc[5, df.columns.get_loc("AICAR_new")] = 1
df["NR_NMN"] = 0.0
df.iloc[4, df.columns.get_loc("NR_NMN")] = 500

indexNames = ["Ctrl", "Ctrl", "AIC", "AIC", "NR+AIC", "PJ34+AIC"] 
indexNames = {i:j for i,j in enumerate(indexNames)}

timeCourse2 = mitoMod.runTimeCourse(24*2,
                                   adjustParams=df,
                                   #rocket=mySuperComputer,
                                   #subSet = [0],
                                   stepSize=0.25,
                                   genReactions=False)

selVar = ['AMPK-P (AU)']
timeCourse2 = [i.rename(columns={"AMPK_P": "AMPK-P (AU)"}) 
               for i in timeCourse2]

mitoVis = timeCourseVisualiser(timeCourse2)

colours = [(0.0,0.0,1.0),(1.0,0.0,0.0),
           (0.0,0.0,1.0),(1.0,0.0,0.0),(1.0,0.0,0.0),(1.0,0.0,0.0)]

mitoVis.barChart(24*2,varSelect=selVar,
                 save = resolvePath(["figures", name, "figS27.png"],
                                    relative=True),
                 style="ticks", indexSelect = indexNames,
                 colourOveride = colours, varOnAxis = True,
                 spacing = [False,False,True,False,False,False,False],
                 figsize=(6,5))
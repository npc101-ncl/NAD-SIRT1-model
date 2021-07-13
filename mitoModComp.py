#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 16:39:56 2021

@author: peter
"""

from python.pycotoolsHelpers import *
from python.utilityTools import *
from python.debugTools import *
import re
import pandas as pd

cmdDict, cmdFlags = getCmdLineArgs()

if "name" in cmdDict.keys():
    name = cmdDict["name"]
else:
    name = "reConf12"
    
mySuperComputer = "slurm" in cmdFlags
    
# add path to copasiSE to path varaiable if not on rocket clustor
if not mySuperComputer:
    addCopasiPath("/Applications/copasi")

RS = loadPick(['data', name, 'runSwitches.p'],relative=True)

cpsPath = resolvePath(["oldModel","NAD_model_files",
                       "AMPK-NAD-PGC1a-SIRT1-model",
                       "Model_Version6_Integrated_Mitochondria.cps"],
                      requireExt="cps",relative=True)

runDir = resolvePath(["copasiRuns","test2"], relative=True)

cpsMod = modelRunner(run_dir=runDir, CopasiFile = cpsPath)

runDir = resolvePath(["copasiRuns","test3"], relative=True)

antMod = modelRunner(antString=RS['mitoAntStr'],run_dir=runDir)

cpsE = cpsMod.getModelEliments()
antE = antMod.getModelEliments()

resCps = {}
resAnt = {}
for k in cpsE.keys():
    resCps[k] = list(set(cpsE[k])-set(antE[k]))
    resAnt[k] = list(set(antE[k])-set(cpsE[k]))

"""
print(resCps["kineticParams"])
print("\n".join([i for i in cpsMod.antString.splitlines()
                 if any([(j in i) for j in resCps["kineticParams"]])]))
    
print(resAnt["kineticParams"])
print("\n".join([i for i in RS['mitoAntStr'].splitlines()
                 if any([(j in i) for j in resAnt["kineticParams"]])]))
"""

cpsP = cpsMod.extractModelParam()
antP = antMod.extractModelParam()

"""
interP = list(set(cpsP.keys()).intersection(set(antP.keys())))

for i in interP:
    if abs(float(cpsP[i])-float(antP[i]))>0:
        print(i, cpsP[i], antP[i])
"""

compList = [["AMPK-P","AMPK_P"],
            ["PGC1a-P","PGC1a_P"],
            ["NR-NMN","NR_NMN"],
            ["Glucose_input_v","Glucose_source"],
            ["AICAR_Delay","AICAR_DelayA"],
            ["GlucoseDelay","GlucoseDelayA"],
            ["Deacetylation_Delay","PGC1a_Deacetylation_Activity"]]

for i, j in compList:
    if abs(float(cpsP[i])-float(antP[j]))>0:
        print(i, cpsP[i], j, antP[j])
        
"""
function Hill_Cooperativity(substrate, Shalve, V, h)
  0.1013*((25/5.36174)**15.04)/(1 + ((25/5.36174)**15.04));
end

Hill_Cooperativity(25, 5.36174, 0.1013, 15.04)/0.1
=GlucoseDelay

GlucoseDelay is in stable point at aprox 1.01 and starts at 1
but GlucoseDelayA is suposed to start in a stable state by default but
is miles away from that
"""

"""
function Alpha_Constant(Shalve, k2, h)
  5.36174*(0.0001**(-1/15.04));
end
Glucose_DUMMY_REACTION_delay_alpha = Alpha_Constant(5.36174, 0.1, 15.04)
function Power_Law_Rate(substrate, alpha, h)
  (25/6.248778235795812)**15.04;
end
Power_Law_Rate(25, 6.248778235795812, 15.04)/Glucose_DUMMY_REACTION_delay_limiter_k2
=GlucoseDelayA

is Glucose_induced_AMPK_dephosphorylation_k1 estimated? if so change
Glucose_DUMMY_REACTION_delay_limiter_k2 to 0.0001 or lower
"""

newParam = loadPick(['data', name, 'new-params.p'],relative=True)

for col in GFID(newParam).columns:
    if col in antP.keys():
        print(col, GFID(newParam).iloc[0][col], antP[col])
    else:
        print(col, "missing")
  
    
boundVars = antE["metabolites"]+antE["assignments"]
testParam = GFID(newParam).iloc[0].to_dict()
if "RSS" in testParam:
    del testParam["RSS"]
myDebug = modelDebugger(RS['mitoAntStr'], nonNegVar=boundVars,
                        ceilingVar=boundVars, ceiling=100000)      
debugResults = myDebug.debug(0, 24*365*60, 24*365*60, isEular=False,
                             overrides=testParam)
print(debugResults)   

tc = loadPick(['data', name, 'new-timeCourses.p'],relative=True)
temp = [[k for k,v in i.iloc[0].items() if v<0] for i in tc]
temp = {i:k for i,k in enumerate(temp) if len(k)>0}
print(temp)
temp = [[j for j in i.columns if any(i[j]!=i.iloc[0][j])] for i in tc]
print(temp)
temp = pd.DataFrame([i.iloc[0] for i in tc])
temp = temp[[i for i in temp.columns
            if i.endswith("_T") or i.endswith("_alpha")]]
print(temp.iloc[0])
(tc[3]["Glucose"]/tc[3]["Glucose_DUMMY_REACTION_delay_T"])
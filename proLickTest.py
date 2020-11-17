#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 13:10:08 2020

@author: peter
"""

import site, os, re
import pandas as pd
from python.pycotoolsHelpers import *
from python.utilityTools import *
from python.visualisationTools import *
import pickle
import time, sys

vis = True

cmdDict, cmdFlags = getCmdLineArgs()

mySuperComputer = "slurm" in cmdFlags

if mySuperComputer:
    vis = False

if "copys" in cmdDict.keys():
    myCopyNum = cmdDict["copys"]
    try:
        myCopyNum = int(myCopyNum)
    except:
        myCopyNum = 10
else:
    myCopyNum = 10

if "depth" in cmdDict.keys():
    myDepth = cmdDict["depth"]
    try:
        myDepth = int(myDepth)
    except:
        myDepth = 10
else:
    myDepth = 10

if "meth" in cmdDict.keys():
    methDict = cmdDict["meth"]
    methDict = [l.split(":") for l in methDict.split(",")]
    methDict = {l[0]:l[1] for l in methDict if len(l)==2}
    for mKey in methDict.keys():
        try:
            methDict[mKey] = float(methDict[mKey])
            if methDict[mKey].is_integer():
                methDict[mKey] = int(methDict[mKey])
            else:
                pass
        except:
            pass
else:
    methDict = None
    
if "cases" in cmdDict.keys():
    myCaseCount = cmdDict["cases"]
    try:
        myCaseCount = int(myCaseCount)
    except:
        myCaseCount = 1
else:
    myCaseCount = 1

if not mySuperComputer:
    addCopasiPath("/Applications/copasi")

working_directory = os.path.dirname(os.path.abspath(__file__))
run_dir = os.path.join(working_directory,'copasiRuns', 'toy')
if not os.path.isdir(run_dir):
    os.makedirs(run_dir)

toyAnt = """
model negative_feedback

    compartment cell = 1.0
    var A in cell
    var B in cell
    
    vAProd = 0.1
    kADeg = 0.2
    kBProd = 0.3
    kBDeg = 0.4
    A=0
    B=0
    
    AProd: => A; cell*vAProd
    ADeg: A =>; cell*kADeg*A*B
    BProd: => B; cell*kBProd*A
    BDeg: B => ; cell*kBDeg*B

end
"""

if not vis:
    toyModel = modelRunner(toyAnt, run_dir)
    
    # 0 to 100 step size 10
    
    timeCourse = toyModel.runTimeCourse(100, stepSize=10) 
    
    expPath = os.path.join(run_dir,"exp.csv")
    
    timeCourse.drop(columns=["vAProd","kADeg","kBProd","kBDeg"]).to_csv(
            path_or_buf=expPath)
    
    myMeth = {'method':'hooke_jeeves'}
    
    params = toyModel.runParamiterEstimation(expPath,copyNum=myCopyNum,
                                             rocket=mySuperComputer,
                                             method=myMeth)
    
    for case in range(myCaseCount):
        override = GFID(params).iloc[case].drop(labels=["RSS"]).to_dict()
        estVar = list(override.keys())
        myRange = [10**((x-9)/3) for x in range(19)]
        myPL = toyModel.runProfileLikelyhood(expPath, myRange, estVar,
                                             rocket=mySuperComputer,
                                             overrideParam=override,
                                             depth=myDepth,
                                             method = methDict)
        # maybe try aneeling methiod with non random start point?
        savePick(["data","toy","PL"+str(case)+".p"], myPL, relative=True)
else:
    
    out_string = ""
    
    for paramCase in range(3):
        
        myPL = loadPick(["data","toy","PL"+str(paramCase)+".p"], relative=True)
        
        out_string = out_string + str(myPL[1]) + "\n"
        
        myVis = profileLikelyhoodVisualisor(myPL)
        
        chunkSize=25
        cols=5
        varNameMax=20
        
        
        chunks = [list(myPL[0].keys())[chunkSize*i:chunkSize*(i+1)] for i
                  in range(len(myPL[0].keys()))
                  if len(list(myPL[0].keys())[chunkSize*i:chunkSize*(i+1)])>0]
    
        for chunk, i in zip(chunks,range(len(chunks))):
            df = []
            for variable in chunk:
                tdf = myPL[0][variable][[variable,"RSS"]].copy()
                tdf= tdf.rename(columns={variable:"adjustment"})
                tdf["variable"] = variable
                if variable in myPL[1].keys():
                    if myPL[1][variable]!=0:
                        tdf["adjustment"] = tdf["adjustment"]/myPL[1][variable]
                    else:
                        print(variable,":",myPL[1][variable])
                else:
                    print("missing",variable)
                df.append(tdf)
            df = pd.concat(df, ignore_index=True)
            rows = len(chunk)//cols
            if len(chunk)%cols>0:
                rows=rows+1
            fig, axs = plt.subplots(rows, cols, sharex=True, sharey=True,
                                    figsize=(12,10))
            axs = trim_axs(axs,len(chunk))
            print(df)
            for ax, variable in zip(axs,chunk):
                ax.set_xscale('log')
                ax.set_yscale('log')
                if len(variable)>varNameMax:
                    myTitle = (variable[:varNameMax//2]+"..."+
                               variable[(len(variable)-varNameMax//2):])
                else:
                    myTitle = variable
                ax.title.set_text(myTitle)
                """
                tdf = df[df["variable"]==variable].groupby(['adjustment']).min()
                """
                tdf = df[df["variable"]==variable]
                tdf["level"] = tdf.groupby(['adjustment']).cumcount()
                tdf = tdf.sort_values(by=["level",'adjustment'])
                for myLev in set(tdf["level"]):
                    ax.plot(tdf[tdf["level"]==myLev]['adjustment'],
                            tdf[tdf["level"]==myLev]["RSS"])
            fig.tight_layout()
            fig.savefig(os.path.join(working_directory,'figures', 'toy', "PL"+
                                     str(paramCase)+"-"+str(i)+".png"))
    myPath = resolvePath(["figures","toy","param.txt"],relative=True)
    f = open(myPath, "w")
    f.write(out_string)
    f.close()
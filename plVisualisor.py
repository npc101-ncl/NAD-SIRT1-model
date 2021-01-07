#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 18:33:54 2020

@author: peter
"""

from python.visualisationTools import *
from python.analysisTools import *
from python.utilityTools import *
import os, re, sys
import pandas as pd
import pickle
import seaborn as sns
import matplotlib.pyplot as plt

name = "reConf8"

working_directory = os.path.dirname(os.path.abspath(__file__))


paramCase=0

myPL = loadPick(["data",name,"proLick-"+str(paramCase)+".p"],
                 relative=True)

tolerance = {'NAD_synthesis_v':0.02,
             'Glucose_DUMMY_REACTION_delay_Shalve':0.02,
             'NAD_increase_by_AMPK_V':0.02,
             'NAD_negative_regulation_k1':0.015}
upperBound = {key:value["RSS"] for key, value
              in myPL[0].items()}
for key in upperBound.keys():
    if key in tolerance.keys():
        temoTol = tolerance[key]
    else:
        temoTol = 0.01
    upperBound[key] = upperBound[key][upperBound[key]<np.inf]
    upperBound[key] = (upperBound[key].min(skipna=True)+
              temoTol*(upperBound[key].max(skipna=True)-
                       upperBound[key].min(skipna=True)))
    
lowerAdjBound = {}
upperAdjBound = {}
for key, value in upperBound.items():
    temp = myPL[0][key]
    temp = temp[temp["RSS"]<=value]
    lowerAdjBound[key] = temp[key].min()
    upperAdjBound[key] = temp[key].max()

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
    fig, axs = plt.subplots(rows, cols, sharex=True, figsize=(12,10))
    axs = trim_axs(axs,len(chunk))
    for ax, variable in zip(axs,chunk):
        ax.set_xscale('log')
        if len(variable)>varNameMax:
            myTitle = (variable[:varNameMax//2]+"..."+
                       variable[(len(variable)-varNameMax//2):])
        else:
            myTitle = variable
        ax.title.set_text(myTitle)
        ax.plot(df[df["variable"]==variable]["adjustment"],
                df[df["variable"]==variable]["RSS"])
        if variable in upperBound.keys():
            ax.axhline(upperBound[variable])
            ax.axvline(lowerAdjBound[variable]/myPL[1][variable])
            ax.axvline(upperAdjBound[variable]/myPL[1][variable])
    fig.tight_layout()
    os.makedirs(resolvePath(['figures', name],relative=True),exist_ok=True)
    fig.savefig(os.path.join(working_directory,'figures', name, "PL"+
                             str(paramCase)+"-"+str(i)+".png"))
    
savePick(["data",name,"PE_bounds.p"],
         {"lowerBounds":lowerAdjBound, "upperBounds":upperAdjBound},
         relative=True)

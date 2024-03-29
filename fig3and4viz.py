#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 15:25:08 2020

@author: peter
"""

import site, os, re
import pandas as pd
from python.analysisTools import *
from python.visualisationTools import *
import pickle
import seaborn as sns
import time, sys

cmdLineArg = sys.argv[1:]

def removeUnderScores(dfOrListLike):
    myDict ={"AMPK_P":"AMPK-P",
             "PGC1a_deacet":"deacylated PGC1a",
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

name = [name[5:] for name in cmdLineArg if (name.startswith("name:") and 
        len(name)>5)]
if len(name)>0:
    name = name[0]
else:
    name = "reConf12"
    
indexToShow = [0]

working_directory = os.path.dirname(os.path.abspath(__file__))

data_dir = os.path.join(working_directory,'data', name)

fig_dir = os.path.join(working_directory,'figures',name)
if not os.path.isdir(fig_dir):
    os.makedirs(fig_dir)

file = open(os.path.join(data_dir,'runSwitches.p'),'rb')
RS = pickle.load(file)
file.close()

f = open(os.path.join(data_dir,'new-params.p'), "rb" )
newParams = pickle.load(f)
f.close()

RSScutoff = min(GFID(newParams)["RSS"].iloc[9],
                RSSClusterEstimation(GFID(newParams))[0]["maxRSS"])
indexCutoff = range(min(10,
                        RSSClusterEstimation(GFID(newParams))[0]["size"]))
if indexToShow is None:
    indexToShow = list(indexCutoff)

file = open(os.path.join(data_dir, 'fig3Cont-timeCourses.p'),'rb')
f3CtimeCourse = pickle.load(file)
file.close()

f3CtimeCourse = [tc.reset_index(drop=True) for tc in f3CtimeCourse]

file = open(os.path.join(data_dir, 'fig3GI-timeCourses.p'),'rb')
f3GItimeCourse = pickle.load(file)
file.close()

f3GItimeCourse = [tc.reset_index(drop=True) for tc in f3GItimeCourse]

TCVis = timeCourseVisualiser(f3CtimeCourse)
TCVis.multiPlot(indexSelect=indexToShow,
                varSelect=["AMPK-P","NAD","PGC1a_deacet"],
                save=os.path.join(fig_dir,'fig3Cont.png'),
                style="ticks", varAsAxis = True, xAxisLabel = "Time (hr)",
                yAxisLabel = "(AU)", wrapNumber=1, figsize = (4,10))

TCVis = timeCourseVisualiser(f3GItimeCourse)
TCVis.multiPlot(indexSelect=indexToShow,
                varSelect=["AMPK-P","NAD","PGC1a_deacet"],
                save=os.path.join(fig_dir,'fig3GI.png'),
                style="ticks", varAsAxis = True, xAxisLabel = "Time (hr)",
                yAxisLabel = "(AU)", wrapNumber=1, figsize = (4,10))

f3timeCourse = [f3CtimeCourse[0], f3GItimeCourse[0]]

TCVis = timeCourseVisualiser([removeUnderScores(i) for i in f3timeCourse])
TCVis.multiPlot(varSelect=removeUnderScores(["AMPK-P","NAD","PGC1a_deacet"]),
                save=os.path.join(fig_dir,'fig3.png'),
                style="ticks", varAsAxis = True, xAxisLabel = "Time (hr)",
                yAxisLabel = "(AU)", wrapNumber=1, figsize = (4,10))

fig4IC = ["cont", "GI", "GINR", "GIPJ"]

timeCourseFig4 = {}
for ICName in fig4IC:
    file = open(os.path.join(data_dir, "fig4"+ICName+"-timeCourses.p"),'rb')
    timeCourseFig4[ICName] = pickle.load(file)
    file.close()
    file = open(os.path.join(data_dir, "fig4"+ICName+"AIC-timeCourses.p"),
                'rb')
    timeCourseFig4[ICName+"AIC"] = pickle.load(file)
    file.close()

myDict = {}
for name, timeCourses in timeCourseFig4.items():
    df = []
    for TC in timeCourses:
        if isinstance(TC,pd.DataFrame):
            #print(TC.iloc[-1].copy().to_dict())
            if TC.iloc[-1]["Time"] == 12:
                df.append(TC.iloc[-1].copy().to_dict())
            else:
                df.append({})
        else:
            df.append({})
            print("not df")
    df = pd.DataFrame(df)
    df["Index"] = list(df.index)
    myDict[name] = df.copy()
df = []
for name, finStates in myDict.items():
    df2 = pd.melt(finStates, id_vars=["Index"])
    df2["condition"] = name
    df.append(df2)
df = pd.concat(df, ignore_index=True)

indexOveride = 1
if indexToShow != list(indexCutoff):
    df = df[df["Index"].isin(indexToShow)]
else:
    df = df[df["Index"] <= min(max(list(indexCutoff)),indexOveride)]

df = df[df["condition"]!="GINR"]
df = df[df["condition"]!="GIPJ"]
df2 = df[df["variable"]=="NAD"].copy()
df2 = df2.rename(columns={"value":"NAD (AU)"})
df2 = df2.replace({'condition': {"contAIC":"AIC", "GIAIC":"GI+AIC",
                                 "GINRAIC":"GI+NR+AIC",
                                 "GIPJAIC":"GI+PJ34+AIC"}})

df2["   "]=df2["condition"].apply(lambda x: "Genomic instability" 
   if x[:2]=="GI" else "WT")
myOrder = ["cont", "GI", "AIC", "GI+AIC", "GI+NR+AIC", "GI+PJ34+AIC"]
with sns.axes_style(style="ticks"):
    plt.figure()
    bp = sns.barplot(x="condition", y="NAD (AU)", hue="   ",
                     data=df2, order=myOrder, dodge=False)
    #bp.set_xticklabels(bp.get_xticklabels(),rotation = 45)
    #plt.xticks(rotation=45)
    bp.get_figure().savefig(os.path.join(fig_dir,'fig4NAD.png'))


df2 = df[df["variable"]=="PGC1a_deacet"].copy()
df2 = df2.rename(columns={"value":"PGC1a_deacet (AU)"})
df2 = df2.replace({'condition': {"contAIC":"AIC", "GIAIC":"GI+AIC",
                                 "GINRAIC":"GI+NR+AIC",
                                 "GIPJAIC":"GI+PJ34+AIC"}})
    
df2["   "]=df2["condition"].apply(lambda x: "Genomic instability" 
   if x[:2]=="GI" else "WT")
with sns.axes_style(style="ticks"):
    plt.figure()
    bp = sns.barplot(x="condition", y=removeUnderScores("PGC1a_deacet (AU)"), 
                     hue="   ", data=removeUnderScores(df2), 
                     order=myOrder, dodge=False)
    bp.get_figure().savefig(os.path.join(fig_dir,'fig4PGC1a_d.png'))

#######

file = open(os.path.join(data_dir, 'figAlphaCont-timeCourses.p'),'rb')
fAlphaCtimeCourse = pickle.load(file)
file.close()

file = open(os.path.join(data_dir, 'figAlphaNoSirt-timeCourses.p'),'rb')
fAlphaNotimeCourse = pickle.load(file)
file.close()

TCVis = timeCourseVisualiser(fAlphaCtimeCourse)
TCVis.multiPlot(indexSelect=indexToShow,
                varSelect=["AMPK-P","NAD","PGC1a_deacet"],
                save=os.path.join(fig_dir,'figAlphaCont.png'),
                style="ticks")

TCVis = timeCourseVisualiser(fAlphaNotimeCourse)
TCVis.multiPlot(indexSelect=indexToShow,
                varSelect=["AMPK-P","NAD","PGC1a_deacet"],
                save=os.path.join(fig_dir,'figAlphaNoSirt.png'),
                style="ticks")
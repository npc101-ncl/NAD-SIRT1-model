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
import seaborn as sns
import matplotlib.pyplot as plt

myStyle = "ticks"

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

def showValsFunc(timeCourses,newParams):
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
    return showValues        

cmdLineArg = sys.argv[1:]

name = [name[5:] for name in cmdLineArg if (name.startswith("name:") and 
        len(name)>5)]
if len(name)>0:
    name = name[0]
else:
    name = "reConf12"

working_dir = os.path.abspath('')

fig_dir = os.path.join(working_dir,'figures',name)
if not os.path.isdir(fig_dir):
    os.makedirs(fig_dir)

data_dir = os.path.join(working_dir,'data', name)

file = open(os.path.join(data_dir,'runSwitches.p'),'rb')
RS = pickle.load(file)
file.close()

def probeIC(ID):
    for dia in RS['diagrams']:
        if dia["name"]==ID:
            if isinstance(dia["IC"],list):
                df = pd.DataFrame([RS["ICTrack"][i] for i in dia["IC"]]).T
            else:
                df = pd.DataFrame([RS["ICTrack"][dia["IC"]]])
            return df
    return None

def probeConditions(ID):
    for dia in RS['diagrams']:
        if dia["name"]==ID:
            if 'Timepoint (hr)' in dia["DS"]:
                return dia["DS"]['Timepoint (hr)']
            else:
                return None
    return None
 
f = open(os.path.join(data_dir,'new-params.p'), "rb" )
newParams = pickle.load(f)
f.close()

f = open(os.path.join(data_dir,'new-timeCourses.p'), "rb" )
timeCourses = pickle.load(f)
f.close()

PEVis = parameterEstimationVisualiser(newParams)

PEVis.waterFall(save=os.path.join(fig_dir,'waterfall.png'),
                indexNames="parameters", style=myStyle)

RSScutoff = min(GFID(newParams)["RSS"].iloc[9],
                RSSClusterEstimation(GFID(newParams))[0]["maxRSS"])
indexCutoff = range(min(3,
                        RSSClusterEstimation(GFID(newParams))[0]["size"]))

indexToShow = [0]
lableToShow = ["Simulation"]

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

for i, myDF in zip(range(len(RS["calDf"])),RS["calDf"]):
    f = open(os.path.join(data_dir,
                          'new-timeCourses'+str(i)+'.p'),'rb')
    timeCourses = pickle.load(f)
    f.close()
    
    
    showValues = showValsFunc(timeCourses,newParams)  
    showValues = [i for i in showValues if i in myDF.columns]          
    
    TCVis = timeCourseVisualiser([removeUnderScores(i) for i in timeCourses])
    if indexToShow is None:
        thisShowIndex = list(indexCutoff)
    else:
        thisShowIndex = indexToShow 
    TCVis.multiPlot(indexSelect=thisShowIndex, 
                    compLines=removeUnderScores(myDF),
                    varSelect=removeUnderScores(showValues), style=myStyle,
                    save=os.path.join(fig_dir,'timeCourseCal'+
                                      str(i)+'.png'),
                    xAxisLabel = "Time (hr)", yAxisLabel = "(AU)",
                    varAsAxis = True, wrapNumber=1, figsize = (6,5))

expNADLevels = [(i,j.iloc[-1]["NAD_fold_increase"]) for i, j
                in zip(range(len(RS["calDf"])),RS["calDf"])
                if "NAD_fold_increase" in j.columns]

S5df = []
for i, expNAD in expNADLevels:
    f = open(os.path.join(data_dir,
                          'new-timeCourses'+str(i)+'.p'),'rb')
    timeCourses = pickle.load(f)
    f.close()
    if (lableToShow is not None) and (indexToShow is not None):
        tempDict = {k:timeCourses[j].iloc[-1]["NAD_fold_increase"]
                    for j, k in zip(indexToShow,lableToShow)}
    elif indexToShow is not None:
        tempDict = {"Simulation "+str(j):timeCourses[j].iloc[-1][
                "NAD_fold_increase"] for j in indexToShow}
    else:
        tempDict = {"Simulation "+str(j):timeCourses[j].iloc[-1][
                "NAD_fold_increase"] for j in indexCutoff}
    tempDict.update({"Experament":expNAD})
    S5df.append(tempDict)
S5df = pd.DataFrame(S5df)
S5df["NR"] = [0, 50, 100, 200, 500, 1000]
S5df = pd.melt(S5df, id_vars=['NR'], value_name="NAD (AU)", 
               var_name="   ")
S5df.rename(columns={"NR":"NR (\u03BCM)"}, inplace=True)
with sns.axes_style(style=myStyle):
    plt.figure()
    bp = sns.barplot(x="NR (\u03BCM)", y="NAD (AU)", hue="   ", 
                     data=S5df)
    bp.get_figure().savefig(os.path.join(fig_dir, "figS5.png"))

for i, diagram in zip(range(len(RS["diagrams"])),RS["diagrams"]):
    DS = diagram["DS"]
    if "Timepoint (hr)" in DS:
        values = []
        for j in diagram["IC"]:
            if isinstance(DS["Timepoint (hr)"],int):
                f = open(os.path.join(data_dir,
                                      'val-timeCourses'+str(j)+'.p'), 'rb')
                timeCourses = pickle.load(f)
                f.close()
                subValues = []
                if indexToShow is not None:
                    myPair = zip(indexToShow,
                                 [timeCourses[k] for k in indexToShow])
                else:
                    myPair = zip(indexCutoff,timeCourses)
                for k, timeCourse in myPair:
                    row = timeCourse[timeCourse["Time"]==
                                     DS["Timepoint (hr)"]].squeeze()
                    if isinstance(row[DS['Species']], (float, int)):
                        subValues.append(row[DS['Species']])
                    else:
                        subValues.append(float("NAN"))
                values.append(subValues)
            elif DS["Timepoint (hr)"] == "steady state":
                f = open(os.path.join(data_dir,
                                      'val-steadStates'+str(j)+'.p'), 'rb')
                SteadyStates = pickle.load(f)
                f.close()
                mySpecies = DS["Species"]
                if mySpecies == "AMPK-P":
                    mySpecies = "AMPK_P"
                if indexToShow is not None:
                    values.append([SteadyStates[k][mySpecies]
                                   for k in indexToShow])
                else:
                    values.append([SteadyStates[k][mySpecies]
                                   for k in indexCutoff])
        if len(diagram["DS"]["df"]) == len(pd.DataFrame(values)):
            df = pd.concat([diagram["DS"]["df"], pd.DataFrame(values)],
                            axis=1)
        ds = df[df['Fold-change Measurement']==1].squeeze()
        if isinstance(ds, pd.Series):
            if indexToShow is not None:
                for index in range(len(indexToShow)):
                    df[index] = df[index]/ds[index]
            else:
                for index in indexCutoff:
                    df[index] = df[index]/ds[index]
            df = df.rename(columns={'Fold-change Measurement':"Experiment"})
        else:
            ds = df.iloc[0]
            if indexToShow is not None:
                for index in range(len(indexToShow)):
                    df[index] = df[index]/ds[index]
            else:
                for index in indexCutoff:
                    df[index] = df[index]/ds[index]
            df["Extracted values"] = (df["Extracted values"]/
              ds["Extracted values"])
            df = df.rename(columns={'Extracted values':"Experiment"})
            #print(df["Experiment"])
        if lableToShow is not None:
            df = df.rename(columns={index:lab for index, lab
                                    in enumerate(lableToShow)})
            value_col = lableToShow
        else:
            df = df.rename(columns={index:"Simulation "+str(index)
                                    for index in indexCutoff})
            value_col = ["Simulation "+str(index) for index
                         in indexCutoff]
        value_col.append("Experiment")
        df = pd.melt(df, id_vars=['Treatment'], value_vars=value_col,
                     value_name=DS["Species"]+" (AU)", var_name="   ")
        #print(df)
        for i in range(len(df)):
            if isinstance(df.iloc[i, 2],pd.Series):
                df.iloc[i, 2] = None
        with sns.axes_style(style=myStyle):
            try:
                plt.figure()
                bp = sns.barplot(x="Treatment", 
                                 y=removeUnderScores(DS["Species"]+" (AU)"),
                                 hue="   ", data=removeUnderScores(df))
                bp.get_figure().savefig(os.path.join(fig_dir,
                             "fig"+diagram["name"]+'.png'))
            except:
                print("error creating :","fig"+diagram["name"]+'.png')
                print(df)                   
    else:
        f = open(os.path.join(data_dir,
                              'val-timeCourses'+str(diagram["IC"])+'.p'),
                 'rb')
        timeCourses = pickle.load(f)
        f.close()
        
        myDF=DS["df"].copy()
        myDF = myDF[["Timepoint (hr)",'Fold-change Measurement']]
        myDF.rename(columns={"Timepoint (hr)":"Time",
                             'Fold-change Measurement':DS[
                                     "df"]["Species"].iloc[0]},
                    inplace=True)
        
        showValues = showValsFunc(timeCourses,newParams)
        showValues = [i for i in showValues if i in myDF.columns]
        
        
        TCVis = timeCourseVisualiser([removeUnderScores(i) 
                                      for i in timeCourses])
        if indexToShow is None:
            thisShowIndex = list(indexCutoff)
        else:
            thisShowIndex = indexToShow 
        TCVis.multiPlot(indexSelect=thisShowIndex,
                        compLines=removeUnderScores(myDF),
                        varSelect=removeUnderScores(showValues),
                        style=myStyle,
                        save=os.path.join(fig_dir,"fig"+diagram["name"]+
                                          '.png'),
                        varAsAxis = True, xAxisLabel = "Time (hr)",
                        yAxisLabel = "(AU)", wrapNumber=1, figsize = (6, 5))
                        
DiaS19 = [i for i in RS["diagrams"] if i["name"]=="S19"][0]
f = open(os.path.join(data_dir, 'val-timeCourses'+str(DiaS19["IC"])+'.p'),
         'rb')
timeCourses = pickle.load(f)
f.close()
timeCourses = timeCourses[0][['Time',"NAD"]]
S19ExtraData = "SupplFig_19_Hsu_and_Burkholder (2016).xlsx"
S19ExtraData = os.path.join(working_dir,"oldModel","NAD_model_files",
                            "AMPK-NAD-PGC1a-SIRT1-manuscript",
                            "Raw_Literature_Data",S19ExtraData)
S19ExtraData = pd.read_excel(S19ExtraData, engine='openpyxl', skiprows=10) 
S19ExtraData.rename(columns={"BR"+i:"Biological Repeat "+i 
                             for i in ["1","2","3"]}, inplace=True)
S19ExtraData = S19ExtraData.melt(id_vars="Time (hr)", value_name='NAD (AU)', 
                                 ignore_index=True)
S19ExtraData = S19ExtraData[S19ExtraData["NAD (AU)"].isna()==False]
timeCourses.rename(columns={"Time":"Time (hr)", "NAD":'NAD (AU)'}, 
                            inplace=True)
timeCourses["variable"] = "Simulation"
timeCourses = pd.concat([timeCourses, S19ExtraData], ignore_index=True)
timeCourses.rename(columns={"variable":"   "}, inplace=True)
with sns.axes_style("ticks"):
    plt.figure()
    lp = sns.lineplot(data=timeCourses, x="Time (hr)", y="NAD (AU)", 
                 hue="   ")
    lp.get_figure().savefig(os.path.join(fig_dir,
                 "fig"+DiaS19["name"]+'-1.png'))
    
DiaS9 = [i for i in RS["diagrams"] if i["name"]=="S9"][0]
f = open(os.path.join(data_dir, 'val-timeCourses'+str(DiaS9["IC"])+'.p'),
         'rb')
timeCourses = pickle.load(f)
f.close()
timeCourses = timeCourses[0][['Time', 'AMPK-P']]
df = DiaS9["DS"]["df"][['Timepoint (hr)','Fold-change Measurement']]
timeCourses = timeCourses[timeCourses["Time"].isin([0.0,24.0])]
df.rename(columns={'Timepoint (hr)':"Protocol",
                   'Fold-change Measurement':"AMPK_P (AU)"}, inplace=True)
df["   "]="Experiment"
timeCourses.rename(columns={'Time':"Protocol", 'AMPK-P':"AMPK_P (AU)"}, 
                            inplace=True)
timeCourses["   "]="Simulation"
df = pd.concat([timeCourses, df], ignore_index=True)
df["Protocol"] = df["Protocol"].replace({0:"Non treated", 24:"AICAR"})
with sns.axes_style(style=myStyle):
    plt.figure()
    bp = sns.barplot(x="Protocol", y="AMPK-P (AU)", hue="   ", 
                     data=removeUnderScores(df))
    bp.get_figure().savefig(os.path.join(fig_dir, "figS9-1.png"))
    
"""

associatedDuration = list(RS["associatedDuration"].keys())

validationPath = os.path.join(working_dir, "oldModel",
                              "NAD_model_files",
                              "AMPK-NAD-PGC1a-SIRT1-manuscript",
                              "Raw_Literature_Data")

noPreProcessing = ['SupplFig_17_Ryu_et_al_2016.xlsx',
                   "SupplFig_21_Fakouri_et_al_2017.xlsx",
                   "SupplFig_23_Fang_et_al_2016.xlsx",
                   "SupplFig_24_Fang_et_al_2016.xlsx"]

dfList = []
for i in [0,1]:
    df = pd.read_excel(os.path.join(validationPath,associatedDuration[i]))
    df = df.rename(columns={"Time (hr)":"Time"})
    dfList.append(df)
for i in range(2,19): # 17
    if associatedDuration[i] in noPreProcessing:
        df = pd.read_excel(os.path.join(validationPath,
                                        associatedDuration[i]),header=None)
    else:
        df = pd.read_excel(os.path.join(validationPath,
                                        associatedDuration[i]))
        temp = pd.isna(df).all(axis=1)
        temp = temp[temp].index
        if (len(temp)>0):
            temp = min(temp)
            df = df[:temp]
        temp = pd.isna(df).all(axis=0)
        temp = temp[~temp].index
        df = df[temp]
        df = df.rename(columns={"Time (hr)":"Time"})
    dfList.append(df)
    
file = open(os.path.join(data_dir,
                         'val-timeCourses'+str(0)+'.p'),'rb')
timeCourses = pickle.load(file)
file.close()

dfList[0]=dfList[0].drop(columns="AMPK-P")
dfList[0] = dfList[0].rename(columns={"Fold change":"AMPK-P"})

TCVis = timeCourseVisualiser(timeCourses)
TCVis.multiPlot(indexSelect=list(indexCutoff),compLines=dfList[0],
                varSelect=["AMPK-P"],
                save=os.path.join(fig_dir,'SupplFig_6.png'))

dfList[1] = dfList[1].drop(columns="AMPK-P")
dfList[1] = dfList[1].rename(columns={"Fold change":"AMPK-P"})

TCVis.multiPlot(indexSelect=list(indexCutoff),compLines=dfList[1],
                varSelect=["AMPK-P"],
                save=os.path.join(fig_dir,'SupplFig_7.png'))

timePoint=RS["associatedDuration"]['SupplFig_8_Egawa_et_al_2014.xlsx']
myTable = []
temp = [0 for _ in indexCutoff]
for i in [3,2,1,0]:
    file = open(os.path.join(data_dir,
                         'val-timeCourses'+str(i)+'.p'),'rb')
    timeCourses = pickle.load(file)
    file.close()
    for index in indexCutoff:
        df = timeCourses[index][timeCourses[index]["Time"]==timePoint]
        df = df.squeeze()
        if df["AICAR"] == 0:
            temp[index] = df["AMPK-P"]
        myTable.append({"AMPK-P":df["AMPK-P"]/temp[index],
                        "AICAR":df["AICAR"]/2,
                        "catagory":("simulation "+str(index))})
df = pd.DataFrame(myTable)
dfList[2] = dfList[2].rename(columns={"Fold change":"AMPK-P",
      "AICAR Conc.":"AICAR"})
dfList[2]["catagory"]="experiment"
df = pd.concat([df, dfList[2]], join="inner")

plt.figure()
bp = sns.barplot(x="AICAR", y="AMPK-P", hue="catagory", data=df)
bp.get_figure().savefig(os.path.join(fig_dir,'SupplFig_8.png'))

timePoint=RS["associatedDuration"]['SupplFig_9_Hall_et_al_2018.xls']
myTable = []

temp = [0 for _ in indexCutoff]
for i in [3,1]:
    file = open(os.path.join(data_dir,
                         'val-timeCourses'+str(i)+'.p'),'rb')
    timeCourses = pickle.load(file)
    file.close()
    for index in indexCutoff:
        df = timeCourses[index][timeCourses[index]["Time"]==timePoint]
        df = df.squeeze()
        if df["AICAR"] == 0:
            temp[index] = df["AMPK-P"]
        myTable.append({"AMPK-P":df["AMPK-P"]/temp[index],
                        "AICAR":df["AICAR"]/2,
                        "catagory":("simulation "+str(index))})
temp = dfList[3][dfList[3]["Time"]==timePoint]["Fold change"]
df = pd.DataFrame([{"AMPK-P":1, "AICAR":0, "catagory":"experiment"},
                   {"AMPK-P":temp, "AICAR":0.5, "catagory":"experiment"}])
df = pd.concat([pd.DataFrame(myTable), df])

plt.figure()
bp = sns.barplot(x="AICAR", y="AMPK-P", hue="catagory", data=df)
bp.get_figure().savefig(os.path.join(fig_dir,'SupplFig_9.png'))

timePoint=RS["associatedDuration"]['SupplFig_10_Canto_et_al_2009.xlsx']
myTable = []

temp = [0 for _ in indexCutoff]
for i in [3,1]:
    file = open(os.path.join(data_dir,
                         'val-timeCourses'+str(i)+'.p'),'rb')
    timeCourses = pickle.load(file)
    file.close()
    for index in indexCutoff:
        df = timeCourses[index][timeCourses[index]["Time"]==timePoint]
        df = df.squeeze()
        if df["AICAR"] == 0:
            temp[index] = df["NAD"]
        myTable.append({"NAD":df["NAD"]/temp[index],
                        "AICAR":df["AICAR"]/2,
                        "catagory":("simulation "+str(index))})
temp = dfList[4][dfList[4]["Unnamed: 0"]=="AICAR"]["Normalised"]
df = pd.DataFrame([{"NAD":1, "AICAR":0, "catagory":"experiment"},
                   {"NAD":temp, "AICAR":0.5, "catagory":"experiment"}])
df = pd.concat([pd.DataFrame(myTable), df])

plt.figure()
bp = sns.barplot(x="AICAR", y="NAD", hue="catagory", data=df)
bp.get_figure().savefig(os.path.join(fig_dir,'SupplFig_10.png'))

timePoint=RS["associatedDuration"]['SupplFig_11_Fulco_et_al_2008.xlsx']
myTable = []

temp = [0 for _ in indexCutoff]
for i in [3,1]:
    file = open(os.path.join(data_dir,
                         'val-timeCourses'+str(i)+'.p'),'rb')
    timeCourses = pickle.load(file)
    file.close()
    for index in indexCutoff:
        df = timeCourses[index][timeCourses[index]["Time"]==timePoint]
        df = df.squeeze()
        if df["AICAR"] == 0:
            temp[index] = df["NAD"]
        myTable.append({"NAD":df["NAD"]/temp[index],
                        "AICAR":df["AICAR"]/2,
                        "catagory":("simulation "+str(index))})
temp = dfList[5][dfList[5]["Unnamed: 0"]=="AICAR"]["Normalised.1"]
df = pd.DataFrame([{"NAD":1, "AICAR":0, "catagory":"experiment"},
                   {"NAD":temp, "AICAR":0.5, "catagory":"experiment"}])
df = pd.concat([pd.DataFrame(myTable), df])

plt.figure()
bp = sns.barplot(x="AICAR", y="NAD", hue="catagory", data=df)
bp.get_figure().savefig(os.path.join(fig_dir,'SupplFig_11.png'))

timePoint=RS["associatedDuration"]['SupplFig_12_Canto_et_al_2009.xlsx']
myTable = []

temp = [0 for _ in indexCutoff]
for i in [3,1]:
    file = open(os.path.join(data_dir,
                         'val-timeCourses'+str(i)+'.p'),'rb')
    timeCourses = pickle.load(file)
    file.close()
    for index in indexCutoff:
        df = timeCourses[index][timeCourses[index]["Time"]==timePoint]
        df = df.squeeze()
        if df["AICAR"] == 0:
            temp[index] = df["PGC1a_deacet"]
        myTable.append({"PGC1a_deacet":df["PGC1a_deacet"]/temp[index],
                        "AICAR":df["AICAR"]/2,
                        "catagory":("simulation "+str(index))})
temp = dfList[6][dfList[6]["Unnamed: 0"]=="AICAR"]["Scaled"]
df = pd.DataFrame([{"PGC1a_deacet":1, "AICAR":0, "catagory":"experiment"},
                   {"PGC1a_deacet":temp, "AICAR":0.5, "catagory":"experiment"}])
df = pd.concat([pd.DataFrame(myTable), df])

plt.figure()
bp = sns.barplot(x="AICAR", y="PGC1a_deacet", hue="catagory", data=df)
bp.get_figure().savefig(os.path.join(fig_dir,'SupplFig_12.png'))

timePoint=RS["associatedDuration"]['SupplFig_13_Park_et_al_2012.xlsx']
myTable = []

temp2 = [0 for _ in indexCutoff]
for i in [4,5,7,6]:
    file = open(os.path.join(data_dir,
                         'val-timeCourses'+str(i)+'.p'),'rb')
    timeCourses = pickle.load(file)
    file.close()
    for index in indexCutoff:
        df = timeCourses[index][timeCourses[index]["Time"]==timePoint]
        df = df.squeeze()
        if (df["Glucose_source"]==5):
            temp = "LG"
        else:
            temp = "HG"
        if df["AICAR"]!=0:
            temp = temp + " + AICAR"
        if (df["AICAR"] == 0) and (df["Glucose_source"]==25):
            temp2[index] = df["AMPK-P"]
        myTable.append({"AMPK-P":df["AMPK-P"]/temp2[index],
                        "Condition":temp,
                        "catagory":("simulation "+str(index))})
    
dfList[7] = dfList[7].drop(columns="AMPK-P")
dfList[7] = dfList[7].rename(columns={"Fold change":"AMPK-P"})
dfList[7]["Condition"].replace({"Low Gluc No AICAR": "LG",
      "Low Gluc AICAR": "LG + AICAR",
      "High Gluc No AICAR": "HG",
      "High Gluc AICAR": "HG + AICAR"}, inplace=True)
dfList[7]["catagory"] = "experiment"
df = pd.concat([pd.DataFrame(myTable), dfList[7]])

plt.figure()
bp = sns.barplot(x="Condition", y="AMPK-P", hue="catagory", data=df)
bp.get_figure().savefig(os.path.join(fig_dir,'SupplFig_13.png'))

timePoint=RS["associatedDuration"]['SupplFig_14_Gerhart-Hines_et_al_2007.xlsx']
myTable = []

temp2 = [0 for _ in indexCutoff]
for i in [4,5]:
    file = open(os.path.join(data_dir,
                             'val-timeCourses'+str(i)+'.p'),'rb')
    timeCourses = pickle.load(file)
    file.close()
    for index in indexCutoff:
        df = timeCourses[index][timeCourses[index]["Time"]==timePoint]
        df = df.squeeze()
        if (df["Glucose_source"]==5):
            temp = "LG"
        else:
            temp = "HG"
        if (df["Glucose_source"]==25):
            temp2[index] = df["NAD"]
        myTable.append({"NAD":df["NAD"]/temp2[index],
                        "Condition":temp,
                        "catagory":("simulation "+str(index))})
    
dfList[8] = dfList[8].drop(columns="NAD")
dfList[8] = dfList[8].rename(columns={"Normalised":"NAD",
                                      "Unnamed: 0":"Condition"})
dfList[8]["catagory"] = "experiment"
df = pd.concat([pd.DataFrame(myTable), dfList[8]])

plt.figure()
bp = sns.barplot(x="Condition", y="NAD", hue="catagory", data=df)
bp.get_figure().savefig(os.path.join(fig_dir,'SupplFig_14.png'))

timePoint=RS["associatedDuration"]['SupplFig_15_Fulco_et_al_2008.xlsx']
myTable = []

temp2 = [0 for _ in indexCutoff]
for i in [4,5]:
    file = open(os.path.join(data_dir,
                             'val-timeCourses'+str(i)+'.p'),'rb')
    timeCourses = pickle.load(file)
    file.close()
    for index in indexCutoff:
        df = timeCourses[index][timeCourses[index]["Time"]==timePoint]
        df = df.squeeze()
        if (df["Glucose_source"]==5):
            temp = "LG"
        else:
            temp = "HG"
        if (df["Glucose_source"]==25):
            temp2[index] = df["NAD"]
        myTable.append({"NAD":df["NAD"]/temp2[index],
                        "Condition":temp,
                        "catagory":("simulation "+str(index))})
    
dfList[9] = dfList[9].drop(columns="NAD")
dfList[9] = dfList[9].rename(columns={"Normalised.1":"NAD",
                                      "Unnamed: 0":"Condition"})
dfList[9]["catagory"] = "experiment"
df = pd.concat([pd.DataFrame(myTable), dfList[9]])

plt.figure()
bp = sns.barplot(x="Condition", y="NAD", hue="catagory", data=df)
bp.get_figure().savefig(os.path.join(fig_dir,'SupplFig_15.png'))

timePoint=RS["associatedDuration"]['SupplFig_16_Canto_et_al_2012.xlsx']
myTable = []

temp2 = [0 for _ in indexCutoff]
for i in [3,8]:
    file = open(os.path.join(data_dir,
                             'val-timeCourses'+str(i)+'.p'),'rb')
    timeCourses = pickle.load(file)
    file.close()
    for index in indexCutoff:
        df = timeCourses[index][timeCourses[index]["Time"]==timePoint]
        df = df.squeeze()
        if (df["NR-NMN"]==0):
            temp = "Vehicle"
            temp2[index] = df["NAD"]
        else:
            temp = "NR"
        myTable.append({"NAD":df["NAD"]/temp2[index],
                        "Condition":temp,
                        "catagory":("simulation "+str(index))})
    
dfList[10] = dfList[10].rename(columns={"Mean":"NAD", "NAD+":"Condition"})
dfList[10]["catagory"] = "experiment"
dfList[10].ix[3,'Condition'] = "Na"
dfList[10]["NAD"]=dfList[10]["NAD"]/dfList[10].iloc[0]["NAD"]
df = pd.concat([pd.DataFrame(myTable), dfList[10]])

plt.figure()
bp = sns.barplot(x="Condition", y="NAD", hue="catagory", data=df)
bp.get_figure().savefig(os.path.join(fig_dir,'SupplFig_16.png'))

timePoint=RS["associatedDuration"]['SupplFig_17_Ryu_et_al_2016.xlsx']
myTable = []

temp2 = [0 for _ in indexCutoff]
for i in [3,9]:
    file = open(os.path.join(data_dir,
                             'val-timeCourses'+str(i)+'.p'),'rb')
    timeCourses = pickle.load(file)
    file.close()
    for index in indexCutoff:
        df = timeCourses[index][timeCourses[index]["Time"]==timePoint]
        df = df.squeeze()
        if (df["NR-NMN"]==0):
            temp = "Untreated"
            temp2[index] = df["NAD"]
        else:
            temp = "NR"
        myTable.append({"NAD":df["NAD"]/temp2[index],
                        "Condition":temp,
                        "catagory":("simulation "+str(index))})
    
df = pd.DataFrame([{"Condition":"Untreated", "NAD":1,
                    "catagory":"experament"},
                   {"Condition":"NR", "NAD":dfList[11].iloc[8,1],
                    "catagory":"experament"}])
df = pd.concat([pd.DataFrame(myTable), df])

plt.figure()
bp = sns.barplot(x="Condition", y="NAD", hue="catagory", data=df)
bp.get_figure().savefig(os.path.join(fig_dir,'SupplFig_17.png'))

timePoint=RS["associatedDuration"]['SupplFig_18_Fletcher_et_al_2017.xlsx']
myTable = []

temp2 = [0 for _ in indexCutoff]
for i in [3,8]:
    file = open(os.path.join(data_dir,
                             'val-timeCourses'+str(i)+'.p'),'rb')
    timeCourses = pickle.load(file)
    file.close()
    for index in indexCutoff:
        df = timeCourses[index][timeCourses[index]["Time"]==timePoint]
        df = df.squeeze()
        if (df["NR-NMN"]==0):
            temp = "Control"
            temp2[index] = df["NAD"]
        else:
            temp = "NR"
        myTable.append({"NAD":df["NAD"]/temp2[index],
                        "Condition":temp,
                        "catagory":("simulation "+str(index))})
    
dfList[12] = dfList[12].drop(columns="NAD")
dfList[12] = dfList[12].rename(columns={"Normalised":"NAD",
                                      "Unnamed: 0":"Condition"})
dfList[12]["catagory"] = "experiment"
df = pd.concat([pd.DataFrame(myTable), dfList[12]])

plt.figure()
bp = sns.barplot(x="Condition", y="NAD", hue="catagory", data=df)
bp.get_figure().savefig(os.path.join(fig_dir,'SupplFig_18.png'))

file = open(os.path.join(data_dir,
                         'val-timeCourses'+str(9)+'.p'),'rb')
timeCourses = pickle.load(file)
file.close()

for i in [1,2,3]:
    df = dfList[13].drop(dfList[13].index[0])
    df = df.rename(columns={"NAD+":"Time",
          "Unnamed: " +str(i):"NAD"})
    df["NAD"] = df["NAD"]/(dfList[13].iloc[1,4])
    
    TCVis = timeCourseVisualiser(timeCourses)
    TCVis.multiPlot(indexSelect=list(indexCutoff),compLines=df,
                    varSelect=["NAD"],
                    save=os.path.join(fig_dir,'SupplFig_19_'+str(i)+'.png'))

timePoint=RS["associatedDuration"]['SupplFig_20_Higashida_et_al_2013.xlsx']
myTable = []

temp2 = [0 for _ in indexCutoff]
for i in [3,11]:
    file = open(os.path.join(data_dir,
                             'val-timeCourses'+str(i)+'.p'),'rb')
    timeCourses = pickle.load(file)
    file.close()
    for index in indexCutoff:
        df = timeCourses[index][timeCourses[index]["Time"]==timePoint]
        df = df.squeeze()
        if (df["NR-NMN"]==0):
            temp = "Control"
            temp2[index] = df["AMPK-P"]
        else:
            temp = "NAM"
        myTable.append({"AMPK-P":df["AMPK-P"]/temp2[index],
                        "Condition":temp,
                        "catagory":("simulation "+str(index))})
    
dfList[14] = dfList[14].drop(columns="AMPK-P")
dfList[14] = dfList[14].rename(columns={"Normalised":"AMPK-P",
                                      "Unnamed: 0":"Condition"})
dfList[14]["catagory"] = "experiment"
df = pd.concat([pd.DataFrame(myTable), dfList[14]])

plt.figure()
bp = sns.barplot(x="Condition", y="AMPK-P", hue="catagory", data=df)
bp.get_figure().savefig(os.path.join(fig_dir,'SupplFig_20.png'))

timePoint=RS["associatedDuration"]['SupplFig_22_Higashida_et_al_2013.xlsx']
myTable = []

temp2 = [0 for _ in indexCutoff]
for i in [3,13]:
    file = open(os.path.join(data_dir,
                             'val-timeCourses'+str(i)+'.p'),'rb')
    timeCourses = pickle.load(file)
    file.close()
    for index in indexCutoff:
        df = timeCourses[index][timeCourses[index]["Time"]==timePoint]
        df = df.squeeze()
        if (df["SIRT1"]!=0):
            temp = "Control"
            temp2[index] = df["PGC1a_deacet"]
        else:
            temp = "SIRT1 inhib"
        myTable.append({"PGC1a_deacet":df["PGC1a_deacet"]/temp2[index],
                        "Condition":temp,
                        "catagory":("simulation "+str(index))})

dfList[16] = dfList[16].rename(columns={"PGC1a deacetylated":"PGC1a_deacet",
                                      "Unnamed: 0":"Condition"})
dfList[16]["catagory"] = "experiment"
df = pd.concat([pd.DataFrame(myTable), dfList[16]])

plt.figure()
bp = sns.barplot(x="Condition", y="PGC1a_deacet", hue="catagory", data=df)
bp.get_figure().savefig(os.path.join(fig_dir,'SupplFig_22.png'))

timePoint=RS["associatedDuration"]['SupplFig_23_Fang_et_al_2016.xlsx']
myTable = []

temp2 = [0 for _ in indexCutoff]
for i in [3,8,14,15]:
    file = open(os.path.join(data_dir,
                             'val-timeCourses'+str(i)+'.p'),'rb')
    timeCourses = pickle.load(file)
    file.close()
    for index in indexCutoff:
        df = timeCourses[index][timeCourses[index]["Time"]==timePoint]
        df = df.squeeze()
        if (df["NR-NMN"]==0 and df["PARP1"]<=1):
            temp2[index] = df["NAD"]
        if (df["PARP1"]<=1):
            temp = "WT"
        else:
            temp = "ATM-KD"
        if df["NR-NMN"]!=0:
            temp = temp + " + NR"
        myTable.append({"NAD":df["NAD"]/temp2[index],
                        "Condition":temp,
                        "catagory":("simulation "+str(index))})

df = pd.DataFrame(data={'Condition': ["WT", "WT + NR", "ATM-KD",
                                      "ATM-KD + NR"],
                        'NAD':dfList[17].iloc[[1,2,6,7],1]})
df["catagory"] = "experiment"
df = pd.concat([pd.DataFrame(myTable), df])

plt.figure()
bp = sns.barplot(x="Condition", y="NAD", hue="catagory", data=df)
bp.get_figure().savefig(os.path.join(fig_dir,'SupplFig_23.png'))

timePoint=RS["associatedDuration"]['SupplFig_24_Fang_et_al_2016.xlsx']
myTable = []

temp2 = [0 for _ in indexCutoff]
for i in [3,7,13,14]:
    file = open(os.path.join(data_dir,
                             'val-timeCourses'+str(i)+'.p'),'rb')
    timeCourses = pickle.load(file)
    file.close()
    for index in indexCutoff:
        df = timeCourses[index][timeCourses[index]["Time"]==timePoint]
        df = df.squeeze()
        if (df["NR-NMN"]==0 and df["PARP1"]<=1):
            temp2[index] = df["PGC1a_deacet"]
        if (df["PARP1"]<=1):
            temp = "WT"
        else:
            temp = "ATM-KD"
        if df["NR-NMN"]!=0:
            temp = temp + " + NR"
        myTable.append({"PGC1a_deacet":df["PGC1a_deacet"]/temp2[index],
                        "Condition":temp,
                        "catagory":("simulation "+str(index))})

df = pd.DataFrame(data={'Condition': ["WT", "WT + NR", "ATM-KD",
                                      "ATM-KD + NR"],
                        "PGC1a_deacet":dfList[18].iloc[[1,2,6,7],1]})
df["catagory"] = "experiment"
df = pd.concat([pd.DataFrame(myTable), df])

plt.figure()
bp = sns.barplot(x="Condition", y="PGC1a_deacet", hue="catagory", data=df)
bp.get_figure().savefig(os.path.join(fig_dir,'SupplFig_23.png'))
"""
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
    name = "reConf4"

working_dir = os.path.abspath('')

fig_dir = os.path.join(working_dir,'figures',name)
if not os.path.isdir(fig_dir):
    os.makedirs(fig_dir)

data_dir = os.path.join(working_dir,'data', name)

file = open(os.path.join(data_dir,'runSwitches.p'),'rb')
RS = pickle.load(file)
file.close()
 
f = open(os.path.join(data_dir,'new-params.p'), "rb" )
newParams = pickle.load(f)
f.close()

f = open(os.path.join(data_dir,'new-timeCourses.p'), "rb" )
timeCourses = pickle.load(f)
f.close()

PEVis = parameterEstimationVisualiser(newParams)

PEVis.waterFall(save=os.path.join(fig_dir,'waterfall.png'),
                indexNames="parameters")

RSScutoff = min(GFID(newParams)["RSS"].iloc[9],
                RSSClusterEstimation(GFID(newParams))[0]["maxRSS"])
indexCutoff = range(min(10,
                        RSSClusterEstimation(GFID(newParams))[0]["size"]))


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
    
    TCVis = timeCourseVisualiser(timeCourses)
    TCVis.multiPlot(indexSelect=list(indexCutoff),compLines=myDF,
                    varSelect=showValues,
                    save=os.path.join(fig_dir,'timeCourseCal'+
                                      str(i)+'.png'))

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

""" # I don't understand how figgures were extracted from the data file
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
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 13:23:17 2020

@author: peter
"""

import os, pickle
import pandas as pd
from reportlab.lib.units import mm, inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Frame, SimpleDocTemplate, Table
from reportlab.platypus import Image, TableStyle
from reportlab.pdfgen import canvas

working_directory = os.path.dirname(os.path.abspath(__file__))

name = "report2c"
calAlvaro = ["Figure_S"+str(i)+".png" for i in range(1,24+1)]
supAlPath = os.path.join(working_directory, "oldModel", "NAD_model_files",
                         "AMPK-NAD-PGC1a-SIRT1-manuscript", "Figures",
                         "Supplementary")
calNew = ["timeCourseCal1.png",
          "timeCourseCal0.png",
          "timeCourseCal3.png",
          "timeCourseCal2.png"]
newRefs = ["Egawa et al. (2014)",
           "Canto et al. (2009)",
           "Canto et al. (2010)",
           "Bai et al. (2011)"]
calNew = calNew + ["figS"+str(i)+".png" for i in range(5,24+1)]
newA = "reConf7"
newB = "reConf7S7"

data_dirA = os.path.join(working_directory,'figures', newA)
data_dirB = os.path.join(working_directory,'figures', newB)

file = open(os.path.join(working_directory,"data",newA,'runSwitches.p'),'rb')
RSA = pickle.load(file)
file.close()

file = open(os.path.join(working_directory,"data",newB,'runSwitches.p'),'rb')
RSB = pickle.load(file)
file.close()

styleSheet = getSampleStyleSheet()
style = styleSheet['BodyText']

styleN = styleSheet['Normal']
styleH = styleSheet['Heading1']
story = []

PW = 10*inch
PH = 5.63*inch

def probeIC(ID,RS):
    for dia in RS['diagrams']:
        if dia["name"]==ID:
            if isinstance(dia["IC"],list):
                df = pd.DataFrame([RS["ICTrack"][i] for i in dia["IC"]]).T
                df = [[str(i)]+[str(j) for _,j in r.items()] for i, r
                       in df.iterrows()]
            else:
                df = pd.DataFrame([RS["ICTrack"][dia["IC"]]])
                df = [list(df.columns),[str(i) for _,i
                      in df.squeeze().items()]]
            return Table(df)
    if int(ID[1:])<5:
        ID2 = int(calNew[int(ID[1:])-1][13])
        df = [list(RS["indep_cond"][ID2].keys()),
              [str(val) for _,val in RS["indep_cond"][ID2].items()]]
        return Table(df)
    return ""

def probeConditions(ID,RS):
    for dia in RS['diagrams']:
        if dia["name"]==ID:
            tabList = [["fig:",ID]]
            if 'Timepoint (hr)' in dia["DS"]:
                tabList.append(["time:",dia["DS"]['Timepoint (hr)']])
            if 'Species' in dia["DS"]:
                tabList.append(["Species:",dia["DS"]['Species']])
            if 'Reference' in dia["DS"]:
                tabList.append(["Reference:",dia["DS"]['Reference']])
            return Table(tabList)
    if int(ID[1:])<5:
        ID2 = int(calNew[int(ID[1:])-1][13])
        tabList = [["fig:",ID]]
        df = RS["calDf"][ID2]
        tabList.append(["time:",str(df["Time"].iloc[-1])])
        tabList.append(["Species:",
                        ", ".join([i for i in df.columns if i!="Time"])])
        tabList.append(["Reference:",newRefs[ID2]])
        return Table(tabList)
    return Table([["fig:",ID]])

styles = getSampleStyleSheet()
"""
tempPar = Paragraph("test text", style = styles["Normal"])
story.append(tempPar)
"""

tempIm = Image(os.path.join(working_directory,"Tital Card.png"))
tempIm._restrictSize(PW-2.2*inch, PH-2.2*inch)
story.append(tempIm)

tempIm = Image(os.path.join(working_directory,"motivation.png"))
tempIm._restrictSize(PW-2.2*inch, PH-2.2*inch)
story.append(tempIm)

tempIm = Image(os.path.join(working_directory,"newModelHandAn.jpg"))
tempIm._restrictSize(PW-2.2*inch, PH-2.2*inch)
story.append(tempIm)

tempIm = Image(os.path.join(working_directory,"workflow.png"))
tempIm._restrictSize(PW-2.2*inch, PH-2.2*inch)
story.append(tempIm)

for i, imNameAl, imNameNew in zip(range(1,len(calAlvaro)+1),calAlvaro,
                                  calNew):
    IA = Image(os.path.join(data_dirA,imNameNew))
    IA._restrictSize((PW-2.1*inch)/3, PH-2.1*inch)
    IB = Image(os.path.join(data_dirB,imNameNew))
    IB._restrictSize((PW-2.1*inch)/3, PH-2.1*inch)
    IO = Image(os.path.join(supAlPath,imNameAl))
    IO._restrictSize((PW-2.1*inch)/3, PH-2.1*inch)
    myTable = Table([[IO,IA,IB],
                     [probeConditions("S"+str(i),RSA),
                      probeIC("S"+str(i),RSA),
                      probeIC("S"+str(i),RSB)]],spaceAfter=inch*0.1)
    myTable.setStyle(TableStyle([('INNERGRID', (0,0), (-1,-1), 0.25,
                                  colors.black),
                                 ('BOX', (0,0), (-1,-1), 0.25,
                                  colors.black)]))
    if i>5:
        tempPar = Paragraph("validation figure: "+imNameAl,
                            style = styles["Normal"])
    else:
        tempPar = Paragraph("calibration figure: "+imNameAl,
                            style = styles["Normal"])
    story.append(tempPar)
    story.append(myTable)

tempIm = Image(os.path.join(working_directory,"newModelHandMito.jpg"))
tempIm._restrictSize(PW-2.2*inch, PH-2.2*inch)
story.append(tempIm)

doc = SimpleDocTemplate(name+".pdf",pagesize = (PW,PH))
doc.build(story)
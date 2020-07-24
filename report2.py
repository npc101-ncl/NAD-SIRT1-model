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

name = "report3"
supAlPath = os.path.join(working_directory, "oldModel", "NAD_model_files",
                         "AMPK-NAD-PGC1a-SIRT1-manuscript", "Figures")

newA = "reConf6"
newB = "reConf6S7"

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


styles = getSampleStyleSheet()

IAC = Image(os.path.join(data_dirA,"fig3Cont.png"))
IAC._restrictSize((PW-2.1*inch)/3, (PH-2.1*inch)/2)
IAGi = Image(os.path.join(data_dirA,"fig3GI.png"))
IAGi._restrictSize((PW-2.1*inch)/3, (PH-2.1*inch)/2)

IBC = Image(os.path.join(data_dirB,"fig3Cont.png"))
IBC._restrictSize((PW-2.1*inch)/3, (PH-2.1*inch)/2)
IBGi = Image(os.path.join(data_dirB,"fig3GI.png"))
IBGi._restrictSize((PW-2.1*inch)/3, (PH-2.1*inch)/2)

IO = Image(os.path.join(supAlPath,"Figure_3.jpg"))
IO._restrictSize((PW-2.1*inch)/3, (PH-2.3*inch))

myTable = Table([[IO,[IAC,IAGi],[IBC,IBGi]]],spaceAfter=inch*0.1)
myTable.setStyle(TableStyle([('INNERGRID', (0,0), (-1,-1), 0.25,
                              colors.black),
                             ('BOX', (0,0), (-1,-1), 0.25,
                              colors.black)]))
fig3par = Paragraph("fig 3:", style = styles["Normal"])
story.append(fig3par)
story.append(myTable)

IANAD = Image(os.path.join(data_dirA,"fig4NAD.png"))
IANAD._restrictSize((PW-2.1*inch)/3, (PH-2.3*inch)/2)
IAPGC = Image(os.path.join(data_dirA,"fig4PGC1a_d.png"))
IAPGC._restrictSize((PW-2.1*inch)/3, (PH-2.3*inch)/2)

IBNAD = Image(os.path.join(data_dirB,"fig4NAD.png"))
IBNAD._restrictSize((PW-2.1*inch)/3, (PH-2.3*inch)/2)
IBPGC = Image(os.path.join(data_dirB,"fig4PGC1a_d.png"))
IBPGC._restrictSize((PW-2.1*inch)/3, (PH-2.3*inch)/2)

IO = Image(os.path.join(supAlPath,"Temporal_Figure_4.jpg"))
IO._restrictSize((PW-2.1*inch)/3, PH-2.3*inch)

myTable = Table([[IO,[IANAD,IAPGC],[IBNAD,IBPGC]]],spaceAfter=inch*0.1)
myTable.setStyle(TableStyle([('INNERGRID', (0,0), (-1,-1), 0.25,
                              colors.black),
                             ('BOX', (0,0), (-1,-1), 0.25,
                              colors.black)]))
fig4par = Paragraph("fig 4:", style = styles["Normal"])
story.append(fig4par)
story.append(myTable)

#####

IAC = Image(os.path.join(data_dirA,"figAlphaCont.png"))
IAC._restrictSize((PW-2.3*inch)/2, (PH-2.3*inch)/2)
IANS = Image(os.path.join(data_dirA,"figAlphaNoSirt.png"))
IANS._restrictSize((PW-2.3*inch)/2, (PH-2.3*inch)/2)

IBC = Image(os.path.join(data_dirB,"figAlphaCont.png"))
IBC._restrictSize((PW-2.3*inch)/2, (PH-2.3*inch)/2)
IBNS = Image(os.path.join(data_dirB,"figAlphaNoSirt.png"))
IBNS._restrictSize((PW-2.3*inch)/2, (PH-2.3*inch)/2)

myTable = Table([[[IAC,IANS],[IBC,IBNS]]],spaceAfter=inch*0.1)
myTable.setStyle(TableStyle([('INNERGRID', (0,0), (-1,-1), 0.25,
                              colors.black),
                             ('BOX', (0,0), (-1,-1), 0.25,
                              colors.black)]))
figApar = Paragraph("fig alpha:", style = styles["Normal"])
story.append(figApar)
story.append(myTable)

doc = SimpleDocTemplate(name+".pdf",pagesize = (PW,PH))
doc.build(story)
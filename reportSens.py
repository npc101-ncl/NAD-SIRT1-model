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

name = "reportSensB"

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


styles = getSampleStyleSheet()

IA = Image(os.path.join(data_dirA,"waterfall.png"))
IA._restrictSize((PW-2.1*inch)/2, (PH-2.1*inch))

IB = Image(os.path.join(data_dirB,"waterfall.png"))
IB._restrictSize((PW-2.1*inch)/2, (PH-2.1*inch))

myTable = Table([[IA,IB]],spaceAfter=inch*0.1)
myTable.setStyle(TableStyle([('INNERGRID', (0,0), (-1,-1), 0.25,
                              colors.black),
                             ('BOX', (0,0), (-1,-1), 0.25,
                              colors.black)]))
story.append(myTable)

i=0
while True:
    fName = "RSSSensitivity"+str(i)+".png"
    fileA = os.path.join(data_dirA,fName)
    fileB = os.path.join(data_dirB,fName)
    if not (os.path.isfile(fileA) and os.path.isfile(fileB)):
        break
    IA = Image(fileA)
    IA._restrictSize((PW-2.1*inch)/2, (PH-2.1*inch))

    IB = Image(fileB)
    IB._restrictSize((PW-2.1*inch)/2, (PH-2.1*inch))

    myTable = Table([[IA,IB]],spaceAfter=inch*0.1)
    myTable.setStyle(TableStyle([('INNERGRID', (0,0), (-1,-1), 0.25,
                                  colors.black),
                                 ('BOX', (0,0), (-1,-1), 0.25,
                                  colors.black)]))
    story.append(myTable)
    i = i+1

doc = SimpleDocTemplate(name+".pdf",pagesize = (PW,PH))
doc.build(story)
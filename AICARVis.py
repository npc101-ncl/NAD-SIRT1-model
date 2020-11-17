#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 17:25:14 2020

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

name = "reConf7"

working_directory = os.path.dirname(os.path.abspath(__file__))
fig_dir = os.path.join(working_directory,"figures",name)

myTCs = loadPick(["data",name,"aicarTimeCourses.p"],
                 relative=True)

showValues = myTCs[0].columns
showValues = [col for col in showValues if (not col.endswith("_k1"))
              and (not col.endswith("_h")) and (not col.endswith("_Shalve"))
              and (not col.endswith("_V")) and (not col.endswith("_v"))
              and (col!="quantity to number factor")]

maxes = getTCSelectionMaxes(myTCs,varSelection=showValues)

maxes = breakSeriesByScale(maxes,maxRunLength=25)

TCVis = timeCourseVisualiser(myTCs)

for i in range(len(maxes)):
    TCVis.multiPlot(varSelect=maxes[i],
                    save=os.path.join(fig_dir,'aicarTimeCourse'+str(i)+'.png'))
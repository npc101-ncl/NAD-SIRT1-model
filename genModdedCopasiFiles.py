#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 17:05:16 2020

@author: peter
"""

from python.pycotoolsHelpers import *
from python.visualisationTools import *
import os, re
import pandas as pd
import pickle

name = "reConf3"

working_dir = os.path.abspath('')
run_dir = os.path.join(working_dir,'copasiRuns', 'reference')

data_dir = os.path.join(working_dir,'data', name)

f = open(os.path.join(data_dir,'new-params.p'), "rb" )
newParams = pickle.load(f)
f.close()

addCopasiPath("/Applications/copasi")
    
antFile = open(os.path.join(working_dir,"modAntFile2.txt"), "r")
antimony_string = antFile.read()
antFile.close()
    
myModel = modelRunner(antimony_string, run_dir)

for i in range(10):
    myModel.genRefCopasiFile(filePath=os.path.join(data_dir,
                                                   'reference'+str(i)+'.cps'),
                             adjustParams=GFID(newParams),
                             setIndex=i)

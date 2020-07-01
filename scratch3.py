#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 17:28:11 2020

@author: peter
"""

import site, os, re
from python.pycotoolsHelpers import *

mySuperComputer=False
if not mySuperComputer:
    addCopasiPath("/Applications/copasi")
    
    
working_directory = os.path.dirname(os.path.abspath(__file__))
mPath = os.path.join(working_directory, "oldModel", "NAD_model_files",
                     "AMPK-NAD-PGC1a-SIRT1-model",
                     "Model_Version6_Integrated_Mitochondria.cps")

myModel = modelRunner(CopasiFile = mPath)

antFile = open(os.path.join(working_directory,"antMitoRefFile.txt"), "w")
antFile.write(myModel.antString)
antFile.close()
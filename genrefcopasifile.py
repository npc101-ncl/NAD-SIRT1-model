#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 14:34:53 2020

@author: peter
"""

import os
from python.pycotoolsHelpers import *

working_directory = os.path.dirname(os.path.abspath(__file__))
run_dir = os.path.join(working_directory,'copasiRuns', 'reference')
if not os.path.isdir(run_dir):
    os.makedirs(run_dir)
    
addCopasiPath("/Applications/copasi")
    
antFile = open(os.path.join(working_directory,"modAntFile.txt"), "r")
antimony_string = antFile.read()
antFile.close()
    
myModel = modelRunner(antimony_string, run_dir)

myModel.genRefCopasiFile(filePath=os.path.join(working_directory,'reference.cps'))

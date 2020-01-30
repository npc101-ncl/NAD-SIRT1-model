#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 16:04:37 2020

@author: peter
"""

from pycotools3 import model
import re, os

copasiPath = "/Applications/copasi"
if not re.search(copasiPath, os.environ["PATH"]):
    os.environ["PATH"] += os.pathsep + copasiPath
    
working_directory = os.path.dirname(os.path.abspath(__file__))

f = open(os.path.join(working_directory,'antFile.txt'), "r" )
oldAntStr = f.read()
f.close()

copasi_filename = os.path.join(working_directory,'temp.cps')

model = model.loada(oldAntStr, copasi_filename)

kineticNames = model.get_variable_names(which='gl',
                                        include_assignments=False)
metaboliteNames = model.get_variable_names(which='m',
                                           include_assignments=False)

model.parameters[kineticNames].to_csv(
        path_or_buf=os.path.join(working_directory,"oldKVals.csv"))


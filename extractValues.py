#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 16:04:37 2020

@author: peter
"""

from pycotools3.model import Model
import re, os

copasiPath = "/Applications/copasi"
if not re.search(copasiPath, os.environ["PATH"]):
    os.environ["PATH"] += os.pathsep + copasiPath
    
working_directory = os.path.dirname(os.path.abspath(__file__))
mPath = os.path.join(working_directory, "oldModel", "NAD_model_files",
                     "AMPK-NAD-PGC1a-SIRT1-model",
                     "Model_Version_6_VALIDATED_12.03.2019.cps")

model = Model(mPath)

kineticNames = model.get_variable_names(which='gl',
                                        include_assignments=False)
metaboliteNames = model.get_variable_names(which='m',
                                           include_assignments=False)

model.parameters[kineticNames].to_csv(
        path_or_buf=os.path.join(working_directory,"oldKVals.csv"))


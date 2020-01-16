#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 22:04:35 2020

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

antFile = open(os.path.join(working_directory,"antFile.txt"), "w")
antFile.write(model.to_antimony())
antFile.close()

[i.name for i in model.reactions]
[{"n":i.name, "e":i.expression} for i in model.reactions]

[i for i in model.reactions if i.name=="NAD increase by AMPK"]

# first data set indep for PARP1=0, (NAD negative regulation).k1=0,
# (NAD increase by AMPK).V=0

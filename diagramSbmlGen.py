#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 15:57:48 2020

@author: peter
"""

from pycotools3 import model
import re, os

copasiPath = "/Applications/copasi"
if not re.search(copasiPath, os.environ["PATH"]):
    os.environ["PATH"] += os.pathsep + copasiPath
    
working_directory = os.path.dirname(os.path.abspath(__file__))
mPath = os.path.join(working_directory, "oldModel", "NAD_model_files",
                     "AMPK-NAD-PGC1a-SIRT1-model",
                     "Model_Version_6_VALIDATED_12.03.2019.cps")
oPath = os.path.join(working_directory,"oldModelProto.xml")
nPath = os.path.join(working_directory,"newModelProto.xml")

def antLineReactionReducer(line):
    expresion = "=>"
    parts = line.split(expresion)
    if len(parts)!=2:
        expresion = "->"
        parts = line.split(expresion)
        if len(parts)!=2:
            return line
    LParts = parts[0].split(":")
    LEParts = LParts[-1].split("+")
    LEParts = [part.strip() for part in LEParts]
    RParts = parts[1].split(";")
    REParts = RParts[0].split("+")
    REParts = [part.strip() for part in REParts]
    WLeft=LEParts
    LEParts=[]
    while len(WLeft)>0:
        TLeft = WLeft.pop()
        for i in range(len(REParts)):
            if TLeft==REParts[i]:
                REParts.pop(i)
                break
        else:
            LEParts.append(TLeft)
    LParts[-1] = "+".join(LEParts)
    RParts[0] = "+".join(REParts)
    parts[0] = ":".join(LParts)
    parts[1] = ";".join(RParts)
    return expresion.join(parts)

def antStringToDiagramSBML(antString,filePath,tempPath):
    myAntList = oldAntStr.splitlines()
    myAntList = [antLineReactionReducer(line) for line in myAntList]
    newAntStr = "\n".join(myAntList)
    newModel = model.loada(newAntStr, tempPath)
    newModel.to_sbml(sbml_file=filePath)

oldModel = Model(mPath)   

oldAntStr = oldModel.to_antimony()

tPath = os.path.join(working_directory,"tempCOPASI.cps")

antStringToDiagramSBML(oldAntStr,oPath,tPath)

f = open(os.path.join(working_directory,"modAntFile.txt"),"r")
newAntStr = f.read()
f.close()

antStringToDiagramSBML(newAntStr,nPath,tPath)
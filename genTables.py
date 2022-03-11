#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 13:41:38 2021

@author: peter
"""

from python.pycotoolsHelpers import *
from python.utilityTools import *
from python.visualisationTools import *
import re
import pandas as pd
from sympy.parsing.sympy_parser import parse_expr
from sympy.printing.mathml import mathml
from sympy import latex

def rateLawToMathml(rateLaw, doLatex = False):
    myMML = rateLaw.replace("^","**")
    tokens = []
    i = 0
    for M in re.finditer(r'[a-zA-Z_]\w*', myMML):
        token = str(i)
        for j, l in enumerate(["A","B","C","D","E","F","G","H","I","J"]):
            token = token.replace(str(j),l)
        i = i+1
        token = "T"+token+"T"
        tokens.append({"o":M.group(0), "T":token, "s":M.start(),
                       "e":M.end()})
    for token in reversed(tokens):
        myMML = myMML[:token["s"]] + token["T"] + myMML[token["e"]:]
    savecopy = myMML
    if doLatex:
        myMML = latex(parse_expr(myMML))
        tokens = {T["T"]:"\\mathrm{"+T["o"].replace("_","\\_")+"}" 
                  for T in tokens}
    else:
        myMML = mathml(parse_expr(myMML),printer='presentation')
        tokens = {T["T"]:T["o"] for T in tokens}
    pattern = re.compile("|".join(tokens.keys()))
    myMML = pattern.sub(lambda m: tokens[m.group(0)], myMML)
    return myMML

cmdDict, cmdFlags = getCmdLineArgs()

if "name" in cmdDict.keys():
    name = cmdDict["name"]
else:
    name = "reConf12"
nameS = "reConf12R2"
if nameS is None:
    nameS = name
    
doLatex = True
    
paramCase = 1
    
mySuperComputer = "slurm" in cmdFlags

# add path to copasiSE to path varaiable if not on rocket clustor
if not mySuperComputer:
    addCopasiPath("/Applications/copasi")

RS = loadPick(['data', nameS, 'runSwitches.p'],relative=True)

newParams = loadPick(['data', nameS, 'new-params.p'],relative=True)

runDir = resolvePath(["copasiRuns",nameS+"-tableOut"], relative=True)

modelsFunc = getModelsAndFunctions(RS["mitoAntStr"])

myReaction = {myMod['name']:extractAntReactions(myMod['text']) for myMod
              in modelsFunc["models"]}

myReaction = (myReaction["Mitonuclear_communication_model"]+
              myReaction["full_reaction"])


for i in range(len(myReaction)):
    myReaction[i]['formula'] = (
            subFunIntoReact(myReaction[i], modelsFunc['functions']))
    myReaction[i]['formula'] = (
            myReaction[i]['formula'].replace("compartment_*",""))
    myReaction[i]['formula'] = (
            rateLawToMathml(myReaction[i]['formula'],doLatex=doLatex))
    if doLatex:
        myReaction[i]['symbol'] = (
                "V_{"+str(i+1)+"}")
    else:
        myReaction[i]['symbol'] = (
                "<msub><mi>V</mi><mn>"+str(i+1)+"</mn></msub>")
    
ODEs = {}

for i, R in enumerate(myReaction):
    for LHT in R["LHS"]:
        if LHT["fixed"]:
            continue
        if not LHT["var"] in ODEs:
            ODEs[LHT["var"]] = {}
            ODEs[LHT["var"]]["term"] = []
        ODEs[LHT["var"]]["term"].append({"s":"-", "n":R["symbol"]})
    for RHT in R["RHS"]:
        if RHT["fixed"]:
            continue
        if not RHT["var"] in ODEs:
            ODEs[RHT["var"]] = {}
            ODEs[RHT["var"]]["term"] = []
        ODEs[RHT["var"]]["term"].append({"s":"+", "n":R["symbol"]})
for k in ODEs.keys():
    expresion = ""
    for i, term in enumerate(ODEs[k]["term"]):
        if term["s"]=="-":
            if doLatex:
                expresion += "-"
            else:
                expresion += "<mo>-</mo>"
        elif i==0:
            pass
        else:
            if doLatex:
                expresion += "+"
            else:
                expresion += "<mo>+</mo>"
        expresion += term["n"]
    if not doLatex:
        expresion = "<mrow>"+expresion+"</mrow>"
    ODEs[k]["expresion"] = expresion
    if doLatex:
        ODEs[k]["symbol"] = ("\\frac{d\\mathrm{"+k.replace("_","\\_")+
            "}}{dt}")
    else:
        ODEs[k]["symbol"] = ("<mfrac><mrow><mi>d</mi><mi>"+k+
            "</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac>")
    

myMod = modelRunner(antString=RS["mitoAntStr"], run_dir=runDir)

myE = myMod.getModelEliments()

myP = myMod.extractModelParam()

myPSet = GFID(newParams).iloc[paramCase]
for k, v in myPSet.items():
    if k in myP:
        myP[k] = v

params = []

i = 1
for p in myE["kineticParams"]:
    if doLatex:
        symb = ("k_{"+str(i)+"}")
    else:
        symb = ("<msub><mi>k</mi><mn>"+str(i)+"</mn></msub>")
    if not p in myP:
        continue
    isInR = False
    if doLatex:
        searchTerm = r"\s*\\mathrm{"+p.replace("_","\\\\_")+"}\s*"
    else:
        searchTerm = r"<mi>\s*"+p+"\s*</mi>"
    for j, R in enumerate(myReaction):
        temp = R['formula']
        myReaction[j]['formula'] = (
                re.sub(searchTerm, symb, R['formula']))
        if temp != myReaction[j]['formula']:
            isInR = True
    if not isInR:
        continue
    i = i+1
    vString = str(myP[p])
    if p in myPSet.index:
        vString = "<i>"+vString+"</i>"
    params.append({"symbol":symb, "value":vString, "name":p})

reactionTable = ""
for R in myReaction:
    if doLatex:
        row = ("<td>"+R['symbol']+"</td>\n<td>"+
               R['formula']+"</td>")
    else:
        row = ("<td><math>"+R['symbol']+"</math></td>\n<td><math>"+
               R['formula']+"</math></td>")
    reactionTable += "<tr>\n"+row+"\n</tr>\n"
reactionTable = "<table>\n" + reactionTable + "</table>"

ODETable = ""
for k, v in ODEs.items():
    if doLatex:
        row = ("<td>"+v['symbol']+"</td>\n<td>"+
               v['expresion']+"</td>")
    else:
        row = ("<td><math>"+v['symbol']+"</math></td>\n<td><math>"+
               v['expresion']+"</math></td>")
    ODETable += "<tr>\n"+row+"\n</tr>\n"
ODETable = "<table>\n" + ODETable + "</table>"

ParamTable = ""
for p in params:
    if doLatex:
        row = ("<td>"+p['symbol']+"</td>\n<td>"+
               p['value']+"</td>")
    else:
        row = ("<td><math>"+p['symbol']+"</math></td>\n<td>"+
               p['value']+"</td>")
    ParamTable += "<tr>\n"+row+"\n</tr>\n"
ParamTable = "<table>\n" + ParamTable + "</table>"

htmlTables = ("<!DOCTYPE html>\n<html>\n<body>\n"+reactionTable+"\n"+
              ODETable+"\n"+ParamTable+"\n</body>\n</html>")
if doLatex:
    outPath = resolvePath(["myTablesLatex.html"],relative=True)
else:
    outPath = resolvePath(["myTables.html"],relative=True)
file = open(outPath, 'w')
file.write(htmlTables)
file.close()
    
myIC = pd.Series({i:myP[i] for i in myE['metabolites']})
myIC.to_csv("ICTable.csv")
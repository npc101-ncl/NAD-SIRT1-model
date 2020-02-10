#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 12:50:50 2020

@author: peter
"""


import site, os, re
import pandas as pd
from python.pycotoolsHelpers import *
import pickle
import time

working_directory = os.path.dirname(os.path.abspath(__file__))
run_dir = os.path.join(working_directory,'copasiRuns', 'reparam')
if not os.path.isdir(run_dir):
    os.makedirs(run_dir)

Fakouri_file = os.path.join(working_directory,"oldModel","NAD_model_files",
                       "AMPK-NAD-PGC1a-SIRT1-manuscript",
                       "Raw_Literature_Data",
                       "SupplFig_21_Fakouri_et_al_2017.xlsx")


Fakouri_data = [pd.read_excel(Fakouri_file,sheet_name='Hoja1',skiprows=4*n,
                              usecols=[1,2],nrows=2) for n in range(6)]
Fakouri_data = {list(i.columns)[0]:i["Fold change"].iloc[1] for
                i in Fakouri_data}

mySuperComputer=False
if not mySuperComputer:
    addCopasiPath("/Applications/copasi")
    
antFile = open(os.path.join(working_directory,"modAntFileS.txt"), "r")
antimony_string = antFile.read()
antFile.close()

if __name__ == "__main__":
    
    myModel = modelRunner(antimony_string, run_dir)
    
    tempParams = myModel.extractModelParam()
    Fakouri_data["AMPK total"] = (tempParams["AMPK_P"]+
                 tempParams["AMPK"])*Fakouri_data["AMPK total"]
    Fakouri_data["AMPK ratio"] = (Fakouri_data["AMPK-P"]*
                tempParams["AMPK_P"]/(tempParams["AMPK"]+
                          tempParams["AMPK_P"]))
    Fakouri_data["AMPK_P"] = (Fakouri_data["AMPK ratio"]*
                Fakouri_data["AMPK total"])
    Fakouri_data["AMPK"] = (Fakouri_data["AMPK total"] - 
                Fakouri_data["AMPK-P"])
    Fakouri_data["SIRT1"] = tempParams["SIRT1"]*Fakouri_data["SIRT1"]
    Fakouri_data["PGC1a_deacet"] = (tempParams["PGC1a_deacet"]*
                Fakouri_data["PGC1a"])
    Fakouri_data["PGC1a_P"] = (tempParams["PGC1a_P"]*
                Fakouri_data["PGC1a"])
    Fakouri_data["PGC1a"] = (tempParams["PGC1a"]*
                Fakouri_data["PGC1a"])
    Fakouri_data["PARP"] = (tempParams["PARP"]*
                Fakouri_data["PARP1"])
    Fakouri_data["NAD"] = (tempParams["NAD"]*
                Fakouri_data["NAD"])
    Fakouri_data.pop("AMPK total", None) 
    Fakouri_data.pop("AMPK ratio", None)
    Fakouri_data.pop("PARP1", None)
    Fakouri_data.pop("AMPK-P", None)
    
    print(myModel.runSteadyStateFinder(params=Fakouri_data))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 10:37:19 2020

@author: peter
"""

import os
import pandas as pd
import sys
import seaborn as sns
import matplotlib.pyplot as plt

cmdLineArg = sys.argv[1:]

name = [name[5:] for name in cmdLineArg if (name.startswith("name:") and 
        len(name)>5)]
if len(name)>0:
    name = name[0]
else:
    name = "reConf7S7"

working_directory = os.path.dirname(os.path.abspath(__file__))

data_dir = os.path.join(working_directory,'data', name)
fig_dir = os.path.join(working_directory,'figures', name)

df = pd.read_csv(os.path.join(data_dir,"sensativity2.csv")) 

myVars = set(df["variable"])

for theVar in myVars:
    if len(df[(df["variable"] == theVar) &
              (df['paramiter change%'] == 0)]) == 0:
        df = df.append({'RSS change%':0, 'variable':theVar,
                        'paramiter change%':0}, ignore_index=True)
df = df.sort_values(by=['variable', 'index', 'paramiter change%'])
df["variable"] = [i.replace('DUMMY_REACTION_','') for i
                  in list(df["variable"])]
varNames = list(set(df["variable"]))
chunkSize = 9
varNames = [varNames[(chunkSize*i):(chunkSize*(i+1))] for i
            in range((len(varNames)-1)//chunkSize +1)]
chunks = [df[df["variable"].isin(i)] for i in varNames]

for i, chunk in zip(range(len(chunks)),chunks):
    grid = sns.FacetGrid(chunk, col="variable", col_wrap=3)
    grid.map(sns.lineplot, "paramiter change%",
             "RSS change%", "index").set_titles("{col_name}")
    grid.savefig(os.path.join(fig_dir,"RSSSensitivity"+str(i)+".png"))

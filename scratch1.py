#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 16:06:40 2020

@author: peter
"""

import tellurium as te

antString = """
model simple_parameter_estimation()
    compartment Cell = 1;

    A in Cell;
    B in Cell;
    
    R1: A => B ; Cell * A;
    R2: B => A ; Cell * B;
    
    A = 2;
    B = 0;
    
end
"""

r = te.loada(antString)
outValues = r.getFloatingSpeciesIds()
r["A"] = 0
r["B"] = 2
pState = {key:r[key] for key in outValues}
r.conservedMoietyAnalysis = True
r.setSteadyStateSolver('nleq1')
r.steadyState()
rState = {key:r[key] for key in outValues}
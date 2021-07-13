#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 13:04:32 2021

@author: peter
"""

from python.pycotoolsHelpers import *
from python.utilityTools import *
import re

cmdDict, cmdFlags = getCmdLineArgs()

if "name" in cmdDict.keys():
    name = cmdDict["name"]
else:
    name = "reConf12"
    
mySuperComputer = "slurm" in cmdFlags
    
# add path to copasiSE to path varaiable if not on rocket clustor
if not mySuperComputer:
    addCopasiPath("/Applications/copasi")

RS = loadPick(['data', name, 'runSwitches.p'],relative=True)

antAddition = """
    MR1: Mito_new -> Mito_old; Mitochondrial_dysfunction_k1*Mito_new*Damage
    MR2:  -> AICAR_treatment; Hill_Cooperativity(Mito_old, Mitochondrial_stress_signal_Shalve, Mitochondrial_stress_signal_V, Mitochondrial_stress_signal_h)
    MR3: Mito_turnover -> Mito_new; Mitogenesis_k1*Mito_turnover
    MR4: Mito_new -> Mito_turnover; Mitophagy_of_new_mitochondria_k1*Mitophagy*Mito_new
    MR5: Mito_old -> Mito_turnover; Mitophagy_of_old_mitochondria_k1*Mitophagy*Mito_old
    MR6: Mitophagy -> ; Dummy_Reaction_Mitophagy_Removal_k1*Mitophagy
    MR7: AICAR_treatment -> ; Dummy_Reaction_Mitochondrial_Stress_Signal_Removal_k1*AICAR_treatment
    MR8: -> Mitophagy ; Delay_Reaction_Mitophagy_k1*PGC1a_deacet
    MR9: -> 2 Damage; Damage_propagation_k1*Mito_old
    
    Mitochondrial_dysfunction_k1 = 0.0003608;
    Mitochondrial_stress_signal_Shalve = 2;
    Mitochondrial_stress_signal_V = 0.1;
    Mitochondrial_stress_signal_h = 20;
    Delay_Reaction_Mitophagy_k1 = 0.1;
    Mitophagy_of_new_mitochondria_k1 = 1;
    Mitophagy_of_old_mitochondria_k1 = 0.0055;
    Dummy_Reaction_Mitophagy_Removal_k1 = 0.1;
    Dummy_Reaction_Mitochondrial_Stress_Signal_Removal_k1 = 0.1;
    Damage_propagation_k1 = 1e-6;
    Mitogenesis_k1 = 100.0;
    Mito_new = 100;
    Mito_old = 0;
    Damage = 0.00251883;
"""

# must force $PARP to PARP
expansion = """
    sTime = 0.0;
    relTime := piecewise(time-sTime, time>sTime, 0.0)
    
    bleedRateAMPK        = 0.0;
    explosionRatePARP    = 0.0;
    bleedRateSIRT        = 0.0;
    explosionRateGlucose = 0.0;
    
    GlucoseE: -> Glucose ; explosionRateGlucose*relTime*Glucose_utilisation_k1*Glucose
    AMPKB1: AMPK ->      ; bleedRateAMPK*relTime
    AMPKB2: AMPK_P ->    ; bleedRateAMPK*relTime
    PARPE:  -> PARP      ; exp(explosionRatePARP*relTime)-1
    SIRTB:  SIRT1 ->     ; exp(bleedRateSIRT*relTime)-1
    
    at (AMPK<=0): AMPK=0.0, bleedRateAMPK=0.0;
    at (AMPK_P<=0): AMPK_P=0.0, bleedRateAMPK=0.0;
    at (SIRT1<=0): SIRT1=0.0, bleedRateSIRT=0.0;
"""

expansion2 = """
    bleedRateAMPK        = 0.0;
    # 10^-6
    explosionRatePARP    = 0.0;
    # 3*10^-6
    bleedRateSIRT        = 0.0;
    # 10^-6
    explosionRateGlucose = 0.0;
    # 7
    
    GlucoseE: -> Glucose ; explosionRateGlucose*Damage
    AMPKB1: AMPK ->      ; bleedRateAMPK*AMPK*AMPK_P*Damage
    AMPKB2: AMPK_P ->    ; bleedRateAMPK*AMPK*AMPK_P*Damage
    PARPE:  -> PARP      ; explosionRatePARP*Damage
    SIRTB:  SIRT1 ->     ; bleedRateSIRT*SIRT1*Damage
"""

antDosing = """

    clockPeriod = 24;
    myDose      = 0;
    myClock := sin(2*pi*time/clockPeriod);
    at (myClock>0): NR_NMN=NR_NMN+myDose;
"""

if False:
    antAddition = antAddition+antDosing
elif True:
    antAddition = antAddition+expansion2

antStrBD = getModelsAndFunctions(RS["antimony_string"])

antStr = [i["text"].splitlines() for i in antStrBD["models"]]
for i in range(len(antStr)):
    antStr[i][0]=antStr[i][0].replace("*","")
    antStr[i] = "\n".join(antStr[i])
antStr = "\n".join(antStr)
antStr = [i for i in antStr.splitlines()
          if not bool(re.match(r".*\bis\b.*", i))]
antStr = "\n".join(antStr)
antStr = ("\n".join([i["text"] for i in antStrBD["functions"]]) + 
          "\n" + antStr)
myMod = modelRunner(antString=antStr,
                    run_dir=resolvePath(["copasiRuns","test"],
                                        relative=True))
myE = myMod.getModelEliments()
antStr = (antStr + "\nmodel full_reaction\n"+
          #"\n".join(["\tvar "+myVar for myVar in myE["metabolites"]])+"\n"+
          ["\tA: "+i["name"]+"();" for i in antStrBD["models"]][0]+"\n"+
          "\n".join(["\tA."+i+" is "+i+";" for i in myE["metabolites"]])+"\n"+
          "\n".join(["\tA."+i+" is "+i+";" for i in myE["kineticParams"]])+"\n"+
          "\n".join(["\tA."+i+" is "+i+";" for i in myE["assignments"]])+"\n"+
          antAddition+
          "end\n")

antStr = antStr.replace("$PARP", "PARP")
antStr = antStr.replace("NR_NMN in compartment_",
                        "$NR_NMN in compartment_")

myMod = modelRunner(antString=antStr,
                    run_dir=resolvePath(["copasiRuns","test"],
                                        relative=True))
myE = myMod.getModelEliments()

RS = loadPick(['data', name, 'runSwitches.p'],relative=True)
RS["mitoAntStr"] = antStr
savePick(['data', name, 'runSwitches.p'],RS,relative=True)
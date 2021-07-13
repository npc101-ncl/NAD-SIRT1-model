#!/bin/bash
# Example SLURM job script for serial (non-parallel) jobs
#
#
# Tell SLURM if you want to be emailed when your job starts, ends, etc.
# Currently mail can only be sent to addresses @ncl.ac.uk
#
#SBATCH --mail-type=ALL
#SBATCH --mail-user=peter.clark@ncl.ac.uk
#

python reparamerteriser.py name:reConf12b ant:modAntFile8.txt runs:200 reconnect ICReview powerLaw slurm meth:particle_swarm_ridiculous removeHardCoded2 forceParam:Induced_PGC1a_deacetylation_k1,AMPK_phosphorylation_induced_by_AICAR_k1,Glucose_induced_AMPK_dephosphorylation_k1 reuse:DUMMY_REACTION_Delay_AICAR_stimulus_V
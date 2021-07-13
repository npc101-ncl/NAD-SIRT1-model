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

python reparamerteriser.py name:reConf10b ant:modAntFile6.txt runs:200 reconnect ICReview slurm meth:particle_swarm_ridiculous removeHardCoded2 forceParam:Induced_PGC1a_deacetylation_k1,AMPK_phosphorylation_induced_by_AICAR_k1,Glucose_induced_AMPK_dephosphorylation_k1 reuse:NR_NMN_supplementation_V,DUMMY_REACTION_Delay_AICAR_stimulus_Shalve,NAD_negative_regulation_k1,NAD_utilisation_by_PARP_k1,Glucose_DUMMY_REACTION_delay_limiter_k1,DUMMY_REACTION_Delay_AICAR_stimulus_V,Glucose_DUMMY_REACTION_delay_Shalve,NAD_synthesis_v
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

python reparamerteriser.py name:reConf7 ant:modAntFile3C.txt runs:200 reconnect ICReview slurm meth:particle_swarm_ridiculous removeHardCoded2 reuse:NAD_synthesis_v,NAD_utilisation_by_PARP_k1,DUMMY_REACTION_AICAR_stimulus_removal_k1,Glucose_DUMMY_REACTION_delay_Shalve,NR_NMN_supplementation_V
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

python reparamerteriser.py name:reConf8 ant:modAntFile4.txt runs:200 reconnect ICReview slurm meth:particle_swarm_ridiculous removeHardCoded2 reuse:DUMMY_REACTION_AICAR_stimulus_removal_k1,NR_NMN_supplementation_V,DUMMY_REACTION_Delay_in_NAD_Increase_2_k1,NAD_increase_by_AMPK_V
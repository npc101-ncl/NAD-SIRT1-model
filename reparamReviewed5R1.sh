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

python reparamerteriser.py name:reConf8 ant:modAntFile4.txt runs:200 reconnect ICReview slurm meth:particle_swarm_ridiculous removeHardCoded2 reuse:NAD_synthesis_v,NAD_utilisation_by_PARP_k1,NR_NMN_supplementation_V
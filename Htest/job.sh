#!/bin/sh
#SBATCH -J 10atomPH
#SBATCH -p skx-dev      # Queue (partition) name
#SBATCH -N 1               # Total # of nodes 
#SBATCH -n 8              # Total # of mpi tasks
#SBATCH -t 02:00:00        # Run time (hh:mm:ss)
#SBATCH --mail-user=tw2619@columbia.edu
#SBATCH --mail-type=all    # Send email at begin and end of job
#SBATCH -A TG-DMR180081 # Allocation name (req'd if you have more than 1)
 
 
date
python3 run_qe.py
wait
date
 
# End of script

#!/bin/sh
#SBATCH -p skx-dev      # Queue (partition) name
#SBATCH -N 2               # Total # of nodes 
#SBATCH -n 8              # Total # of mpi tasks
#SBATCH -t 02:00:00        # Run time (hh:mm:ss)
#SBATCH --mail-user=tw2619@columbia.edu
#SBATCH --mail-type=all    # Send email at begin and end of job
#SBATCH -A TG-DMR180081 # Allocation name (req'd if you have more than 1)


 

for i in 0 5 10 15 20 25 30 35 40 45 50 55; do
cd vc$i
ibrun pw.x -in vc$i.in > vc$i.out &
sleep 3
cd ..
done
wait

#!/bin/sh
#SBATCH -p skx-dev      # Queue (partition) name
#SBATCH -N 1               # Total # of nodes 
#SBATCH -n 4              # Total # of mpi tasks
#SBATCH -t 02:00:00        # Run time (hh:mm:ss)
#SBATCH --mail-user=tw2619@columbia.edu
#SBATCH --mail-type=all    # Send email at begin and end of job
#SBATCH -A TG-DMR180081 # Allocation name (req'd if you have more than 1)
 

for i in 0 3 6 9 12 15 18 21 24 27 30 33 ; do
cd scfkpoint
ibrun pw.x -in ${i}kpscf.in > $i.out &
sleep 3
cd ..
done
wait

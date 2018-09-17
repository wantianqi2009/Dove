#!/bin/sh
#SBATCH -p skx-dev      # Queue (partition) name
#SBATCH -N 1               # Total # of nodes 
#SBATCH -n 2              # Total # of mpi tasks
#SBATCH -t 02:00:00        # Run time (hh:mm:ss)
#SBATCH --mail-user=jw3588@columbia.edu
#SBATCH --mail-type=all    # Send email at begin and end of job
#SBATCH -A TG-DMR180081 # Allocation name (req'd if you have more than 1)
 

for i in 30 40 50 60 70 80 90 100 110 120 130 140 ; do
cd scfecut
ibrun pw.x -in ${i}ecutscf.in > $i.out &
sleep 3
cd ..
done
wait

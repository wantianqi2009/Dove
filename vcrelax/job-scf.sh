#!/bin/sh
#SBATCH -J 10atomPH
#SBATCH -p skx-dev      # Queue (partition) name
#SBATCH -N 2               # Total # of nodes 
#SBATCH -n 16              # Total # of mpi tasks
#SBATCH -t 02:00:00        # Run time (hh:mm:ss)
#SBATCH --mail-user=tw2619@columbia.edu
#SBATCH --mail-type=all    # Send email at begin and end of job
#SBATCH -A TG-DMR180081 # Allocation name (req'd if you have more than 1)
 
#date
#for i in 0 5 10 15 20 25 30 35 40 45 50 55 ; do
#cd scf$i
#ibrun pw.x -in scf$i.in > scf$i.out &
#sleep 3
#cd ..
#done
#wait

date
for i in 30 35 40 45 50 55; do
cd scf$i
ibrun ph.x -in scf${i}ph.in > scf${i}-ph.out &
sleep 3
cd ..
done
wait
date

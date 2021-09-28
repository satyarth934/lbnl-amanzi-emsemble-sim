# !/bin/bash

path=/global/scratch/zexuanxu/lbnl-amanzi-emsemble-sim/simulation_runs
for n in {0..15}; do
  cd ${path}/sim${n}
  rm -f run_amanzi.sh
  cp ../shared_files/run_amanzi.sh run_sim${n}.sh
  sbatch run_sim${n}.sh

done

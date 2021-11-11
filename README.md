# lbnl-amanzi-emsemble-sim

Code to generate input files for amanzi simulation.

It is recommended but not necessary to set up a virtual environment to run the code.
Use the following command to set up the environment.
> `conda env create -f requirement.yml`

## How to use the code?
There are two ways to run the code.
1. **Option 1:** Specify the code parameters in a configuration file.
   > `python generate_input_files.py @generate_input_files.cfg`
2. **Option 2:** Specify the code parameters in the command line.
   > `python generate_input_files.py --input_template /path/to/template.tpl --variable_mapping /path/to/variable_maps.yml --num_simulations 16 --output_dir /path/to/output_dir`

A combination of the two can be used as well where some parameters are specified in the configuration file and others are specified in the command line.

## What are the different files?
1. `generate_input_files.cfg`
   > Configuration parameters for running the code.
2. `templates/farea_3d_tritium.tpl`
   > Template file
3. `variable_maps/sim_param_mapping.yml`
   > Mapping of the variables with their corresponding value ranges
4. `requirements.yml`
   > File used to create the virtual environment.

---
## Ensemble Simulation
[`run_ensembles.sh`](run_ensembles.sh) script is used to initiate the ensemble simulation.
This script requires two commandline inputs:
1. Output Directory (`-o`)
   > This directory contains all the individual simulation directories. The output of each simulation is stored in the respective directories.
3. Number of simulations (`-n`)
   > This is the number of simulation runs. This number should match the count of simulation directories.

### REQUIREMENT:
> This script requires a `shared_files` directory within the Output Directory.
This `shared_files` directory must contain the following files:
1. `run_amanzi.sh`
   > This file is replicated for each simulation and the replicated version is stored in the simulation directory.
   > The `sbatch` configurations are specified in this file.
   > Number of processors is also specified in this file.
2. `farea_3D_barriers.exo`
3. `farea_tritium.bdg`

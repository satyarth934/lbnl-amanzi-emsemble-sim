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

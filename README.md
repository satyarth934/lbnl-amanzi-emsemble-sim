# lbnl-amanzi-emsemble-sim

Code to generate input files for amanzi simulation.

## How to use the code?
There are two ways to run the code.

*Option 1:* Specify the code parameters in a configuration file.
> `python generate_input_files.py @generate_input_files.cfg`

*Option 2:* Specify the code parameters in the command line.
> `python generate_input_files.py --input_template /path/to/template.tpl --variable_mapping /path/to/variable_maps.yml --num_simulations 16 --output_dir /path/to/output_dir`

A combination of the two can be used as well where some parameters are specified in the configuration file and others are specified in the command line.

## What are the different files?
> `generate_input_files.cfg`
> 
> Configuration parameters for running the code.

> `templates/farea_3d_tritium.tpl`
> 
> Template file


> `variable_maps/sim_param_mapping.yml`
> 
> Mapping of the variables with their corresponding value ranges


> `requirements.yml`
> 
> File used to create the virtual environment.
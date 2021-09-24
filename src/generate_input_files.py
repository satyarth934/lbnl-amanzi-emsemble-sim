import os

# import sys
# from os import replace
import yaml
import argparse
import numpy as np
from pprint import pprint
from joblib import Parallel, delayed

parallel_function = Parallel(n_jobs=-1, verbose=5)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Main function to generate simulation input files.",
        fromfile_prefix_chars="@",  # helps read the arguments from a file.
    )

    parser.add_argument(
        "--input_template",
        type=str,
        default=None,
        help="Path to the input template that contains all the simulation parameters.",
    )

    parser.add_argument(
        "--variable_mapping_file",
        type=str,
        default=None,
        help="Mapping of different varible keys to its value ranges.",
    )

    parser.add_argument(
        "--num_simulations",
        type=int,
        default=16,
        help="The number of desired simulation runs. This is same as the number if input files generated.",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default=None,
        help="The output directory where the generated files are stored.",
    )

    args, unknown = parser.parse_known_args()

    # print("--- args ---")
    # print(args)

    return args


def generate_random_input_params(template_str, var_maps, output_dir, template_filename):
    tpl_str = template_str

    # for a single input file:
    for k in var_maps:
        # rand_val = np.random.uniform(var_maps[k]["low"], var_maps[k]["high"])
        tpl_str = tpl_str.replace(k, str(var_maps[k]))
        print(f"updating {k} to {var_maps[k]}...")

    output_filepath = os.path.join(
        output_dir,
        f"sim{var_maps['@@serial_number@@']}",
        os.path.basename(template_filename).replace(".tpl", ".xml"),
    )
    try:
        os.makedirs(os.path.dirname(output_filepath))
    except Exception as e:
        print("Simulation directory already exists.")

    with open(output_filepath, "w") as f_out:
        f_out.writelines(tpl_str)

    # print("--- Generated Input String ---")
    # print(inp_str)


def parse_variable_mapping(mapping_file):
    var_map_ranges = yaml.load(open(mapping_file, "r"))
    for k in var_map_ranges:
        for k_k in var_map_ranges[k]:
            temp = var_map_ranges[k][k_k].split("*")
            if len(temp) == 2:
                var_map_ranges[k][k_k] = float(temp[0]) * float(temp[1])
            elif len(temp) == 1:
                var_map_ranges[k][k_k] = float(temp[0])

    return var_map_ranges


def main():
    # Parse commandline arguments
    args = parse_arguments()
    for k in args.__dict__:
        print(f"{k} => {args.__dict__[k]}")

    # template data
    with open(args.input_template, "r") as tpl_f:
        tpl_str = "".join(tpl_f.readlines())
    print("--- Template String ---")
    print(tpl_str)

    # Parsing yaml file for variable maps
    var_map_ranges = parse_variable_mapping(mapping_file=args.variable_mapping_file)
    pprint(var_map_ranges, width=3)

    # Generating all the variable mappings within the ranges
    var_map_list = list()
    for i in range(args.num_simulations):
        var_map_i = {"@@serial_number@@": i}
        for k in var_map_ranges:
            rand_val = np.random.uniform(
                var_map_ranges[k]["low"], var_map_ranges[k]["high"]
            )
            var_map_i[k] = rand_val

        var_map_list.append(var_map_i)
    print(var_map_list)

    # Replacing values in the template file with the mappings - SAMPLE - SINGLE FILE
    generate_random_input_params(
        template_str=tpl_str,
        var_maps=var_map_list[0],
        output_dir=args.output_dir,
        template_filename=args.input_template,
    )

    # Replacing values in the template file with the mappings - PARALLEL for all files
    parallel_function(
        delayed(generate_random_input_params)(
            template_str=tpl_str,
            var_maps=var_map_i,
            output_dir=args.output_dir,
            template_filename=args.input_template,
        )
        for var_map_i in var_map_list
    )


if __name__ == "__main__":
    main()

from jinja2 import Environment, FileSystemLoader
import os
import yaml
import argparse
from utils.treeparser import treeparser

basepath = os.path.dirname(__file__)
project_root = os.path.dirname(basepath)
output_path = os.path.join(project_root, "output")


def main(flat: bool = None, output_name: str = "config"):
    if not output_name:
        output_name = "config"
    env = Environment(
        loader=FileSystemLoader(
            os.path.abspath(os.path.join(project_root, "templates"))
        ),
        trim_blocks=False,
    )

    values_env = Environment(
        loader=FileSystemLoader(
            os.path.abspath(os.path.join(project_root, "values"))
        ),
        trim_blocks=True,
    )

    # Mount the values YAML
    values_template = values_env.get_template(r"master.jinja2")
    values = values_template.render()
    master_value = yaml.safe_load(values)

    # Mount the Config File
    template = env.get_template(r"master.jinja2")
    output = template.render(master_value)

    # Write the Config File to disk
    with open(os.path.join(output_path, f"{output_name}.sros"), "w") as fout:
        fout.writelines(output)

    if flat:
        file_input = os.path.abspath(
            os.path.join(output_path, f"{output_name}.sros")
        )
        file_output = os.path.abspath(
            os.path.join(output_path, f"{output_name}_flat.sros")
        )
        treeparser(file_input, file_output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--flatConfig",
        action="store_true",
        help="Convert final configuration file in flat script",
    )
    parser.add_argument(
        "-o",
        "--outputName",
        type=str,
        help="Specify the name of the file that will be output. Example: SROS01",
    )

    args = parser.parse_args()

    main(flat=args.flatConfig, output_name=args.outputName)

from jinja2 import Environment, FileSystemLoader
import os
from tempfile import TemporaryFile
import yaml

basepath = os.path.dirname(__file__)
project_root = os.path.dirname(basepath)

env = Environment(
    loader=FileSystemLoader(os.path.abspath(
        os.path.join(project_root, 'templates'))
        ),
    trim_blocks=False
)

values_env = Environment(
    loader=FileSystemLoader(os.path.abspath(
        os.path.join(project_root, 'values'))
        ),
    trim_blocks=True
)

# Mount the values YAML
values_template = values_env.get_template(r'master.jinja2')
values = values_template.render()
master_value = yaml.safe_load(values)


# Mount the Config File
template = env.get_template(r'master.jinja2')
output = template.render(master_value)

# Write the Config File to disk
with open(os.path.join(project_root, 'test.sros'), 'w') as fout:
    fout.writelines(output)

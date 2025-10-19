import yaml
from jinja2 import Environment, FileSystemLoader

# Load the YAML file
with open('messageDesc.yaml', 'r') as yaml_file:
    data = yaml.safe_load(yaml_file)

# Prepare the Jinja2 environment and load the template
env = Environment(loader=FileSystemLoader('.'), trim_blocks=True, lstrip_blocks=True)


template = env.get_template('messageClassInclude_tmpl.jinja2')

# Render the template with data from the YAML file
output = template.render(message=data['Message'])

# Save the rendered output to a file
with open(f'{data["Message"]["name"]}.h', 'w') as cpp_file:
    cpp_file.write(output)


template = env.get_template('messageClassImpl_tmpl.jinja2')

# Render the template with data from the YAML file
output = template.render(message=data['Message'])

# Save the rendered output to a file
with open(f'{data["Message"]["name"]}.cpp', 'w') as cpp_file:
    cpp_file.write(output)

print("C++ class generated successfully.")
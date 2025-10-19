from jinja2 import Environment, FileSystemLoader

# loading the environment
env = Environment(loader = FileSystemLoader('templates'))

# loading the template
template = env.get_template('helloName.jinja')

# rendering the template and storing the resultant text in variable output
output = template.render(name = 'Geeks')

# printing the output on screen
print(output)
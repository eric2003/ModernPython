from jinja2 import Environment, FileSystemLoader
env = Environment(loader = FileSystemLoader('templates'))
template = env.get_template('helloWorld.jinja')
output = template.render()
print(output)
with open("renders/outputFileName.txt", 'w') as f:
    print(output, file = f)
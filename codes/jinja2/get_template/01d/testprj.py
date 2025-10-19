from jinja2 import Environment, FileSystemLoader

env = Environment(loader = FileSystemLoader('templates'))

template = env.get_template('webTable.jinja')

with open("renders/output.html", 'w') as f:
    print(template.render(tableOf = 5), file = f)
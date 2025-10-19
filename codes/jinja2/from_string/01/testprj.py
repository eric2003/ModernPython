from jinja2 import Environment

env = Environment()  

template = env.from_string("Hello {{ name }}")

rendered = template.render(name="World")

print(rendered)
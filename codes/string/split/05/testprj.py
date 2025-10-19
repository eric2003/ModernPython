import re

text = "Python;is,a powerful::language"
words = re.split(';|,|:| |is', text)
new_list = [item for item in words if item]
print(words)
print(new_list)
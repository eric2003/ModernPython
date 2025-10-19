import re

text = "Python;is,a powerful::language"
words = re.split(';|,|:| ', text)
new_list = [item for item in words if item]
print(words)
print(new_list)
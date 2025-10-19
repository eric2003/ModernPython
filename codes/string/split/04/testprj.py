import re

text = "Python;is,a powerful:language"
words = re.split(';|,| ', text)
print(words)
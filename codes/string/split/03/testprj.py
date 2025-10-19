string = "GeeksForGeeks, | is an-awesome! website"
delimiters = [",", "|", ";", "!"]
 
for delimiter in delimiters:
    string = " ".join(string.split(delimiter))
 
result = string.split()
 
print(result)
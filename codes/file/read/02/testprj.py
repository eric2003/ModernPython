       
file = open('example.txt', 'r')
lines = file.readlines()

for index, line in enumerate(lines):
    print("Line {}: {}".format(index, line.strip()))
    
file.close()       
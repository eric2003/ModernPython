with open('example.txt', 'r') as f:
    for index, line in enumerate(f):
        print("Line {}: {}".format(index, line.strip()))
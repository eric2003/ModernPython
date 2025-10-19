with open('sod_theory.plt', 'r') as f:
    for index, line in enumerate(f):
        #print("Line {}: {}".format(index, line.strip()))
        words = line.strip().split()
        print(words)
        print('len(words)=',len(words))
        print(words[0])
        

filename = "output.txt"
fp = open(filename, 'w', encoding='UTF-8')
s = "Hello"
t = "world"
fp.writelines(s)
fp.writelines(t)
 
    



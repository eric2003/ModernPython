
str1 = "ab<cd>ef"

ist = str1.find('<')
ied = str1.find('>')
print("ist={}, ied={}".format(ist, ied))

str2 = str1[ist+1:ied]
print("str2={}".format(str2))


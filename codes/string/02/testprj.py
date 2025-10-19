
str1 = "abcd"

ist = str1.find('a')
ied = str1.find('b')
print("ist={}, ied={}".format(ist, ied))

str2 = str1[ist:ied]
print("str2={}".format(str2))

ist1 = str1.find('a')
ied1 = str1.find('c')

print("ist1={}, ied1={}".format(ist1, ied1))
str3 = str1[ist1:ied1]
print("str3={}".format(str3))


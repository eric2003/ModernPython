
str1 = "-  [【Python科学计算三维可视化】北京理工大学](https://www.bilibili.com/video/BV1F7411i74Q/)."

print("str1={}".format(str1))

ist = str1.find('[')
ied = str1.find(']')
print("ist={}, ied={}".format(ist, ied))

str2 = str1[ist+1:ied]
print("str2={}".format(str2))

ist1 = str1.find('(')
ied1 = str1.find(')')

print("ist1={}, ied1={}".format(ist1, ied1))

str3 = str1[ist1+1:ied1]
print("str3={}".format(str3))




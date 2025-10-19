def getsubstr( str, s, t ):
   ist = str.find(s)
   ied = str.find(t)

   return str[ist+1:ied]
   
str = "-  [【Python科学计算三维可视化】北京理工大学](https://www.bilibili.com/video/BV1F7411i74Q/)."   
str1 = getsubstr( str, '[', ']' )
str2 = getsubstr( str, '(', ')' )
print("str1={}".format(str1))
print("str2={}".format(str2))



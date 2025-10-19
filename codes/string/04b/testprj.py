def getsubstr( str, s, t ):
    ist = str.find(s)
    ied = str.find(t)

    return str[ist+1:ied]
   
def get_namelink( str ):
    name = getsubstr( str, '[', ']' )
    link = getsubstr( str, '(', ')' )
    return name, link
    
str = "-  [【Python科学计算三维可视化】北京理工大学](https://www.bilibili.com/video/BV1F7411i74Q/)."   
str1,str2 = get_namelink( str )
print("str1={}".format(str1))
print("str2={}".format(str2))
    



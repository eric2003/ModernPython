def getsubstr( str, s, t ):
    ist = str.find(s)
    ied = str.find(t)

    return str[ist+1:ied]
   
def get_namelink( str ):
    name = getsubstr( str, '[', ']' )
    link = getsubstr( str, '(', ')' )
    return name, link
    
filepath = 'example.txt'
with open(filepath, 'r', encoding='UTF-8') as fp:
   line = fp.readline()
   cnt = 1
   while line:
       print("Line {}: {}".format(cnt, line.strip()))
       str1,str2 = get_namelink( line )
       print("str1={}".format(str1))
       print("str2={}".format(str2))       
       line = fp.readline()
       cnt += 1
    



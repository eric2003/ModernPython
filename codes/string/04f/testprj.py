def getsubstr( str, s, t ):
    ist = str.find(s)
    ied = str.find(t)

    return str[ist+1:ied]
   
def get_namelink( str ):
    name = getsubstr( str, '[', ']' )
    link = getsubstr( str, '(', ')' )
    return name, link
    
filepath = 'example.txt'
str1_list = []
str2_list = []
with open(filepath, 'r', encoding='UTF-8') as fp:
   line = fp.readline()
   while line:
       str1,str2 = get_namelink( line )
       str1_list.append( str1 )
       str2_list.append( str2 )
       line = fp.readline()
       
filename = "output.txt"
with open(filename, 'w', encoding='UTF-8') as fpout:
    nLines = len(str1_list)
    for i in range( nLines ):
        str1 = str1_list[i]
        str2 = str2_list[i]
        str = str1 + " <" + str2 + ">'_"
        print("str={}".format(str) )
        #fpout.write("i={}, nLines={}\n".format(i, nLines))
        #fpout.write("str1={}\n".format(str1))
        #fpout.write("str2={}\n".format(str2))


    



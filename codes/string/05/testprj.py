def getsubstr( str, s, t ):
    ist = str.find(s)
    ied = str.find(t)

    return str[ist+1:ied]
   
def get_namelink( str ):
    name = getsubstr( str, '[', ']' )
    link = getsubstr( str, '(', ')' )
    return name, link
    
#. 'Metis official website <http://glaros.dtc.umn.edu/gkhome/metis/metis/overview/>'_

def get_sphinx_namelink( str ):
    name = getsubstr( str, '`', '<' )
    link = getsubstr( str, '<', '>' )
    return name, link  

str1_list = []
str2_list = []
    
sphinx_filename = "sphinx.rst"    
with open(sphinx_filename, 'r', encoding='UTF-8') as fp:
   line = fp.readline()
   while line:
       str1,str2 = get_sphinx_namelink( line )
       str1_list.append( str1 )
       str2_list.append( str2 )
       line = fp.readline()

mkdocs_filename = "mkdocs.md"
with open(mkdocs_filename, 'w', encoding='UTF-8') as fpout:
    nLines = len(str1_list)
    for i in range( nLines ):
        str1 = str1_list[i]
        str2 = str2_list[i]
        str = "- [" + str1 + "](" + str2 + ")."
        print("str={}".format(str) )
        fpout.write("{}\n".format(str))


    



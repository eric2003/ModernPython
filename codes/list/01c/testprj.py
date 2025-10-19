list1 = ['a1', 'a2']
list2 = ['b1', 'b2']
list3 = ['c1', 'c2']
list = []
list.append( list1 )
list.append( list2 )
list.append( list3 )

mylen = len(list)
for i in range(mylen):
    print(list[i])

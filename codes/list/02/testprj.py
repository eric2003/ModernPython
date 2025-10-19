import numpy as np

ni = 10
nm = 3
q = np.zeros( (ni, nm ) )
x = np.zeros( (ni) )

list=[]

for i in range(ni):
    x[i]=i
    q[i,0]=1.0 + i * 0.001
    q[i,1]=0.0 + i * 0.001
    q[i,2]=0.1 + i * 0.001
    ll = []
    ll.append(x[i])
    ll.append(q[i,0])
    ll.append(q[i,1])
    ll.append(q[i,2])
    list.append(ll)
    

mylen = len(list)
for i in range(mylen):
    print(list[i])

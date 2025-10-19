import numpy as np

A = [[1, -1], [21, -20]]
print("A=\n",A)

b = [-1,-19]
print("b=\n",b)

x = np.linalg.solve(A, b)
d = A@x
print("d=\n",d)

e=np.dot(A,x)

print("e=\n",e)


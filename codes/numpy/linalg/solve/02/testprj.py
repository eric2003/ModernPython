import numpy as np

a = np.array([[1, 2], [3, 5]])
b = np.array([1, 2])
x = np.linalg.solve(a, b)
print("a=\n",a)
print("b=\n",b)
print("x=\n",x)

result=np.allclose(np.dot(a, x), b)

print("result=\n",result)
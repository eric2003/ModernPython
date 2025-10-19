#https://www.w3resource.com/numpy/manipulation/stack.php

import numpy as np

x1 = np.array([1, 2, 3])
y1 = np.array([4, 5, 6])
z1 = np.stack((x1, y1))
print("z1=",z1)
print()
x2 = np.array([11, 21, 31])
y2 = np.array([41, 51, 61])
z2 = np.stack((x2, y2))
print("z2=",z2)
print()

z3 = np.stack((z1, z2))

print("z3=",z3)
print()

z4 = np.stack((z1, z2), axis=2)

print("z4=",z4)
print()


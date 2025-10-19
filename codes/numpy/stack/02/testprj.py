#https://www.w3resource.com/numpy/manipulation/stack.php

import numpy as np

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
z1 = np.stack((x, y))
print(z1)
print()
z2 = np.stack((x, y), axis=-1)
print(z2)

#https://www.w3resource.com/numpy/manipulation/stack.php

import numpy as np

x = np.array([2, 3, 4])
y = np.array([3, 4, 5])
z = np.stack((x, y))
print(z)

#https://www.w3resource.com/numpy/manipulation/stack.php

import numpy as np

a1 = np.random.randn(3)
s1 = np.stack(a1, axis=0).shape
print(s1)

a2 = np.random.randn(3,4)
s2 = np.stack(a2, axis=0).shape
print(s2)

s3 = np.stack(a2, axis=1).shape
print(s3)



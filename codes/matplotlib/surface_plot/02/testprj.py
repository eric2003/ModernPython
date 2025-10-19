import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

A = np.matrix([[3.0, 2.0], [2.0, 6.0]])
b = np.matrix([[2.0], [-8.0]])  # we will use the convention that a vector is a column vector
c = 0.0

def f(x, A, b, c):
    return np.sum(0.5 * x.T * A * x - b.T * x + c)
    
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(1,2,1,projection='3d')
size = 20
x1 = list(np.linspace(-6, 6, size))
x2 = list(np.linspace(-6, 6, size))
x1, x2 = np.meshgrid(x1, x2)
zs = np.zeros((size, size))
for i in range(size):
    for j in range(size):
        x = np.matrix([[x1[i,j]], [x2[i,j]]])
        zs[i,j] = f(x, A, b, c)
ax.plot_surface(x1, x2, zs, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0)
ax2 = fig.add_subplot(1,2,2,projection='3d')
ax2.plot_surface(x1, x2, zs, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0)
plt.show()
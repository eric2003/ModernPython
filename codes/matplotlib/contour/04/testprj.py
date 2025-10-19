# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

nx = 64
ny = 64

x = np.zeros(nx+1)
y = np.zeros(ny+1)
  
xmin = -1
xmax = 1
ymin = -1
ymax = 1

dx = ( xmax - xmin ) / nx
dy = ( ymax - ymin ) / ny

x[0] = xmin
y[0] = ymin

for i in range(nx):
    x[i+1] = xmin + ( i + 1 ) * dx

for j in range(ny):
    y[j+1] = ymin + ( j + 1 ) * dy


#print("x=\n",x)
#print("y=\n",y)
  
# Creating 2-D grid of features
[X, Y] = np.meshgrid(x, y)
  
fig, ax = plt.subplots(1, 1)

Z = np.sqrt(X**2+Y**2)
  
# plots contour lines
ax.contour(X, Y, Z)
  
plt.show()
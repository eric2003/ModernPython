# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
  
feature_x = np.arange(0, 50, 2)
feature_y = np.arange(0, 50, 3)

print("feature_x=\n",feature_x)
print("feature_y=\n",feature_y)
  
# Creating 2-D grid of features
[X, Y] = np.meshgrid(feature_x, feature_y)
  
fig, ax = plt.subplots(1, 1)
  
Z = np.cos(X / 2) + np.sin(Y / 4)
  
# plots contour lines
#ax.contour(X, Y, Z)
ax.contour(Z)
  
plt.show()
# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
  
feature_x = np.arange(0, 50, 2)
feature_y = np.arange(0, 50, 3)
  
# Creating 2-D grid of features
[X, Y] = np.meshgrid(feature_x, feature_y)
  
fig, ax = plt.subplots(1, 1)
  
Z = np.cos(X / 2) + np.sin(Y / 4)
  
# plots contour lines
ax.contour(X, Y, Z)
  
ax.set_title('Contour Plot')
ax.set_xlabel('feature_x')
ax.set_ylabel('feature_y')
  
plt.show()
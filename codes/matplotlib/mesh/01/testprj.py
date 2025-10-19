import matplotlib.pyplot as plt
import numpy as np
  
plt.vlines(np.linspace(0,1,11), 0, 0.6)
plt.hlines(np.linspace(0,0.6,7), 0, 1)
  
plt.show()
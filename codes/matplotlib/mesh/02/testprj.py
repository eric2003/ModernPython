import matplotlib.pyplot as plt
import numpy as np
  
x = np.linspace(0,1,11)
y = np.linspace(0,0.6,7)
plt.vlines(x, y[0], y[-1] )
plt.hlines(y, x[0], x[-1] )

plt.show()
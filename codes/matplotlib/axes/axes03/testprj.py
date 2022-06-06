import matplotlib.pyplot as plt
import numpy as np

ax = plt.axes()
x = np.linspace(0, 10, 100)
ax.plot(x, np.sin(x), 'o-r');
ax.plot(x, np.cos(x), '--');
plt.show()
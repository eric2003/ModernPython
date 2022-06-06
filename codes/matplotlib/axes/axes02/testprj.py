import matplotlib.pyplot as plt
import numpy as np

ax = plt.axes()
x = np.linspace(0, 10, 1000)
ax.plot(x, np.sin(x));
plt.show()
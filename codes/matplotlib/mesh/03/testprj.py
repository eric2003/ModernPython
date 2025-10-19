import numpy as np
import matplotlib.pyplot as plt

x, y = np.meshgrid(np.linspace(0,1, 11), np.linspace(0, 0.6, 7))

plt.plot(x, y) # use plot, not scatter
xt=np.transpose(x)
yt=np.transpose(y)

plt.plot(xt, yt) # add this here
plt.show()

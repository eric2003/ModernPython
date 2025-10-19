import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

x, y = np.meshgrid(np.linspace(0,1, 11), np.linspace(0, 0.6, 7))

plt.scatter(x, y)

segs1 = np.stack((x,y), axis=2)
segs2 = segs1.transpose(1,0,2)
plt.gca().add_collection(LineCollection(segs1))
plt.gca().add_collection(LineCollection(segs2))
plt.show()


#https://stackoverflow.com/questions/47295473/how-to-plot-using-matplotlib-python-colahs-deformed-grid

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

def plot_grid(x,y, ax=None, **kwargs):
    ax = ax or plt.gca()
    segs1 = np.stack((x,y), axis=2)
    segs2 = segs1.transpose(1,0,2)
    ax.add_collection(LineCollection(segs1, **kwargs))
    ax.add_collection(LineCollection(segs2, **kwargs))
    ax.autoscale()


f = lambda x,y : ( x+0.8*np.exp(-x**2-y**2),y )

fig, ax = plt.subplots()

grid_x,grid_y = np.meshgrid(np.linspace(-3,3,20),np.linspace(-3,3,20))
distx, disty = f(grid_x,grid_y)
plot_grid(distx, disty, ax=ax, color="blue")

plt.show()

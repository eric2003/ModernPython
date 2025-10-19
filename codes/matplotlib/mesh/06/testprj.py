#https://stackoverflow.com/questions/47295473/how-to-plot-using-matplotlib-python-colahs-deformed-grid

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

def plot_grid(x,y, ax=None, **kwargs):
    ax = ax or plt.gca()
    segs1 = np.stack((x,y), axis=2)
    print("x =",x)
    print("y =",y)
    print("x shape=",np.stack(x, axis=0).shape)
    print("segs1 =",segs1)
    print("segs1 shape=",np.stack(segs1, axis=0).shape)
    print("type(segs1) =",type(segs1))
    segs2 = segs1.transpose(1,0,2)
    print("type(segs2) =",type(segs2)) 
    print("segs2 =",segs2)    
    ax.add_collection(LineCollection(segs1, **kwargs))
    ax.add_collection(LineCollection(segs2, **kwargs))
    ax.autoscale()


f = lambda x,y : ( x+0.8*np.exp(-x**2-y**2),y )

fig, ax = plt.subplots()

grid_x,grid_y = np.meshgrid(np.linspace(0,1,4),np.linspace(0,1,5))
plot_grid(grid_x,grid_y, ax=ax,  color="lightgrey")

#distx, disty = f(grid_x,grid_y)
#plot_grid(distx, disty, ax=ax, color="C0")

plt.show()

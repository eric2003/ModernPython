import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 6])
y1 = np.array([0, 100])

# using the variable ax for single a Axes
#fig, ax = plt.subplots()

# using the variable axs for multiple Axes
fig, axs = plt.subplots(2, 1)

axs[0].plot(x1,y1)
axs[0].set_xlabel("x1")
axs[0].set_ylabel("y1")

axs[1].plot(x1,y1)
axs[1].set_xlabel("x2")
axs[1].set_ylabel("y2")

plt.show()
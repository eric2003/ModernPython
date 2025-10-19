import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 6])
y1 = np.array([0, 100])


# using tuple unpacking for multiple Axes
fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.plot(x1,y1)
ax1.set_xlabel("x1")
ax1.set_ylabel("y1")

ax2.plot(x1,y1)
ax2.set_xlabel("x2")
ax2.set_ylabel("y2")

plt.show()
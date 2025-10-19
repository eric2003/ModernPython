import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 6])
y1 = np.array([0, 100])

# using the variable ax for single a Axes
fig, ax = plt.subplots()

ax.plot(x1,y1)
ax.set_xlabel("x")
ax.set_ylabel("y")

plt.show()
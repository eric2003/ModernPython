import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 6])
y1 = np.array([0, 100])

fig, ax1 = plt.subplots()
ax1.plot(x1,y1)
ax1.set_title("plot 1")
ax1.set_xlabel("x")
ax1.set_ylabel("y")

fig, ax2 = plt.subplots()
ax2.plot(x1,y1)
ax2.set_title("plot 2")
ax2.set_xlabel("u")
ax2.set_ylabel("v")

plt.show()
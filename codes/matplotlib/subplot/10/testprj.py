import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 6])
y1 = np.array([0, 100])


# using tuple unpacking for multiple Axes
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

ax1.plot(x1,y1)
ax1.set_xlabel("x1")
ax1.set_ylabel("y1")

ax2.plot(x1,y1)
ax2.set_xlabel("x2")
ax2.set_ylabel("y2")

ax3.plot(x1,y1)
ax3.set_xlabel("x3")
ax3.set_ylabel("y3")

ax4.plot(x1,y1)
ax4.set_xlabel("x4")
ax4.set_ylabel("y4")

plt.tight_layout()
plt.show()
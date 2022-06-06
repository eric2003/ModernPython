import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

#plot 1:
x1 = np.array([0, 6])
y1 = np.array([0, 100])

ax1 = fig.add_subplot(1,2,1)
ax1.plot(x1,y1)
ax1.set_title("plot 1")
ax1.set_xlabel("xxx")
ax1.set_ylabel("yyy")

#plot 2:
x2 = np.array([1, 2, 3, 4])
y2 = np.array([1, 4, 9, 16])

ax2 = fig.add_subplot(1,2,2)
ax2.plot(x2,y2)
ax2.set_title("plot 2")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
plt.suptitle("Subplot Test")
plt.show()
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x1 = np.array([0, 6])
y1 = np.array([0, 100])

plt.subplot(1, 2, 1)
plt.plot(x1,y1)
plt.title("plot 1")

#plot 2:
x2 = np.array([1, 2, 3, 4])
y2 = np.array([1, 4, 9, 16])

plt.subplot(1, 2, 2)
plt.plot(x2,y2)
plt.title("plot 2")

plt.suptitle("Subplot Test")
plt.show()
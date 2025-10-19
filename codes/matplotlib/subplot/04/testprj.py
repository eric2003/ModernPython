import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 6])
y1 = np.array([0, 100])

fig, ax1 = plt.subplots()
ax1.plot(x1,y1)
ax1.set_title("plot 1")
ax1.set_xlabel("xxx")
ax1.set_ylabel("yyy")

plt.show()
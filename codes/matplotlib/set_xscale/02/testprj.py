import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x**2

# Create figure
fig, ax = plt.subplots()

ax.plot(x, y)
ax.set_xscale("log", base=2)
ax.set_yscale("log", base=10)
ax.set_title("Normal scale")

plt.show()
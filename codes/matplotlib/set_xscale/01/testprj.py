import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.set_xscale('log', base=2)
ax.set_yscale('log', base=10)

ax.plot(range(1024))
plt.show()
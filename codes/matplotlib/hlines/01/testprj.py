import matplotlib.pyplot as plt

# Add horizontal line
plt.hlines(y=1, xmin=1, xmax=4, lw=7, color='orange')
plt.text(4, 1, 'y=1', ha='left', va='center')

# Add another horizontal line
plt.hlines(y=2, xmin=2, xmax=5, lw=7, color='red')
plt.text(2, 2, 'y=2', ha='right', va='center')

plt.show()
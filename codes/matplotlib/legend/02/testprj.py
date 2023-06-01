import matplotlib.pyplot as plt

line, = plt.plot([1, 2, 3])
line.set_label('Label via method')
plt.legend()

plt.show();
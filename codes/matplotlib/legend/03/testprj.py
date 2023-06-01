import matplotlib.pyplot as plt

line1, = plt.plot([1, 2, 3])
line2, = plt.plot([4, 5, 6])
line3, = plt.plot([7, 8, 9])

plt.legend([line1, line2, line3], ['label1', 'label2', 'label3'])

plt.show();
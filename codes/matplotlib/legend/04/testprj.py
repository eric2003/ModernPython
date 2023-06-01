import matplotlib.pyplot as plt

line1, = plt.plot([1, 2, 3],label='haha1')
line2, = plt.plot([4, 5, 6],label='haha2')
line3, = plt.plot([7, 8, 9],label='haha3')

plt.legend(handles=[line1, line2, line3])

plt.show();
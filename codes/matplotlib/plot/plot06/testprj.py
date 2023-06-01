import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [4, 5, 6]
#plt.plot([1, 2, 3], [4, 5, 6] ) # plot x and y using default line style and color
#plt.plot([1, 2, 3], [4, 5, 6], 'bo' ) # plot x and y using blue circle markers
#plt.plot([4, 5, 6] ) # plot y using x as index array 0..N-1
#plt.plot(y, 'r+') # ditto, but with red plusses
#plt.plot(x, y, 'go--', linewidth=2, markersize=12)
plt.plot(x, y, color='green', marker='o', linestyle='dashed',
     linewidth=2, markersize=12)
plt.show()
from matplotlib import pyplot as plt
  
plt.hlines(y = 1, xmin = 1, xmax = 4, label ="black line")
  
plt.hlines(y = 1.6, xmin = 1.5, xmax = 4.5, color ='r')
plt.text(1, 1.6, 'Red line', ha ='left', va ='center')
plt.text(2, 1.8, 'Reddd line', ha ='left', va ='center')
  
plt.hlines(y = 2, xmin = 2, xmax = 5)

plt.show()
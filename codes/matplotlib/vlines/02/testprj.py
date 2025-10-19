#https://www.datasciencelearner.com/matplotlib-vlines-example-implementation/

import matplotlib.pyplot as plt
plt.vlines(2, 0, 8, linestyles ="solid", colors ="red")
plt.vlines(7, 0, 8, linestyles ="dashed", colors ="blue")
plt.xlim(0, 15) 
plt.ylim(0, 15) 
plt.show()
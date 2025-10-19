#https://www.datasciencelearner.com/matplotlib-vlines-example-implementation/

import matplotlib.pyplot as plt 
plt.vlines((3, 4, 7,), 0, 10, colors = ("b", "r", "g"), 
         linestyles = ("dotted", "dashed","solid")) 
  
plt.show() 
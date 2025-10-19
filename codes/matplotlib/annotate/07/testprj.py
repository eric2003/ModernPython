import numpy as np
import matplotlib.pyplot as plt

# Create our figure and data we'll use for plotting
fig, ax = plt.subplots(figsize=(4, 4))

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)

# Plot a line and add some simple annotations
line, = ax.plot(t, s)
ax.annotate('figure pixels',
            xy=(100, 10), xycoords='figure pixels')
            
x = line.get_xdata()[-1]
y = line.get_ydata()[-1]
print("x=",x)
print("y=",y)
#ax.annotate("haha", xy=(1,y), xytext=(1,0), textcoords="figure fraction" )  
ax.annotate("haha", xy=(0,0), xytext=(0.5,0.5), textcoords="figure fraction" )  
ax.annotate("haha1", xy=(0,y), xytext=(0,0), textcoords='data' )  
ax.annotate("hello", xy=(x,y), xytext=(x,y), textcoords='data' )  
ax.annotate("world", xy=(0,0), xytext=(x,y), textcoords='data' )  
            

plt.show()
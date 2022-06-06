import matplotlib.pyplot as plt

fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
ax.plot([0,1,2], [10,20,3])
fig.savefig('test.png')   # save the figure to file
plt.close(fig)    # close the figure window

plt.show()
#https://www.studytonight.com/matplotlib/matplotlib-3d-wireframe-plot-plot_wireframe-function

from mpl_toolkits.mplot3d import axes3d 
from matplotlib import pyplot 

fig = pyplot.figure() 
wf = fig.add_subplot(111, projection='3d') 
x, y, z = axes3d.get_test_data(0.07) 
wf.plot_wireframe(x,y,z, rstride=2, cstride=2, color='maroon') 

wf.set_title('3D wireframe plot') 
pyplot.show() 
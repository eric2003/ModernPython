#https://www.studytonight.com/matplotlib/matplotlib-3d-wireframe-plot-plot_wireframe-function

from matplotlib import pyplot 
import numpy 

a = numpy.linspace(-5, 5, 25) 
b = numpy.linspace(-5, 5, 25) 
x, y = numpy.meshgrid(a, b) 
z = numpy.cos(numpy.sqrt(x**2 + y**2)) 

fig = pyplot.figure() 
wf = pyplot.axes(projection ='3d') 
wf.plot_wireframe(x, y, z, color ='blue') 

wf.set_title('Example 2') 
pyplot.show() 
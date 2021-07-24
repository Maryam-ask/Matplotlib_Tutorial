import matplotlib.pyplot
import numpy

x_points = numpy.array([0, 2, 4, 8])
y_points = numpy.array([8, 4, 2, 0])

# matplotlib.pyplot.plot(x_points, y_points, ls='-.', c='r')
# matplotlib.pyplot.plot(x_points, y_points, ls='-.', c='#6f1548')    # hexadecimal color
matplotlib.pyplot.plot(x_points, y_points, ls='-.', c='hotpink') # Color Names Supported by All Browsers (HTML color names)
matplotlib.pyplot.show()
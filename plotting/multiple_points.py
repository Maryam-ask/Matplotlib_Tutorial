# Multiple Points
#
# You can plot as many points as you like, just make sure you have the same number of points in both axis.


import matplotlib.pyplot as pyp
import numpy as num

x_points = num.array([1, 2, 6, 8])
y_points = num.array([3, 8, 1, 10])


pyp.plot(x_points, y_points)
pyp.show()
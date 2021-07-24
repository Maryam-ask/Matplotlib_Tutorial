import matplotlib.pyplot as pyp
import numpy as npy

x_points = npy.array([2, 3, 4, 5, 6])
y_points = npy.array([4, 9, 16, 25, 36])

# pyp.plot(x_points, y_points, marker='d', ms=20, mec='r')
# pyp.show()


# You can use the keyword argument markerfacecolor or the shorter mfc to set the color inside the edge of the markers:
pyp.plot(x_points, y_points, marker='h', ms=30, mfc='r')
pyp.show()

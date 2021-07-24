import matplotlib.pyplot as pl
import numpy as nump

x_points = nump.array([2, 8, 4, 9, 10])
y_points = nump.array([2, 4, 1, 7, 5])

pl.plot(x_points, y_points, marker='*', ms=20)
pl.show()


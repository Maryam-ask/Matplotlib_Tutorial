import matplotlib.pyplot as pyp
import numpy as npy

x_points = npy.array([2, 3, 4, 5, 6])
y_points = npy.array([4, 9, 16, 25, 36])

pyp.plot(x_points,y_points, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')
# pyp.plot(x_points, y_points, marker='d', ms=20, mec='#4CAF50', mfc='#4CAF50')
pyp.show()

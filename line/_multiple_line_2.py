import matplotlib.pyplot as plt
import numpy as np

x_line1_points = np.array([0, 1, 8, 18, 2])
y_line1_points = np.array([9, 1, 2, 12, 0])

x_line2_points = np.array([1, -2, -9, 12])
y_line2_points = np.array([-9, -2, 0, 4])

plt.plot(x_line1_points, y_line1_points, ls='--', c='blueviolet', lw='2')
plt.plot(x_line2_points, y_line2_points, ls='-.', c='hotpink', lw='6')

plt.show()
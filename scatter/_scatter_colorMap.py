import matplotlib.pyplot as plt
import numpy as np

x_axis = np.array([4, 5, 6, 7, 8, 9, 10, 12, 4])
y_axis = np.array([99, 100, 40, 20, 103, 88, 82, 77, 29])

colors = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80])

plt.scatter(x_axis, y_axis, c=colors, cmap='viridis')
plt.show()

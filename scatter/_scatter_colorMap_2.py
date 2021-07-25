import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 8, 4, 2, 6, 8, 2, 1])
y = np.array([9, 10, 33, 17, 89, 90, 100, 50])

color= np.array([10, 20, 30, 40, 50, 60, 70, 80])

plt.scatter(x, y, c=color, cmap='viridis')
# for showing the colorMap
plt.colorbar()
plt.show()
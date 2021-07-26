# Horizontal Bars:
from matplotlib import pyplot as plt
import numpy as np

x = np.array(['Maryam', 'Nadia', 'Mohammad'])
y = np.array([27, 23, 19])

plt.barh(x, y, color='#4CAF50', height=0.1)
plt.show()
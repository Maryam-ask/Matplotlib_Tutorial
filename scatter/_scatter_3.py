import matplotlib.pyplot as plt
import numpy as np

x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 77, 85])

# for each dot
colors = np.array(['red', 'green', 'blue', 'yellow', 'pink', 'black',
                   'orange', 'purple', 'brown', 'gray'])

plt.scatter(x, y, c=colors)
plt.show()
import matplotlib.pyplot as plt
import numpy as np

x = np.array([32, 25, 25, 15])
_labels = ["Apples", "Oranges", "cherries", "carrots"]

plt.pie(x, labels=_labels)
plt.show()
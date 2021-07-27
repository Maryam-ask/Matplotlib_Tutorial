from matplotlib import pyplot as plt
import numpy as np

x = np.array([45, 25, 30, 10])
my_labels = ["Apple", "Cherries", "Oranges", "Bananas"]
my_explode = [0.2, 0, 0, 0]

# Shadow:  shadow=True
plt.pie(x, labels=my_labels, explode=my_explode, shadow=True)
plt.show()
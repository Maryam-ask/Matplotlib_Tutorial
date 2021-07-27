import matplotlib.pyplot as plt
import numpy as np

x = np.array([30, 40, 25, 10])
my_labels = ["Cats", "Dogs", "Rabbits", "Birds"]
my_colors = ["black", "b", "hotpink", "#4caf50"]

plt.pie(x, labels=my_labels, colors=my_colors)
# Legends:
plt.legend(title='Four Fruits:')
plt.show()

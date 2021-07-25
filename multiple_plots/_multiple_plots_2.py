import matplotlib.pyplot as plt
import numpy as np

# plot 1:
x1 = np.array([0, 1, 2, 3])
y1 = np.array([0, 4, 2, 3])

plt.subplot(2, 2, 1)
plt.plot(x1, y1)
plt.title("SALES")

# plot 2:
x2 = np.array([2, 4, 8])
y2 = np.array([1, 2, 3])

plt.subplot(2, 2, 2)
plt.plot(x2, y2)


# plot 3:
x3 = np.array([0, 2, 5, 7])
y3 = np.array([10, 20, 50, 70])

plt.subplot(2, 2, 3)
plt.plot(x3, y3)
plt.title("INCOMES")


# plot 4:
x4 = np.array([16, 9, 4, 1])
y4 = np.array([4, 3, 2, 1])

plt.subplot(2, 2, 4)
plt.plot(x4, y4)

plt.show()
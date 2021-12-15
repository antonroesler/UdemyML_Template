import matplotlib.pyplot as plt
import numpy as np



y1 = [2, 4, 6, 2, 7, 8, 3, 5, 2, 8, 4, 6, 1]
y2 = [6, 7, 3, 2, 5, 7, 3, 1, 8, 6, 3, 1, 3]

y1 = np.array(y1)
y2 = np.array(y2)

# Plot
plt.plot(range(len(y1)), y1)
plt.plot(range(len(y2)), y2)
plt.legend(["Peter", "Fridel"])
plt.xlabel("Month")
plt.ylabel("Number of Dates")

plt.title("Number of Dates per Month of Peter and Fridel")

plt.show()

# Scatter
plt.scatter(range(len(y1)), y1)
plt.scatter(range(len(y2)), y2)
plt.legend(["Peter", "Fridel"])
plt.xlabel("Month")
plt.ylabel("Number of Dates")

plt.title("Number of Dates per Month of Peter and Fridel")

plt.show()

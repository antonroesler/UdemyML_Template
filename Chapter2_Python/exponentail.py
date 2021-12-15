import numpy as np
import matplotlib.pyplot as plt
a = [1, 2, 8]

y = np.exp(a)

print(y)


plt.plot(range(8), np.exp(range(8)))
plt.xlabel("x")
plt.ylabel("e(x)")
plt.title("e(x)")
plt.show()

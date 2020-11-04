import numpy as np
import matplotlib.pyplot as plt

n = 1000
a = np.random.normal(0, 1, (n, n))
A = a + a.T
v = np.linalg.eigvalsh(A)

print(v)
plt.hist(v, density=True)
plt.show()

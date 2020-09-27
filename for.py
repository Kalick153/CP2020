import numpy as np
import matplotlib.pyplot as plt

a = np.array([[3, 0], [0, -2]])
u, s, vh = np.linalg.svd(a)
v = np.transpose(vh)
plt.arrow(0, 0, *u[:,0] * s[0], color='red')
plt.arrow(0, 0, *u[:,1] * s[1], color='blue')
# plt.arrow(0, 0, *v[:,0] * s[0], color='red')
# plt.arrow(0, 0, *v[:,1] * s[1], color='blue')
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.show()


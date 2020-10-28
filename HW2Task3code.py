import numpy as np
import matplotlib.pyplot as plt

a = np.array([[3, 0], [0, -2]])
u, s, vh = np.linalg.svd(a)
v = np.transpose(vh)
print(s)
plt.arrow(0, 0, *u[:,0] * s[0], color='red')
plt.arrow(0, 0, *u[:,1] * s[1], color='blue')

ell = np.arange(0, 2 * np.pi, 0.01)
x = s[0] * np.cos(ell)
y = s[1] * np.sin(ell)
a = u.T[0][1]
b = u.T[0][0]
cos = 1 / (1 + (a / b) ** 2) ** 0.5
sin = (a / b) / (1 + (a / b) ** 2) ** 0.5
plt.plot(x * cos - sin * y, sin * x + cos * y)
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.show()

circle = np.arange(0, 2 * np.pi, 0.01)
plt.arrow(0, 0, *v[:,0], color='red')
plt.arrow(0, 0, *v[:,1] , color='blue')
plt.plot(np.cos(circle), np.sin(circle))
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.show()

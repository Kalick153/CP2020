import numpy as np
import matplotlib.pyplot as plt

# 1 + cos x = 0
n = 100
x = np.zeros(n)
x[0] = 1
for i in range(1, n):
    x[i] = x[i-1] + (np.cos(x[i-1]) + 1) / np.sin(x[i-1])

print(x)
err = (x - np.pi)**2
plt.plot(err)
plt.title("1 + сos x = 0")
plt.yscale('log')
plt.show()
# получили, что сходимость линейная

# x**2 = 2
n = 10
x = np.zeros(n)
x[0] = 1
for i in range(1, n):
    x[i] = 1/2 * (x[i-1] + 2 / x[i-1])

print(x)
err = (x - np.sqrt(2))**2
plt.plot(err)
plt.yscale('log')
plt.title("x**2 = 2")
plt.show()
# получили, что зависимость квадратичная

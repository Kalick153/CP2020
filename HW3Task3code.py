import numpy as np
import matplotlib.pyplot as plt

a = np.zeros((15, 28))
a[2:-2, 1] = 1
a[2, 2:6] = 1
a[2:7, 6] = 1
a[7:-2, 7] = 1
a[7, 2:7] = 1
a[-3, 2:7] = 1
a[2:-2, 10] = 1
a[2:-2, 14] = 1
a[2:-2, 18] = 1
a[-3, 10:19] = 1
a[2:-2, 26] = 1
a[2, 21:26] = 1
a[7, 21:26] = 1
a[12, 21:26] = 1
plt.imshow(a)
plt.show()
U, s, V = np.linalg.svd(a)
rank = np.linalg.matrix_rank(a)
print(U, s, V)
print(rank)

for i in range(rank + 1):
    B = np.zeros((len(U), len(V)))
    for j in range(i):
        B += s[j] * np.matrix(U.T[j]).T * np.matrix(V[j])
    plt.imshow(B)
    plt.show()


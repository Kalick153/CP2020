import numpy as np

n = 1000
a = np.random.normal(0, 1, (n, n))
A = a @ a.T
v = np.linalg.eigvalsh(A)

q, r = np.linalg.qr(A)
k = 0
while True:
    k += 1
    ak = r @ q
    q, r = np.linalg.qr(ak)
    if 0.99 * np.min(v) <= np.min(np.diag(ak)) <= 1.01 * np.min(v):
        break


print(k)

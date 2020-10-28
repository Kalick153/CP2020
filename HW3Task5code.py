import numpy as np

A = np.zeros((2, 10))
A[1, 0:11] = 1


# из формулы xi = x(i-1) + u(i-1) * t + at^2/2 ;
# в нашем случае t = 1, a = f => xi = x(i-1) + u(i-1) + fi/2
# u0 = at => ui = f1 + f2 + f3....
# тогда x1 = f1/2, x2 = f1/2 + f1 + f2/2 = (1/2 + 1)f1 + 1/2 f2 ....
xo = 0
u = 0
for i in range(0, 10):
    A[0, i] = 1 / 2 + 9 - i
print(A)

u, s, vh = np.linalg.svd(A)
v = np.transpose(vh)

a = np.zeros((2, 1))
a[0] = 1
a[1] = 0


sfull = np.zeros((2, 10))
sfull[0, 0] = 1/s[0]
sfull[1, 1] = 1/s[1]

# Apinv = np.linalg.pinv(A)
# fpinv = Apinv @ a

Ap = v @ sfull.T @ u.T
f = Ap @ a
print(f)
# совпало с f, найденным с помощью pinv

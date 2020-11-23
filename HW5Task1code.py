import numpy as np
import matplotlib.pyplot as plt

with np.load('data.npz') as data:
    A, C = data['A'], data['C']

def mat2vec (A):
    h, w = A. shape
    a = np. zeros (h*w, dtype =A. dtype )
    A = np. flipud (A)
    for i, row in enumerate (A):
        a[i*w:i*w+w] = row
    return a

def vec2mat (a, shape ):
    h, w = shape
    A = np. zeros (shape , dtype =a. dtype )
    for i in range (h):
        A[i, :] = a[i*w:i*w+w]
    return np. flipud (A)

a = mat2vec(A)

# получим изображение как на рис1
plt.imshow(A)
plt.show()


# посмотрим, что делает фильтр С
X = np.zeros(((16, 51)))
X[2:12, 10] = 1
X[2:12, 40] = 1
X[2, 10:40] = 1
X[12, 10:41] = 1

x0 = mat2vec(X)
x = C @ x0
X = vec2mat(x, (25, 60))

plt.imshow(X)
plt.show()

a0_guess = np.linalg.pinv(C) @  a
A0_guess = vec2mat(a0_guess, (16, 51))
plt.imshow(A0_guess)
plt.show()
# такой способ не сработал, попробуем через SVD


u, s, vh = np.linalg.svd(C)
v = np.transpose(vh)

sfull = np.zeros((25 * 60, 16 * 51))

for i in range(len(s) - 450):
    sfull[i][i] = 1/s[i]

Cp = v @ sfull.T @ u.T
aguess = Cp @ a
Aguess = vec2mat(aguess, (16, 51))
plt.imshow(Aguess)
plt.show()

# на картинке - БОТАЙ

import numpy as np
#внизу пример вывода

A = np.array([(3, 1, 0, 0), (1, 2, 0, 1), (0, 0, 1, 1), (0, 1, 1, 1)])
vo = np.random.random(4)
print("Начальный вектор", vo)
v = vo
sys = np.linalg.eigh(A)
psi = sys[1][:, -1]
v /= np.sqrt(v @ v)
v *= np.sign(v[0]/psi[0])

print("\n", "Степенная итерация")
for i in range(100):
    v = A @ v
    v /= np.sqrt(v @ v)
    if np.linalg.norm(v - psi) < 10**(-3):
        print("Номер итерации и точность:", i, np.linalg.norm(v - psi))
        break

maxeigval = (v @ (A @ v)) / (v @ v)
print("Приближение:", maxeigval, "\n", "Значение через linalg:", sys[0][3])

v = vo
m1 = 3.5
print("\n", "Обратная итерация с m =", m1)
for i in range(20):
    v = np.linalg.inv(A - m1 * np.eye(4)) @ v
    v /= np.sqrt(v @ v)
    if np.linalg.norm(v - psi) < 10**(-3):
        print("Номер итерации и точность:", i, np.linalg.norm(v - psi))
        break
maxeigval = (v @ (A @ v)) / (v @ v)
print("Приближение:", maxeigval, "\n", "Значение через linalg:", sys[0][3])

v = vo
m2 = 3.7
print("\n", "Обратная итерация с m =", m2)
for i in range(20):
    v = np.linalg.inv(A - m2 * np.eye(4)) @ v
    v /= np.sqrt(v @ v)
    if np.linalg.norm(v - psi) < 10**(-3):
        print("Номер итерации и точность:", i, np.linalg.norm(v - psi))
        break
maxeigval = (v @ (A @ v)) / (v @ v)
print("Приближение:", maxeigval, "\n", "Значение через linalg:", sys[0][3])

# Пример вывода:
# Начальный вектор [0.72733938 0.4637855  0.94944749 0.18183926]
#
#  Степенная итерация
# Номер итерации и точность: 12 0.0007064183151297696
# Приближение: 3.7507997072840586
#  Значение через linalg: 3.750800422060915
#
#  Обратная итерация с m = 3.5
# Номер итерации и точность: 3 0.0007517829639960998
# Приближение: 3.750799602428915
#  Значение через linalg: 3.750800422060915
#
#  Обратная итерация с m = 3.7
# Номер итерации и точность: 1 0.000572502356867508
# Приближение: 3.7507998525683677
#  Значение через linalg: 3.750800422060915



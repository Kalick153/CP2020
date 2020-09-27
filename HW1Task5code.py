import math


def round_to_n(x, n):
    if x == 0:
        return x
    else:
        return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))


res = 0
for k in range(1, 3001):
    res = round_to_n(res + 1 / k ** 2, 4)
print(res)

res = 0
for k in range(1, 3001):
    res = round_to_n(res + 1 / (3001 - k)**2, 4)
print(res)

# при прямом суммировании с некоторого значения k ошибка округления отрицательной,
# так как все члены меньше 0.0005 перестанут изменять наше число
# из-за этого суммарная ошибка будет накапливаться
# при обратном же суммировании такого происходить не будет

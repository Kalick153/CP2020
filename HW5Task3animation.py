import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, writers

# скопируем генерацию матрицы и получим спектр
n = 12
A = np.zeros((n, n))
A[n - 1, 0] = -1
for i in range(0, n, 2):
    A[i][i] = 4
    A[i + 1][i + 1] = 2
    A[i][i + 1] = -2
    A[i][i - 1] = -2
    A[i + 1][i] = -1
for i in range(0, n - 2, 2):
    A[i + 1][i + 2] = -1

eigval, eigvec = np.linalg.eig(A)
eigval = np.abs(eigval)
w = np.sqrt(eigval)
# теперь можем начать анимацию
# зададим константы


# минимальная частота очень маленька, поэтому домножим её для наглядности
# для наглядности так же увеличим амплитуды
w = [5 * 10 ** 7 * np.min(w), np.max(w), w[-2]]
u = [3 * eigvec[:, np.argmin(eigval)], 3 * eigvec[:, np.argmax(eigval)], 3 * eigvec[:, -2]]
xo = [-25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 40]

# создадим сабплоты и списки с плотами для разных сабплотов для каждого атома
fig, ax = plt.subplots(3, 1)
titles = ['Минимальная энергия', 'Максимальная энергия', 'Случайная энергия']
pointsmin = []
pointsmax = []
pointsrand = []
for i in range(3):
    ax[i].axis([-30, 30, -30, 30])
    ax[i].axis('off')
    ax[i].axhline(y=0.5, color='black')
    ax[i].set_title(titles[i])
for i in range(n):
    pointsmin.append(ax[0].plot([], [], marker="o")[0])
    pointsmax.append(ax[1].plot([], [], marker="o")[0])
    pointsrand.append(ax[2].plot([], [], marker="o")[0])


# функция, генерирующая наши точки
def moving_dot(t, w, xo, u):
    j = 0
    for i in range(n):
        x = u[j][i] * np.sin(t * w[j]) + xo[i]
        y = 0.5
        pointsmin[i].set_data([x], [y])
    j = 1
    for i in range(n):
        x = u[j][i] * np.sin(t * w[j]) + xo[i]
        y = 0.5
        pointsmax[i].set_data([x], [y])
    j = 2
    for i in range(n):
        x = u[j][i] * np.sin(t * w[j]) + xo[i]
        y = 0.5
        pointsrand[i].set_data([x], [y])
    return pointsmin + pointsmax + pointsrand


# сама анимация
animation = FuncAnimation(fig, func=moving_dot, fargs=(w, xo, u), frames=np.linspace(0, 100, 1000, endpoint=False),
                          interval=10)

plt.get_current_fig_manager().window.state('zoomed')
plt.show()

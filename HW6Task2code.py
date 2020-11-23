import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return x ** 2 - 1


def fder(x):
    return 2 * x


def newton_iteration(f, fder, x0, eps=1e-5, maxiter=1000):
    """ Newton 's root finding method for f ( x )=0
    Parameters
    ----------
    f : callable
    Function f .
    fder : callable
    Derivative of f .
    x0 : float
    Initial point for iterations .
    eps : float
    Requested accuracy .
    maxiter : int
    Maximal number of iterations .
    Returns
    -------
    x : float
    Approximate root .
    niter : int
    Number of iterations .
    """
    iterations = 0
    shodimost = [x0]
    for i in range(maxiter):
        iterations += 1
        x = x0 - func(x0)/fder(x0)
        x0 = x
        shodimost.append(x0)
        if (x - 1)**2 <= eps**2:
            break
    return x, iterations, shodimost

x0 = 2
root, iterations, shodimost = newton_iteration(func, fder, x0)
shodimost = np.array(shodimost)

print("Корень: ", root)
print("Количество иттераций: ", iterations)
plt.plot(shodimost)
plt.show()
# получили, что сходимость - квадратичная

# Корень:  1.0000000464611474
# Количество иттераций:  4

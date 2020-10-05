import numpy as np
import scipy as sc

import matplotlib.pyplot as plt

#Formula para optimizar (Descenso del gradiente)
func = lambda th: np.sin(1/2 * th[0] ** 2 - 1/4 * th[1] ** 2 + 3) * np.cos(2 * th[0] + 1 - np.e ** th[1])

res = 100

_X = np.linspace(-2, 2, res)
_Y = np.linspace(-2, 2, res)

_Z = np.zeros((res, res))

for ix, x in enumerate(_X):
    for iy, y in enumerate(_Y):
        _Z[iy, ix] = func([x, y])

plt.contourf(_X, _Y, _Z, 100)
plt.colorbar()

Theta = np.random.rand(2) * 4 - 2

_T = np.copy(Theta)
h = 0.001
lr = 0.001

#Grafico de superficie
plt.plot(Theta[0], Theta[1], "o", c="white")

grad = np.zeros(2)

for _ in range(1000):
    #Derivada parcial
    for it, th in enumerate(Theta):
        _T = np.copy(Theta)
        _T[it] = _T[it] + h
        deriv = (func(_T) - func(Theta)) / h
        grad[it] = deriv
    Theta = Theta - lr * grad
    if(_ % 50 == 0):
        plt.plot(Theta[0], Theta[1], ".", c="red")
        
plt.plot(Theta[0], Theta[1], "o", c="green")
plt.show
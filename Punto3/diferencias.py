#/usr/bin/env python3
# -*- coding: utf-8 -*-

from sympy import symbols
import numpy as np
from numpy import zeros, diag


x = symbols('x')


def diferencias(x, y, n):
    '''
    (array, array, int) -> array
    Dados los n datos de una tabla (x,y) calcula sus diferencias
    divididas. Nos devuelve un array con los elementos de la
    diagonal principal, que son los coeficientes del polinomio
    de Taylor.
    '''
    T = y
    for k in range(1, n + 1):
        T[k: n] = (T[k: n] - T[k - 1]) / (x[k: n] - x[k - 1])
    return T

def polneville(x, y, x0):
    '''
    (array, array, float) -> list
    Calcula la aproximación interpolante en un punto x0 mediante el algoritmo
    de Neville. En una lista nos devuelve la aproximación final y las
    aproximaciones en cada paso en un array para poder dibujarlas.
    '''
    Q = np.zeros((len(x), len(x)), dtype=float)
    for k in range(0, len(x)):
        Q[k][0] = y[k]

    for i in range(1, len(x)):
        for j in range(1, i + 1):
            Q[i][j] = ((x0-x[i-j])*Q[i][j-1]-(x0-x[i])*Q[i-1][j-1])/(x[i]-x[i-j])

    return [Q[-1][-1], np.diag(Q, 0)]

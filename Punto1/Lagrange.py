# Interpolacion de Lagrange
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Datos
xi = [0,1,2]
fi = [10,15,5]

n = len(xi)
x = sp.Symbol('x')
# Polinomio
polinomio = 0
for i in range(0,n,1):
    #Lagrange
    termino = 1
    for j  in range(0,n,1):
        if j!=i:
            termino = termino*(x-xi[j])/(xi[i]-xi[j])
    polinomio = polinomio + termino*fi[i]
# Expande el polinomio
px = polinomio.expand()

print('Polinomio de Lagrange')
print(polinomio)
print('Expandido: ')
print(px)
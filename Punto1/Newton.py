# Interpolación Newton
import numpy as np
import matplotlib.pyplot as plt

# Datos
xi = [0,1,2]
fi = [10,15,5]


xi = np.array(xi)
fi = np.array(fi)
n = len(xi)

# Vector B en columna
B = np.array(fi)
B = fi[:,np.newaxis]

# Matriz Vandermonde D
D = np.zeros(shape=(n,n),dtype =float)
for f in range(0,n,1):
    for c in range(0,n,1):
        potencia = (n-1)-c
        D[f,c] = xi[f]**potencia

# matriz aumentada
coeficiente =  np.linalg.solve(D,B)

# Polinomio
import sympy as sp
x = sp.Symbol('x')
polinomio = 0
for i in range(0,n,1):
    potencia = (n-1)-i
    termino = coeficiente[i,0]*((x**potencia))
    polinomio = polinomio + termino

# Convierte polinomio a funcion
px = sp.lambdify(x,polinomio)


k = 100
inicio = np.min(xi)
fin = np.max(xi)
puntosx = np.linspace(inicio,fin,k)
puntosy = px(puntosx)


print('Matriz Vandermonde: ')
print(D)
print('los coeficientes del polinomio: ')
print(coeficiente)
print('Polinomio de interpolación: ')
print(polinomio)

# Grafica
plt.plot(xi,fi,'o')
plt.plot(puntosx,puntosy)
plt.show()
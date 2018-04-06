__author__ = 'tobal'

#/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from numpy import array, cos, pi
from sympy import symbols, init_printing, lambdify, horner, expand, pprint
from diferencias import diferencias, polneville
import matplotlib.pyplot as plt
from matplotlib import rcParams


rcParams['text.latex.unicode'] = True
rcParams['text.usetex'] = True
rcParams['text.latex.preamble'] = '\\usepackage{amsthm}', '\\usepackage{amsmath}', '\\usepackage{amssymb}',
'\\usepackage{amsfonts}', '\\usepackage[T1]{fontenc}', '\\usepackage[utf8]{inputenc}'

x = symbols('x')

init_printing(use_unicode=True)

datosx = np.array([0, 0.1, 0.2, 0.3, 0.4], dtype=float)
datosy = np.array([0, 0.00467884, 0.01752309, 0.03693637, 0.06155793], dtype=float)
datosy2 = datosy.copy()
diff = diferencias(datosx, datosy, len(datosx))
pprint('ALGORITMOS INTERPOLADORES DE NEVILLE.')
pprint('=================================================')
print()
pprint('Introduce el valor en el que desees interpolar: ')
interpolar = eval(input())

valorN = polneville(datosx, datosy2, interpolar)[0]
pprint('Para {0} obtenemos {1} con Neville. '.format(interpolar, valorN))

f, (ax1, ax2) = plt.subplots(1, 2)
f.set_size_inches(15, 15)
f.subplots_adjust(hspace=0)
f.suptitle(r'$ALGORITMOS\; DE NEVILLE.$', fontsize=20)
title1 = r'$Polinomio \; Interpolador \; Newton \; Grado \; n={}$'.format(len(datosx) - 1)
ax1.set_title(title1, fontsize=18)
title2 = r'$Newton\; Vs.\; Neville.\; n\; =\; {}$'.format(len(datosx))
ax2.set_title(title2, fontsize=18)
t = np.linspace(datosx[0], datosx[-1], 1000)

ax1.xaxis.label.set_fontsize(20)
ax1.yaxis.label.set_fontsize(20)
ax1.set_xlabel(r'$Datos\; x$', color='blue')
ax1.set_ylabel(r'$Datos\; y$', color='blue')

ax2.xaxis.label.set_fontsize(20)
ax2.yaxis.label.set_fontsize(20)
ax2.set_xlabel(r'$Datos\; x$', color='blue')
ax2.set_ylabel(r'$Datos\; y$', color='blue')

ax1.axis([0.0, 8.0, -2.0, 5.0])
ax2.axis([0.0, 8.0, -2.0, 5.0])

ax1.grid('on')
ax2.grid('on')

ax1.scatter(datosx, datosy2, c='r', s=70, edgecolors='r')
ax1.scatter(interpolar, valor, c='g', s=70, edgecolors='g')
ax1.plot(t, P(t), 'b-', lw=1.5)

text1 = r'$Pol.\; Newton$'
text2 = r'$Puntos\; Tabla$'
text3 = r'$P({0},\; {1})$'.format(interpolar, valor)

legend = ax1.legend([text1, text2, text3], scatterpoints=1, markerscale=1.5, shadow=True)
frame = legend.get_frame()
frame.set_facecolor('0.90')

ax2.scatter(datosx, polnewton(diff, datosx, interpolar)[1], c='r', s=70, edgecolors='r')
ax2.plot(datosx, polnewton(diff, datosx, interpolar)[1], 'r-', lw=1.5)
ax2.scatter(datosx, polneville(datosx, datosy2, interpolar)[1], c='b', s=70, edgecolors='g')
ax2.plot(datosx, polneville(datosx, datosy2, interpolar)[1], 'b-', lw=1.5)

xtcks = np.arange(0, 9)
xtckslatex = []
for i in xtcks:
    xtckslatex.append('$' + str(i) + '$')
ytcks = np.arange(-2, 6)
ytckslatex = []
for i in ytcks:
    ytckslatex.append('$' + str(i) + '$')

ax1.set_xticklabels(xtckslatex, fontsize=18)
ax1.set_yticklabels(ytckslatex, fontsize=18)

ax2.set_xticklabels(xtckslatex, fontsize=18)
ax2.set_yticklabels(ytckslatex, fontsize=18)

text21 = r'$Puntos\; Aprox.\; Newton$'
text22 = r'$Poligonal\; Aprox.\; Nevwton$'
text23 = r'$Puntos\; Aprox.\; Neville$'
text24 = r'$Poligonal\; Aprox.\; Neville$'

legend2 = ax2.legend([text22, text24, text21, text23], scatterpoints=1, markerscale = 1.5, shadow=True, loc=4)
frame2 = legend2.get_frame()
frame2.set_facecolor('0.90')

plt.show()
plt.close()
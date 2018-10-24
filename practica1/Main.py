# -*- coding: utf-8 -*-
"""
@author: Andrés Martos
@author: Darío Adrián Hernández Barroso

@grupo: 1461
@pareja: 10
"""

from Datos import Datos
import EstrategiaParticionado as ep
from itertools import izip
import numpy as np

# dataset_ballons = Datos('balloons.data')
# dataset_tictactoe = Datos('tic-tac-toe.data')
# dataset_german = Datos('german.data')

# print(dataset_ballons.datos)
# print(dataset_ballons.diccionarios)
print('\n')
# print(dataset_tictactoe.datos)
# print('\n\n')
# print(dataset_german.datos)


d = Datos('balloons.data')
print d.datos, "\n\n"
# print("\n\n SubMatriz: \n\n")
# print(d.extraeDatos([1,2,3,5,7,8]))

tablas = []
a = []

for i in range(len(d.diccionarios[-1])):
    a.append(np.array([n for n in d.datos if n[-1] == i]))
    print '\n', a[i], '\n'
    for j in range(d.datos.shape[1] - 1):
        tabla = np.array(np.unique(a[i][:, j], return_counts=True))
        tablas.append(tabla)

print('\n')


for i in range(len(tablas)):
    print tablas[i]



tablas_finales = []

for i in range((d.datos.shape[1] - 1)):
    tablas_finales.append(np.array(list(izip(tablas[i][1], tablas[(i + d.datos.shape[1] - 1)][1]))))

print('\n')


for i in range(len(tablas_finales)):
    #     if len(tablas_finales[i]) < len(d.diccionarios[-1]):
    #
    #         if tablas[i*2][0][0] == 0.0:
    #             tablas_finales[i] = np.vstack([tablas_finales[i],[4., 0.]])
    #         #el
    print tablas_finales[i]

# e = ep.ValidacionCruzada()
# particiones = e.creaParticiones(d.datos)
# print(particiones.indicesTrain)
# print(particiones.indicesTest)

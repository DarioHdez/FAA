# -*- coding: utf-8 -*-
"""
@author: Andrés Martos
@author: Darío Adrián Hernández Barroso
@grupo: 1461
@pareja: 10
"""

from Datos import Datos
from Clasificador import  ClasificadorNaiveBayes,ClasificadorVecinosProximos,ClasificadorRegresionLogistica
from EstrategiaParticionado import  ValidacionCruzada,ValidacionSimple,ValidacionBootstrap

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


d = Datos('ConjuntosDatos/example1.data')

# print("\n\n SubMatriz: \n\n")
# print(d.extraeDatos([1,2,3,5,7,8]))
e = ValidacionCruzada()
e.creaParticiones(d.datos)

d.calcularMediasDesv(d.extraeDatos(e.particiones[0].indicesTrain))
d.normalizarDatos()

print('\n')

c =ClasificadorRegresionLogistica(nEpocas=20)

print(np.mean(c.validacion(e,d,c,seed=None,laplace=False)))





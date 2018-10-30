# -*- coding: utf-8 -*-
"""
@author: Andrés Martos
@author: Darío Adrián Hernández Barroso

@grupo: 1461
@pareja: 10
"""

from Datos import Datos
from Clasificador import  ClasificadorNaiveBayes
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


d = Datos('german.data')

# print("\n\n SubMatriz: \n\n")
# print(d.extraeDatos([1,2,3,5,7,8]))
estrategiaSimple = ValidacionSimple()
estrategiaCruzada = ValidacionCruzada(10)
nBayes = ClasificadorNaiveBayes()

errorNBayes = nBayes.validacion(estrategiaSimple,d,nBayes,seed=None, laplace=True)
print("Error naive simple:\n")
print(errorNBayes[0])
errorNBayes = nBayes.validacion(estrategiaCruzada,d,nBayes,seed=None, laplace=True)
print("\nMedia de errores naive cruzada:\n")
print(np.mean(errorNBayes))

# e = ep.ValidacionCruzada()
# particiones = e.creaParticiones(d.datos)
# print(particiones.indicesTrain)
# print(particiones.indicesTest)

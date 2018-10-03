# -*- coding: utf-8 -*-
"""
@author: Andrés Martos
@author: Darío Adrián Hernández Barroso

@grupo: 1461
@pareja: 10
"""

from Datos import Datos
import EstrategiaParticionado as ep

#dataset_ballons = Datos('balloons.data')
#dataset_tictactoe = Datos('tic-tac-toe.data')
#dataset_german = Datos('german.data')

#print(dataset_ballons.datos)
#print('\n\n')
#print(dataset_tictactoe.datos)
#print('\n\n')
#print(dataset_german.datos)

d = Datos('balloons.data')
print(d.datos)
#print("\n\n SubMatriz: \n\n")
#print(d.extraeDatos([]))

e = ep.ValidacionSimple()
particiones = e.creaParticiones(d.datos)

print(particiones.indicesTrain)
print(particiones.indicesTest)


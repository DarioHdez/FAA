# -*- coding: utf-8 -*-
"""
@author: Andrés Martos
@author: Darío Adrián Hernández Barroso

@grupo: 1461
@pareja: 10
"""

from Datos import Datos
import EstrategiaParticionado as ep

dataset_ballons = Datos('balloons.data')
dataset_tictactoe = Datos('tic-tac-toe.data')
dataset_german = Datos('german.data')

print(dataset_ballons.datos)
#print(dataset_ballons.diccionarios)
print('\n\n')
print(dataset_tictactoe.datos)
print('\n\n')
print(dataset_german.datos)

# -*- coding: utf-8 -*-
from Estrategias.EstrategiaParticionado import EstrategiaParticionado
from Estrategias.Particion import Particion
import numpy
import random

class ValidacionCruzada(EstrategiaParticionado):

    def __init__(self, nfolds=10):
        self.nombreEstrategia = 'Validacion Cruzada'
        self.nfolds = nfolds
        self.particiones = []

    # Crea particiones segun el metodo de validacion cruzada.
    # El conjunto de entrenamiento se crea con las nfolds-1 particiones y el de test con la particion restante
    # Esta funcion devuelve una lista de particiones (clase Particion)
    def creaParticiones(self, datos, seed=None):
        numFilas = datos.shape[0]
        random.seed(seed)
        index = list(range(numFilas))

        random.shuffle(index)
        indexK = numFilas // self.nfolds
        lIndex = [index[i:i + indexK] for i in range(0, len(index), indexK)]
        i = 0

        while i < self.nfolds:
            particion = Particion()
            particion.indicesTest = lIndex[i]
            auxL = [x for j, x in enumerate(lIndex) if j != i]
            particion.indicesTrain = [x for subL in auxL for x in subL]
            self.particiones.append(particion)
            i += 1

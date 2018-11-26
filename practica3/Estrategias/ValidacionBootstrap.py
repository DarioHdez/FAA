# -*- coding: utf-8 -*-
from EstrategiaParticionado import EstrategiaParticionado
import numpy
import random

class ValidacionBootstrap(EstrategiaParticionado):

    def __init__(self,numeroParticiones=10):
        self.nombreEstrategia = 'Validacion Bootstrap'
        self.numeroParticiones = numeroParticiones
        self.particiones = []

    # Crea particiones segun el metodo de validacion por bootstrap.
    # Esta funcion devuelve una lista de particiones (clase Particion)
    def creaParticiones(self, datos, seed=None):

        for i in range(self.numeroParticiones):
            p = Particion()
            num = datos.shape[0]
            random.seed(seed)

            p.indicesTrain = [random.randint(0, datos.shape[0] - 1) for n in range(num)]
            p.indicesTest = [n for n in range(datos.shape[0]) if n not in p.indicesTrain]

            self.particiones.append(p)

# -*- coding: utf-8 -*-
from Estrategias.EstrategiaParticionado import EstrategiaParticionado
from Estrategias.Particion import Particion
import numpy
import random

class ValidacionSimple(EstrategiaParticionado):

    def __init__(self, numeroParticiones=10):
        self.nombreEstrategia = 'Validacion Simple'
        self.numeroParticiones = numeroParticiones;
        self.particiones = []
    # Crea particiones segun el metodo tradicional de division de los datos segun el porcentaje deseado.
    # Devuelve una lista de particiones (clase Particion)
    def creaParticiones(self, datos, seed=None):

        for i in range(self.numeroParticiones):
            p = Particion()
            num = datos.shape[0] / 2
            random.seed(seed)

            while len(p.indicesTrain) < num:
                a = random.randint(0, datos.shape[0] - 1)
                if not a in p.indicesTrain: p.indicesTrain.append(a)
            # p.indicesTrain = list({random.randint(0,datos.shape[0]-1) for n in range(num)})

            p.indicesTest = [n for n in range(datos.shape[0]) if n not in p.indicesTrain]

            self.particiones.append(p)

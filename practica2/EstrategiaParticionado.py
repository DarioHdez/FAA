# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
import random
import Datos
import numpy as np


class Particion():

    # Esta clase mantiene la lista de indices de Train y Test para cada partición del conjunto de particiones
    def __init__(self):
        self.indicesTrain = []
        self.indicesTest = []


#####################################################################################################

class EstrategiaParticionado(object):
    # Clase abstracta
    __metaclass__ = ABCMeta

    # Atributos: deben rellenarse adecuadamente para cada estrategia concreta: nombreEstrategia, numeroParticiones, listaParticiones. Se pasan en el constructor
    nombreEstrategia = ""
    numeroParticiones = 0

    @abstractmethod
    def creaParticiones(self, datos, seed=None):
        pass


#####################################################################################################

class ValidacionSimple(EstrategiaParticionado):
    def __init__(self, nfolds=10):
        self.particiones = []
    # Crea particiones segun el metodo tradicional de division de los datos segun el porcentaje deseado.
    # Devuelve una lista de particiones (clase Particion)
    def creaParticiones(self, datos, seed=None):
        self.nombreEstrategia = 'Validacion Simple'
        self.numeroParticiones = 1
        p = Particion()
        num = datos.shape[0] / 2
        random.seed(seed)

        while len(p.indicesTrain) < num:
            a = random.randint(0, datos.shape[0] - 1)
            if not a in p.indicesTrain: p.indicesTrain.append(a)
        # p.indicesTrain = list({random.randint(0,datos.shape[0]-1) for n in range(num)})

        p.indicesTest = [n for n in range(datos.shape[0]) if n not in p.indicesTrain]

        self.particiones.append(p)



#####################################################################################################
class ValidacionCruzada(EstrategiaParticionado):

    def __init__(self, nfolds=10):
        self.nfolds = nfolds
        self.particiones = []

    # Crea particiones segun el metodo de validacion cruzada.
    # El conjunto de entrenamiento se crea con las nfolds-1 particiones y el de test con la particion restante
    # Esta funcion devuelve una lista de particiones (clase Particion)
    def creaParticiones(self, datos, seed=None):
        self.nombreEstrategia = 'Validacion Cruzada'
        # self.particiones = []
        random.seed(seed)
        numFilas = datos.shape[0]
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


#####################################################################################################
class ValidacionBootstrap(EstrategiaParticionado):

    # Crea particiones segun el metodo de validacion por bootstrap.
    # Esta funcion devuelve una lista de particiones (clase Particion)
    def creaParticiones(self, datos, seed=None):
        self.nombreEstrategia = 'Validacion Bootstrap'
        p = Particion()
        num = datos.shape[0]
        random.seed(seed)

        p.indicesTrain = [random.randint(0, datos.shape[0] - 1) for n in range(num)]
        p.indicesTest = [n for n in range(datos.shape[0]) if n not in p.indicesTrain]

        self.particiones.append(p)

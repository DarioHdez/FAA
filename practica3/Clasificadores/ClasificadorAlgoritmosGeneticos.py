# -*- coding: utf-8 -*-
import numpy as np
from Estrategias.ValidacionCruzada import ValidacionCruzada

from Clasificadores.Clasificador import Clasificador
from random import randint
import numpy as np

#########################################################################

class ClasificadorAG(Clasificador):


    def __init__(self, K=1):
        super().__init__()


    def _genera_individuos(tampoblacion, num_reglas,  atributosDiscretos, k):

        individuos=[]

        for i in range(tampoblacion):
            individuo = []
            num_reglas = randint(1,num_reglas)
            for z in range(num_reglas):
                regla = [randint(0, k) for _ in range(len(atributosDiscretos) - 1)] + [randint(0, 1)]
                individuo.append(regla)

            individuos.append(individuo)

        return individuos


    def entrenamiento(self, datostrain, atributosDiscretos=None, diccionario=None, tampoblacion=100,generaciones=100,num_reglas=10,k=10):

        individuos = self._genera_individuos(tampoblacion, num_reglas,  atributosDiscretos, k)

        #calcular fitness
        #recombinar
        #mutacion
        #supervivientes
        pass

    def clasifica(self, datostest, atributosDiscretos=None, diccionario=None):
        pass



#########################################################################

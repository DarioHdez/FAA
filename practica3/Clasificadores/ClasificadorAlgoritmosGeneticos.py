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
        for i in range(generaciones):
            fitness = fitness(datostrain, individuos)
            self.update_stats(individuos, fitness)
        #recombinar
        #mutacion
        #supervivientes
        pass

    def clasifica(self, datostest, atributosDiscretos=None, diccionario=None):
        pass

    def fitness(self, datostrain, individuos):
        aciertos = 0
        datosdiscretizados = self.discretizar_elementos(datostrain)

        for dato in datosdiscretizados:
            for individuo in individuos:
                for regla in individuo:
                    if ((dato == regla).all() or ((dato[:-1] != regla[:-1]).any() and dato[-1] != regla[-1])):
                        flag = True
                        break
                if flag:
                    aciertos += 1



        return aciertos * 1. / len(datostrain)

    def discretizar_elementos(self, datostrain):
        datos_discretos = np.copy(datostrain)
        k=ceil(1+ 3.322*log10(len(datostrain)))

        for i in range(datostrain.shape[1]-1):
            xmin = min(datostrain[:, i])
            xmax = max(datostrain[:, i])
            a = np.around((xmax - xmin) / k, decimals=3)

            for j in range(datostrain.shape[0]):
                intervalo = datostrain[j, i] // a
                datos_discretos[j, i] = np.clip(intervalo, 1, k)

        return datos_discretos
#########################################################################

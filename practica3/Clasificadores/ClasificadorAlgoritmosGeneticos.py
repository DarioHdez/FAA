# -*- coding: utf-8 -*-
import numpy as np
from Estrategias.ValidacionCruzada import ValidacionCruzada
from Clases_AG.IntervalosDataSet import IntervalosDataSet
from Clases_AG.Individuo import Individuo
from Clases_AG.Regla import Regla

from Clasificadores.Clasificador import Clasificador
import numpy as np
from math import ceil

#########################################################################

class ClasificadorAG(Clasificador):


    def __init__(self, tampoblacion,numgeneraciones,maxreglas,dataset,probCruce,probMutacion):
        super().__init__()
        self.nIndividuos = tampoblacion
        self.nMaxGeneraciones = numgeneraciones
        self.nMaxReglas = maxreglas
        self.Intervalos = IntervalosDataSet(dataset.datos)
        self.nMaxReglasIniciales = 2
        self.probCruce = probCruce
        self.probMutacion = probMutacion
        self.nMiembrosElite = ceil(self.nIndividuos*0.02/2)*2


    def _genera_individuos(self,tampoblacion):
        return [Individuo(reglasIni=self.nMaxReglasIniciales,Intervalos=self.Intervalos) for n in range(tampoblacion)]

    def _transformar(self,dato):
        columnas = len(dato)-1

        for i in range(columnas):
            dato[i] = self.Intervalos.tablas[i].getIntervalo(dato[i])

    def _discretizar_elementos(self, datostrain):
        datos_discretos = np.copy(datostrain)

        for dato in datos_discretos:
            self._transformar(dato)
            # print('Dato transformado:\n\t',dato)

        return datos_discretos

    def _fitness(self, datostrain, individuos):
        aciertos = 0
        datos_discretizados = self._discretizar_elementos(datostrain)

        for individuo in individuos:
            individuo.calcula_acierto(datos_discretizados)

    def _seleccion_progenitores(self,individuos):
        total = sum([n.fitness for n in individuos])
        probabIndividuo = [n.fitness/total for n in individuos]
        print(probabIndividuo)
        progenitores = []
        for n in range(self.nIndividuos-self.nMiembrosElite):
            progenitores.append(np.random.choice(individuos,p=probabIndividuo))

        return progenitores

    def _cruce(self,progenitores):
        pass

    def _mutacion(self,descendientes):
        pass

    def entrenamiento(self, datostrain, atributosDiscretos=None, diccionario=None,laplace=None):


        # Poblacion Inicial
        individuos = self._genera_individuos(self.nIndividuos)

        # for i in individuos:
        #     print('Reglas: ',i.numReglas)
        #     for regla in i.reglas:
        #         print(regla.condiciones)
        #     print('\n')

        # Fitness
        self._fitness(datostrain=datostrain,individuos=individuos)

        # Sacamos la elite
        elite = sorted(individuos, key=lambda: in: in.fitness,reverse=True)[:self.nMiembrosElite]

        # for i in individuos:
        #     print(i.fitness)

        # Seleccion de progenitoress
        progenitores = self._seleccion_progenitores(individuos)

        # Cruce
        descendientes = self._cruce(progenitores)

        # Mutacion
        self._mutacion(descendientes)
        # for i in range(generaciones):
        #     fitness = fitness(datostrain, individuos)
        #     self.update_stats(individuos, fitness)
        #recombinar
        #mutacion
        #supervivientes
        pass

    def clasifica(self, datostest, atributosDiscretos=None, diccionario=None):
        pass



#########################################################################

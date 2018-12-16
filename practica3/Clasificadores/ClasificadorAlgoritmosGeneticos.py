# -*- coding: utf-8 -*-
import numpy as np
from Estrategias.ValidacionCruzada import ValidacionCruzada
from Clases_AG.IntervalosDataSet import IntervalosDataSet
from Clases_AG.Individuo import Individuo
from Clases_AG.Regla import Regla

from Clasificadores.Clasificador import Clasificador
import numpy as np
from math import ceil
from operator import attrgetter
from random import randint,random,seed

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
        self.Poblacion = []


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
        # print(probabIndividuo)
        progenitores = []
        for n in range(self.nIndividuos-self.nMiembrosElite):
            progenitores.append(np.random.choice(individuos,p=probabIndividuo))

        return progenitores

    def _cruce(self,progenitores):
        # descendencia = [Individuo() for n in range(len(progenitores))]
        descendencia = []
        seed()

        for (p1,p2) in zip(progenitores[::2],progenitores[1::2]):
            prob_cruce = random()
            vastago1 = Individuo(reglasIni=1,Intervalos=self.Intervalos)
            vastago2 = Individuo(reglasIni=1,Intervalos=self.Intervalos)
            # print('Is ',prob_cruce,'lower than',self.probCruce)
            print('P1 nReglas: ',p1.numReglas,'\nP2 nReglas: ',p2.numReglas)
            if len(p1.reglas) != 1 or len(p2.reglas) != 1:
                if prob_cruce <= self.probCruce:
                    corte_p1 = randint(1,p1.numReglas)
                    # if corte_p1 == 0:
                    #     corte_p2 = randint(1,p2.numReglas)
                    #     vastago1.reglas,vastago2.reglas = p1.reglas[:corte_p1]+p2.reglas[corte_p2:],p1.reglas[corte_p1:]+p2.reglas[:corte_p2]
                    # else:
                    corte_p2 = randint(1,p2.numReglas)

                    if p1.numReglas != 1 and p2.numReglas != 1 and vastago1.numReglas <=self.nMaxReglas and vastago2.numReglas <=self.nMaxReglas:
                        vastago1.reglas,vastago2.reglas = p1.reglas[:corte_p1]+p2.reglas[corte_p2:],p1.reglas[corte_p1:]+p2.reglas[:corte_p2]
                    else:
                        vastago1.reglas,vastago2.reglas= p1.reglas+p2.reglas, p1.reglas+p2.reglas
                    vastago1.numero_reglas(); vastago2.numero_reglas()
                    print('V1 nReglas: ',vastago1.numReglas,'\nV2 nReglas: ',vastago1.numReglas)
                    descendencia.append(vastago1);descendencia.append(vastago2)
                else:
                    descendencia.append(p1);descendencia.append(p2)
            else:
                descendencia.append(p1);descendencia.append(p2)

        return descendencia

    def _mutacion(self,descendientes):
        seed()
        for individuo in descendientes:
            for regla in individuo.reglas:
                for condicion in regla.condiciones:
                        if random() <= self.probMutacion:
                            entero = randint(0,self.Intervalos.tablas[0].nintervalos)


    def entrenamiento(self, datostrain, atributosDiscretos=None, diccionario=None,laplace=None):

        # Poblacion Inicial
        individuos = self._genera_individuos(self.nIndividuos)
        generacion = 0
        # for i in individuos:
        #     print('Reglas: ',i.numReglas)
        #     for regla in i.reglas:
        #         print(regla.condiciones)
        #     print('\n')
        while True:
            print('Generacion: ',generacion)
            # Fitness
            self._fitness(datostrain=datostrain,individuos=individuos)

            # Sacamos la elite
            elite = sorted(individuos, key=attrgetter('fitness'),reverse=True)[:self.nMiembrosElite]
            print('Best fitness so far: ', elite[0].fitness,'\n')
            if elite[0].fitness >= 0.95:
                break
            # for i in elite:
            #     print(i.fitness,i.numReglas)
            # for i in individuos:
            #     print(i.fitness)

            # Seleccion de progenitoress
            progenitores = self._seleccion_progenitores(individuos)
            # print('Numero Elites: ',len(elite))
            # print('Numero progenitores: ',len(progenitores))
            # Cruce
            descendientes = self._cruce(progenitores)
            # print('Numero descendientes: ',len(descendientes))
            # Mutacion
            self._mutacion(descendientes)
            # for i in range(generaciones):
            #     fitness = fitness(datostrain, individuos)
            #     self.update_stats(individuos, fitness)

            supervivientes = descendientes+elite
            individuos = supervivientes
            # print(len(supervivientes))
            if generacion >= self.nMaxGeneraciones:
                break
            else:
                generacion += 1

        self.Poblacion = individuos

    def clasifica(self, datostest, atributosDiscretos=None, diccionario=None):
        pass



#########################################################################

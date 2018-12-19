# -*- coding: utf-8 -*-
import numpy as np
from Estrategias.ValidacionCruzada import ValidacionCruzada
from Clases_AG.IntervalosDataSet import IntervalosDataSet
from Clases_AG.Individuo import Individuo
from Clases_AG.Regla_numerica import Regla_numerica

from Clasificadores.Clasificador import Clasificador
from copy import deepcopy
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
        # self.nMaxReglasIniciales = 2
        self.probCruce = probCruce
        self.probMutacion = probMutacion
        self.nMiembrosElite = ceil(self.nIndividuos*0.02/2)*2
        self.Poblacion = []
        self.mejoresndividuos=[]
        self.mejorindividuo=0
        self.mejoresFitness = []
        self.mediaFitnesPoblacion = []


    def _genera_individuos(self,tampoblacion):
        return [Individuo(reglasIni=self.nMaxReglas,Intervalos=self.Intervalos) for n in range(tampoblacion)]

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
        # print('Total: ',total)
        probabIndividuo = [n.fitness/total for n in individuos]

        # print(np.array(probabIndividuo))
        # print(probabIndividuo)
        progenitores = []
        for n in range(self.nIndividuos-self.nMiembrosElite):
            progenitores.append(np.random.choice(individuos,p=probabIndividuo))

        probabProg = [n.fitness/total for n in progenitores]
        # print(np.array(probabProg))
        # print('\n\n')
        return progenitores

    def _cruce(self,progenitores):
        # descendencia = [Individuo() for n in range(len(progenitores))]
        descendencia = []
        seed()

        for (p1,p2) in zip(progenitores[::2],progenitores[1::2]):
            prob_cruce = random()
            # print('Random devuelve: ',prob_cruce)
            vastago1 = Individuo(reglasIni=1,Intervalos=self.Intervalos)
            vastago2 = Individuo(reglasIni=1,Intervalos=self.Intervalos)
            # print('Is ',prob_cruce,'lower than',self.probCruce)
            # print('P1 nReglas: ',p1.numReglas,'\nP2 nReglas: ',p2.numReglas)
            if len(p1.reglas) != 1 or len(p2.reglas) != 1:
                if prob_cruce <= self.probCruce:
                    # print('Cruce')
                    corte = randint(1,min(p1.numReglas,p2.numReglas))
                    # if corte == 0:
                    #     corte_p2 = randint(1,p2.numReglas)
                    #     vastago1.reglas,vastago2.reglas = p1.reglas[:corte]+p2.reglas[corte_p2:],p1.reglas[corte:]+p2.reglas[:corte_p2]
                    # else:
                    # corte = randint(1,p2.numReglas)

                    if vastago1.numReglas <= self.nMaxReglas and vastago2.numReglas <= self.nMaxReglas:
                        vastago1.reglas,vastago2.reglas = p1.reglas[:corte]+p2.reglas[corte:],p1.reglas[corte:]+p2.reglas[:corte]
                    else:
                        vastago1.reglas,vastago2.reglas= p1.reglas+p2.reglas, p1.reglas+p2.reglas

                    vastago1.numero_reglas(); vastago2.numero_reglas()
                    # print('V1 nReglas: ',vastago1.numReglas,'\nV2 nReglas: ',vastago1.numReglas)
                    descendencia.append(vastago1);descendencia.append(vastago2)
                else:
                    descendencia.append(p1);descendencia.append(p2)
            else:
                descendencia.append(p1);descendencia.append(p2)

        return descendencia

    def _mutacion(self,descendientes):
        seed()
        for individuo in descendientes:
            if random() <= self.probMutacion and individuo.numReglas < self.nMaxReglas:
                individuo.reglas.append(Regla_numerica(self.Intervalos))
            for regla in individuo.reglas:
                for condicion in regla.condiciones:
                        if random() <= self.probMutacion:
                            # print('Muto')
                            condicion = randint(0,self.Intervalos.tablas[0].nintervalos)


    # def _seleccion_supervivientes(self,individuos,num_super=5):
    #     fitness=[]
    #     for ind in individuos:
    #         fitness.append(ind.fitness)
    #
    #     index_mejores = np.array(fitness).argsort()[-num_super:][::-1]
    #
    #     mejores_padres = np.array(individuos)[index_mejores].tolist()
    #     return mejores_padres

    def selecionar_mejor_individuo(self):
        # fitness = []
        # for ind in individuos:
        #     fitness.append(ind.fitness)
        #
        # mejor_individuo = individuos[fitness.index(max(fitness))]
        # # fitness_medio = sum(fitness) / len(individuos)
        #
        # self.mejoresndividuos.append(mejor_individuo)
        return sorted(self.Poblacion, key=attrgetter('fitness'),reverse=True)[0]

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

            # print('Generacion: ',generacion)
            # Fitness
            self._fitness(datostrain=datostrain,individuos=individuos)

            # self._selecionar_mejor_individuo(individuos)

            # print('Mejor de Generacion',generacion,self.mejoresndividuos[generacion].fitness)

            # Sacamos la elite
            elite = sorted(individuos, key=attrgetter('fitness'),reverse=True)[:self.nMiembrosElite]
            copias = []
            for el in elite:
                copias.append(deepcopy(el))
            self.mejoresFitness.append(elite[0].fitness)

            total = 0
            for i in individuos:
                total += i.fitness

            self.mediaFitnesPoblacion.append(total/self.nIndividuos)

            # print('Fitness de la raza superior: ',elite[0].fitness)
           # print('Best fitness so far: ', elite[0].fitness,'\n')
            if elite[0].fitness >= 0.95:
                print('Fitness superior a 0.95,', elite[0].fitness)
                break
            # for i in elite:
            #     print(i.fitness)
            # for i in individuos:
            #     print(i.fitness,i.numReglas)

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

            # supervivientes=self._seleccion_supervivientes(individuos,5)
            supervivientes=descendientes+copias

            print('Generacion: ',generacion,'\n\tBest fitness: ', elite[0].fitness)

            # print(len(supervivientes))
            if generacion >= self.nMaxGeneraciones:
                print('Max generaciones alcanzada.\n\tBest fitness: ', elite[0].fitness)
                break
            else:
                generacion += 1

            individuos = supervivientes

        self.Poblacion = individuos
        self.selecionar_mejor_individuo()
        # self.mejorindividuo=self.mejoresndividuos[-1]




    def clasifica(self, datostest, atributosDiscretos=None, diccionario=None):

        datos_discretizados = self._discretizar_elementos(datostest)
        Ario = sorted(self.Poblacion, key=attrgetter('fitness'),reverse=True)[0]
        print('Fitness Ario: ',Ario.fitness)
        return Ario.prediccion_test(datostest)


#########################################################################

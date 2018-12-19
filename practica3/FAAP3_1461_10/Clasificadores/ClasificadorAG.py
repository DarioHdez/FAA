# -*- coding: utf-8 -*-
import numpy as np
from Estrategias.ValidacionCruzada import ValidacionCruzada
from Clases_AG.IntervalosDataSet import IntervalosDataSet
from Clases_AG.Individuo import Individuo
from Clases_AG.Regla_binaria import Regla_binaria
from Clases_AG.Regla_numerica import Regla_numerica
from Clases_AG.Regla import Regla

from Clasificadores.Clasificador import Clasificador
from copy import deepcopy
import numpy as np
from math import ceil
from operator import attrgetter
from random import randint,random,seed

#########################################################################

class ClasificadorAG(Clasificador):

    def __init__(self, tampoblacion,numgeneraciones,maxreglas,dataset,probCruce,probMutacion,tipoRegla=Regla_numerica):
        assert isinstance(tipoRegla,object), "Me tienes que pasar un tipo de regla que exista (Regla_numerica, Regla_binaria)"
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
        self.tipoRegla = tipoRegla


    def _genera_individuos(self,tampoblacion,tipoRegla):
        return [Individuo(reglasIni=self.nMaxReglas,Intervalos=self.Intervalos,tipoRegla=tipoRegla) for n in range(tampoblacion)]

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
        # print('Fitness total de poblacion: ',total)
        # if total == 0: total += 0.01
        probabIndividuo = [n.fitness/total for n in individuos]

        # print(np.array(probabIndividuo))
        # print(probabIndividuo)
        progenitores = []
        for n in range(self.nIndividuos-self.nMiembrosElite):
            progenitores.append(np.random.choice(individuos,p=probabIndividuo))

        # probabProg = [n.fitness/total for n in progenitores]
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

                    vastago1.reglas,vastago2.reglas = p1.reglas[:corte]+p2.reglas[corte:],p1.reglas[corte:]+p2.reglas[:corte]

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
            for regla in individuo.reglas:
                    regla.mutar(self.probMutacion)

    def selecionar_mejor_individuo(self):
        return sorted(self.Poblacion, key=attrgetter('fitness'),reverse=True)[0]

    def entrenamiento(self, datostrain, atributosDiscretos=None, diccionario=None,laplace=None):

        # Poblacion Inicial
        individuos = self._genera_individuos(self.nIndividuos,self.tipoRegla)
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

            print('Generacion: ',generacion,'\tBest fitness: ', elite[0].fitness)

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

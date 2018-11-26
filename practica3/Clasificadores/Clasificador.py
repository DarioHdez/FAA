# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
import sys
from functools import reduce

from Estrategias import EstrategiaParticionado, ValidacionSimple,ValidacionCruzada,ValidacionBootstrap
import operator
import numpy as np
from scipy.special import expit


class Clasificador(object):
    # Clase abstracta
    __metaclass__ = ABCMeta

    # Metodos abstractos que se implementan en casa clasificador concreto
    @abstractmethod
    # datosTrain: matriz numpy con los datos de entrenamiento
    # atributosDiscretos: array bool con la indicatriz de los atributos nominales
    # diccionario: array de diccionarios de la estructura Datos utilizados para la codificacion
    #  de variables discretas
    def entrenamiento(self, datosTrain, atributosDiscretos, diccionario):
        pass

    @abstractmethod
    # devuelve un numpy array con las predicciones
    def clasifica(self, datosTest, atributosDiscretos, diccionario):
        pass

    # Obtiene el numero de aciertos y errores para calcular la tasa de fallo
    # TODO: implementar
    def error(self, datos, pred):
        # Aqui se compara la prediccion (pred) con las clases reales y se calcula el error
        errores = 0
        Elems = datos.shape[0]

        if Elems != pred.shape[0]:
            pass

        for i in range(Elems):
            if datos[i][-1] != pred[i]:
                errores += 1

        return (errores / float(Elems))

    # Realiza una clasificacion utilizando una estrategia de particionado determinada
    def validacion(self, particionado, dataset, clasificador, seed=None, laplace=False,normalizacion=False):
        # Creamos las particiones siguiendo la estrategia llamando a particionado.creaParticiones
        particionado.creaParticiones(dataset.datos, None)
        numPart = particionado.numeroParticiones
        dataset_diccionario = dataset.diccionarios
        dataset_atributos_discretos = dataset.nominalAtributos
        errores = []

        if normalizacion:
            _calcularMediasDesv(datostrain=dataset.extraeDatos(particionado.particiones[-1].indicesTrain))
            _normalizarDatos(dataset)

        for i in range(numPart):
            clasificador.entrenamiento(datostrain=dataset.extraeDatos(particionado.particiones[i].indicesTrain),atributosDiscretos=dataset_atributos_discretos, diccionario=dataset_diccionario, laplace=laplace)

            pred = clasificador.clasifica(datostest=dataset.extraeDatos(particionado.particiones[i].indicesTest),atributosDiscretos=dataset_atributos_discretos, diccionario=dataset_diccionario)

            errores.append(clasificador.error(datos=dataset.extraeDatos(particionado.particiones[i].indicesTest),pred=pred))

            err = clasificador.error(datos=dataset.extraeDatos(particionado.particiones[i].indicesTest), pred=pred)

            errores.append(err)

        return errores;


    def _calcularMediasDesv(datostrain):
        indices = range(len(self.nominalAtributos))
        indices_continuos = [n for n in indices if not self.nominalAtributos[n]]

        self.medias = [0]*len(self.nominalAtributos)
        self.desviaciones = [0]*len(self.nominalAtributos)

        for i in range(len(self.nominalAtributos)):
            if i in indices_continuos:

                column = np.array(datostrain[:,i])

                self.medias[i] = np.mean(column)
                self.desviaciones[i] = np.std(column)
            else:
                self.medias[i] = None
                self.desviaciones[i] = None

    def _normalizarDatos(datos=None):
        for i in range(len(self.medias)):
            if not self.medias[i] == None:
                column = np.array(self.datos[:,i])

                media_atributo = self.medias[i]
                desviacion_atributo = self.desviaciones[i]

                normalized_data = []

                # # Normalizamos cada dato
                for j in list(column):
                    normalized_data.append((j - media_atributo)/desviacion_atributo)

                self.datos[:,i] = normalized_data

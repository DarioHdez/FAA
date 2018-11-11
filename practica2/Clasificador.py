# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
import sys
from functools import reduce

import EstrategiaParticionado
import math
import operator
import numpy as np


class Clasificador(object):
    # Clase abstracta
    __metaclass__ = ABCMeta

    # Metodos abstractos que se implementan en casa clasificador concreto
    @abstractmethod
    # TODO: esta funcion deben ser implementadas en cada clasificador concreto
    # datosTrain: matriz numpy con los datos de entrenamiento
    # atributosDiscretos: array bool con la indicatriz de los atributos nominales
    # diccionario: array de diccionarios de la estructura Datos utilizados para la codificacion
    # de variables discretas
    def entrenamiento(self, datosTrain, atributosDiscretos, diccionario):
        pass

    @abstractmethod
    # TODO: esta funcion deben ser implementadas en cada clasificador concreto
    # devuelve un numpy array con las predicciones
    def clasifica(self, datosTest, atributosDiscretos, diccionario):
        pass

    # Obtiene el numero de aciertos y errores para calcular la tasa de fallo
    # TODO: implementar
    def error(self, datos, pred):
        # Aqui se compara la prediccion (pred) con las clases reales y se calcula el error

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
    # TODO: implementar esta funcion
    def validacion(self, particionado, dataset, clasificador, seed=None, laplace=False):
        # Creamos las particiones siguiendo la estrategia llamando a particionado.creaParticiones
        particionado.creaParticiones(dataset.datos, None)
        numPart = particionado.numeroParticiones # Esto va a petar muy fuerte
        dataset_diccionario = dataset.diccionarios
        dataset_atributos_discretos = dataset.nominalAtributos
        errores = []
        # Validacion Simple
        # falta poner argumentos
        if particionado.nombreEstrategia == "Validacion Simple" or particionado.nombreEstrategia == "Validacion Bootstrap":
            clasificador.entrenamiento(datostrain = dataset.extraeDatos(particionado.particiones[0].indicesTrain),atributosDiscretos=dataset_atributos_discretos, diccionario=dataset_diccionario,laplace=laplace)

            pred = clasificador.clasifica(datostest=dataset.extraeDatos(particionado.particiones[0].indicesTest),atributosDiscretos=dataset_atributos_discretos, diccionario=dataset_diccionario)

            errores.append(clasificador.error(datos=dataset.extraeDatos(particionado.particiones[0].indicesTest),pred=pred))

        elif (particionado.nombreEstrategia == "Validacion Cruzada"):

            for i in range(particionado.nfolds):
                clasificador.entrenamiento(datostrain=dataset.extraeDatos(particionado.particiones[i].indicesTrain),atributosDiscretos=dataset_atributos_discretos, diccionario=dataset_diccionario, laplace=laplace)

                pred = clasificador.clasifica(datostest=dataset.extraeDatos(particionado.particiones[i].indicesTest),atributosDiscretos=dataset_atributos_discretos, diccionario=dataset_diccionario)

                errores.append(clasificador.error(datos=dataset.extraeDatos(particionado.particiones[i].indicesTest),pred=pred))

                err = clasificador.error(datos=dataset.extraeDatos(particionado.particiones[i].indicesTest), pred=pred)

                errores.append(err)


        return errores;

        # - Para validacion cruzada: en el bucle hasta nv entrenamos el clasificador con la particion de train i
        # y obtenemos el error en la particion de test i
        # - Para validacion simple (hold-out): entrenamos el clasificador con la particion de train
        # y obtenemos el error en la particion test


##############################################################################

class ClasificadorNaiveBayes(Clasificador):
    dicc_atributos = {}
    dicc_clases = {}
    dicc_verosimilitudes = {}

    # TODO: implementar
    def entrenamiento(self, datostrain, atributosDiscretos, diccionario, laplace=None):

        numElem = datostrain.shape[0]
        lista_verosimilitudes = [] # listaCont
        lista_indices_nominales = [] # listaIndices
        tablas_laplace = []
        clases = {}
        atributos = {}

        indices_atrib_discretos = []
#        num_clases = len(diccionario[-1].keys())

        for i in range(datostrain.shape[1] -1):

            atributos.update({i:{}}) # inicializamos el diccinario del atributo i (columnas)

            # {0:{'media':{False: x, True: y}, 'varianza':{False: z, True: w}}, 1}

            if not atributosDiscretos[i]: # atributos continuos
                atributos[i].update({'media':{}})
                atributos[i].update({'varianza':{}})

                for key,value in diccionario[-1].items(): # para cada una de nuestras clases
                    # rellenamos la lista con las filas de cada clase
                    lista_verosimilitudes = [datostrain[j][i] for j in range(numElem) if datostrain[j][-1] == value]
                    atributos[i]['media'].update({value:np.mean(lista_verosimilitudes)}) # hacemos la media de apariciones
                    atributos[i]['varianza'].update({value:np.std(np.array(lista_verosimilitudes))})

            else: # atributos discretos

                for key,value in diccionario[i].items():
                    atributos[i].update({value:{}})

                    for key2,value2 in diccionario[-1].items(): # para cada una de nuestras clases
                        lista_indices_nominales = [j for j in range(numElem) if datostrain[j][-1] == value2 and datostrain[j][-1] == value]

                        if laplace and not lista_indices_nominales: # preparamos laplace
                            tablas_laplace.append(i) # i es cada una de nuestra columnas
                        atributos[i][value].update({value2:len(lista_indices_nominales)})

        # Hacemos la correcion de laplace
        if laplace:
            for j in tablas_laplace: # para cada tabla en la que hace falta laplace
                for key, value in atributos[j].items(): # para cada columna en la que hace falta laplace
                    for key2,value2 in atributos[j][key].items(): # para cada media y varianza
                        atributos[j][key][key2] += 1


        for i in range(numElem):
            clase = datostrain[i][-1]
            if (clase not in clases.keys()):
                clases[clase] = 1
            else:
                clases[clase] += 1


        self.dicc_atributos = atributos
        self.dicc_clases = clases

    # TODO: implementar
    def clasifica(self, datostest, atributosDiscretos, diccionario):
        prioris = {}
        probabilidad_clase = {}
        probabilidades = []
        probabilidad_atributo = []
        numElem = datostest.shape[0]
        total_clases = sum(list(self.dicc_clases.values())) # sumo todas las apariciones de todas las clases

        for key,value in self.dicc_clases.items():
            prioris.update({key: (value / total_clases)})

        for i in range(len(datostest)):
            probabilidad_clase.update({i:{}})

            for key,value in self.dicc_clases.items():
                for j in range(datostest.shape[1]-1) :
                    if 'media' in self.dicc_atributos[j].keys():
                        media = self.dicc_atributos[j]['media'][key]
                        varianza = self.dicc_atributos[j]['varianza'][key]
                        probabilidad_atributo.append(gauss(media,varianza,datostest[i][j]))
                    else:
                        probabilidad_atributo.append(self.dicc_atributos[j][datostest[i][j]][key] / float(value))

                probabilidades.append(math.log1p(reduce(lambda x, y: x*y, probabilidad_atributo) * prioris[key]))
                probabilidad_clase[i][key] = probabilidades
                probabilidades = []
                probabilidad_atributo = []

        predicciones = np.zeros(numElem)
        #predicciones = [max(probabilidad_clase[i].items(),key=operator.itemgetter(1))[0] for i in range(numFilas)]

        for i in range(numElem):
            predicciones[i] = max(probabilidad_clase[i].items(), key=operator.itemgetter(1))[0]
        return predicciones


def gauss(media,varianza, num):
    if varianza == 0:
        varianza += math.pow(10,-6)

    exponente = - (math.pow((num-media), 2) / (2*varianza))
    base = 1 / math.sqrt(2*math.pi*varianza)
    return base*math.pow(math.e,exponente)


#########################################################################

class ClasificadorVecinosProximos(Clasificador):
    k = 1
    train = 0
    indicestrain = np.array(())

    def __init__(self, K):
        self.k = K

    def entrenamiento(self, datostrain, atributosDiscretos=None, diccionario=None, laPlace=True):
        self.indicestrain = datostrain

    # TODO: implementar
    def clasifica(self, datostest, atributosDiscretos=None, diccionario=None):
        k = self.k
        distancia = []

        for i, dato in enumerate(datostest):
            if (len(dato) == len(atributosDiscretos)):
                dato = dato[0:-1]

            dist_euclidea = lambda x, y: (x - y) ** 2
            distancias = map(lambda punto: [(sum(map(dist_euclidea, dato, punto[0:-1]))) ** 0.5, punto[-1]],self.indicestrain)


            distancias = np.array((distancias))
            distancias = distancias[distancias[:, 0].argsort()]

      
            claseGanadora = np.unique(distancias[range(k), 1], return_counts=True)
            clase = claseGanadora[0][np.argmax(claseGanadora[0])]
            distancia.append(clase)
        distancia = np.array((distancia))
        return distancia

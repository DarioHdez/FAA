from Clasificadores.Clasificador import Clasificador
import numpy as np
import math
from functools import reduce
import operator

class ClasificadorNaiveBayes(Clasificador):

    def gauss(media,varianza, num):
        if varianza == 0:
            varianza += math.pow(10,-6)

        exponente = - (math.pow((num-media), 2) / (2*varianza))
        base = 1 / math.sqrt(2*math.pi*varianza)
        return base*math.pow(math.e,exponente)

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

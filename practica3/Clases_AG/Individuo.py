# -*- coding: utf-8 -*-
from Clases_AG.Regla import Regla
from Clases_AG.Regla_numerica import Regla_numerica
from Clases_AG.Regla_binaria import Regla_binaria
from random import randint
import numpy as np
from collections import Counter

class Individuo(object):


    def __init__(self,reglasIni,Intervalos,tipoRegla=Regla_numerica):
        self.numReglas = randint(1,reglasIni)
        self.reglas = [tipoRegla(Intervalos) for n in range(self.numReglas)]
        self.fitness = 0


    def calcula_acierto(self,datostrain):
        aciertos = 0
        numdatos = datostrain.shape[0]

        # count = Counter(list(datostrain[:,-1]))
        # priori = int(count.most_common()[0][0])

        # predicciones = {'ceros':0,'unos':0}
        votantes = []
        # mayoritario = 2

        for dato in datostrain:
            # print('Dato a comparar:\t',dato)
            for regla in self.reglas:
                if regla.comparar(dato):
                    # print('Regla acierta')
                    votantes.append(regla.conclusion)

            if votantes:
                count = Counter(votantes)
                # print(count)
                mayoritario = int(count.most_common()[0][0])

                if mayoritario == dato[-1]:
                    aciertos += 1

            votantes = []
            # aciertos = 0

            # predicciones['ceros'] = 0
            # predicciones['unos'] = 0

        self.fitness = np.around(aciertos*1./numdatos,3)

    def numero_reglas(self):
        self.numReglas = len(self.reglas)

    def prediccion_test(self,datostest):

        numdatos = datostest.shape[0]

        votantes = []
        prediction = []

        for dato in datostest:
            for regla in self.reglas:
                if regla.comparar(dato):
                    votantes.append(regla.conclusion)

            if votantes:
                count = Counter(votantes)
                # print(count)
                mayoritario = int(count.most_common()[0][0])

                prediction.append(mayoritario)
            else:
                count = Counter(list(datostest[:,-1]))
                priori = int(count.most_common()[0][0])
                prediction.append(priori)
            votantes = []

        return np.array(prediction)

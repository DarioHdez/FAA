# -*- coding: utf-8 -*-
from Clases_AG.Regla import Regla
from random import randint
import numpy as np
from collections import Counter

class Individuo(object):

    def __init__(self,reglasIni,Intervalos):
        self.numReglas = randint(1,reglasIni)
        self.reglas = [Regla(Intervalos) for n in range(self.numReglas)]
        self.fitness = 0


    def calcula_acierto(self,datostrain):
        aciertos = 0
        numdatos = datostrain.shape[0]


        count = Counter(list(datostrain[:,-1]))
        priori = int(count.most_common()[0][0])

        predicciones = {'ceros':0,'unos':0}
        mayoritario = 2

        for dato in datostrain:
            for regla in self.reglas:
                if regla.comparar(dato):
                    predicciones['unos'] += 1
                else:
                    predicciones['ceros'] += 1

            if predicciones['ceros'] > predicciones['unos']:
                mayoritario = 0
            elif predicciones['ceros'] < predicciones['unos']:
                mayoritario = 1
            else:
                mayoritario = priori

            if mayoritario == dato[-1]:
                aciertos += 1

            predicciones['ceros'] = 0
            predicciones['unos'] = 0

        self.fitness = aciertos*1./numdatos

    def numero_reglas(self):
        self.numReglas = len(self.reglas)

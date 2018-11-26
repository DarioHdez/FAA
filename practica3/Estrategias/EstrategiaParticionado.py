# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

class EstrategiaParticionado(object):
    # Clase abstracta
    __metaclass__ = ABCMeta

    # Atributos: deben rellenarse adecuadamente para cada estrategia concreta: nombreEstrategia, numeroParticiones, listaParticiones. Se pasan en el constructor

    @abstractmethod
    def creaParticiones(self, datos, seed=None):
        pass

#####################################################################################################

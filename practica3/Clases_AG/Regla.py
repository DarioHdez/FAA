from abc import ABCMeta, abstractmethod
import sys
import numpy as np

class Regla_numerica(object):

    # Clase abstracta
    __metaclass__ = ABCMeta

    @abstractmethod
    def comparar(self,dato):
        pass

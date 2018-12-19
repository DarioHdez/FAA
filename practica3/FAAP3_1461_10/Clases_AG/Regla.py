# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
import sys
import numpy as np

class Regla(object):

    # Clase abstracta
    __metaclass__ = ABCMeta

    @abstractmethod
    def comparar(self,dato):
        pass

    @abstractmethod
    def mutar(self,probM):
        pass

import numpy as np
from math import log10,ceil
from Clases_AG.Intervalo import Intervalo
# from Intervalo import Intervalo

class IntervalosClase(object):

    def __init__(self,columna):
        self.nintervalos = ceil(1+ 3.322*log10(len(columna)))
        xmax = max(columna)
        xmin = min(columna)
        amplitudIntervalo = int((self.xmax - self.xmin)/self.k)

        self.Intervalos = []

        old = xmin+amplitudIntervalo
        Id = 1
        self.Intervalos.append(Intervalo(Id,xmin,old))

        for n in range(self.nintervalos-2):
            Id += Id
            new = old+amplitudIntervalo
            i = Intervalo(Id,old,new)
            old = new

        self.Intervalos.append(Intervalo(self.nintervalos,old,xmax))
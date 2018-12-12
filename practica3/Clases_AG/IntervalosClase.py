import numpy as np
from math import log10,ceil
from Clases_AG.Intervalo import Intervalo
# from Intervalo import Intervalo

class IntervalosClase(object):

    def __init__(self,columna):
        self.nintervalos = ceil(1+ 3.322*log10(len(columna)))
        self.Intervalos = []
        xmax = max(columna)
        xmin = min(columna)
        amplitudIntervalo = np.around((xmax - xmin)/self.nintervalos,decimals=3)

         # print('Amplitud de clase: ',amplitudIntervalo)


        old = xmin+amplitudIntervalo
        Id = 1
        self.Intervalos.append(Intervalo(Id,xmin,old))
        # print(self.Intervalos[0].maximo,self.Intervalos[0].minimo)

        for n in range(self.nintervalos-2):
            Id += 1
            new = old+amplitudIntervalo
            i = Intervalo(Id,old,new)
            old = new
            self.Intervalos.append(i)

        self.Intervalos.append(Intervalo(self.nintervalos,old,xmax))


    def getIntervalo(self,valor):
        for intervalo in self.Intervalos:
            # print(intervalo.minimo,intervalo.maximo)
            if intervalo.esMio(valor):
                return intervalo.id

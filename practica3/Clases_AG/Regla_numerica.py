import numpy as np
from Clases_AG.Regla import Regla
from random import random,randint

class Regla_numerica(Regla):

    def __init__(self,intervalosDataset):
        super().__init__()
        self.tam = intervalosDataset.ntablas
        self.condiciones = []
        self.conclusion =  np.random.randint(0,2)
        self._nintervalos = intervalosDataset.tablas[0].nintervalos

        for i in range(self.tam):
            self.condiciones.append(np.random.choice([0,np.random.randint(1,self._nintervalos+1)],p=[0.90,0.1]))
            # self.condiciones.append(0)


    def comparar(self,dato):
        l = [True if self.condiciones[i] == dato[i] or self.condiciones[i] == 0 else False for i in range(self.tam)]

        return all(l)


    def mutar(self,probM):
        for cond in self.condiciones:
            if random() <= probM:
                cond = randint(0,self._nintervalos)

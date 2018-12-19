import numpy as np
from Clases_AG.IntervalosClase import IntervalosClase
from Clases_AG.Intervalo import Intervalo

class IntervalosDataSet(object):

    def __init__(self,dataset):
        super().__init__()
        self.ntablas = dataset.shape[1]-1
        self.tablas = []

        for n in range(self.ntablas):
            t = IntervalosClase(np.take(dataset,n,axis=1))
            self.tablas.append(t)

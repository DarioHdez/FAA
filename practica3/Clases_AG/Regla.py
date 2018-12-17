import numpy as np

class Regla_numerica(object):

    def __init__(self,IntervalosDataset):
        self.tam = intervalosDataset.ntablas
        self.condiciones = []
        self.conclusion =  np.random.randint(0,2)


    @abstract
    def comparar(self,dato):
        pass

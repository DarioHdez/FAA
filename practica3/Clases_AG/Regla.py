import numpy as np

class Regla(object):

    def __init__(self,intervalosDataset):
        self.tam = intervalosDataset.ntablas

        self.condiciones = []
        self.conculsion =  np.random.randint(0,1)

        for i in range(self.tam):
            self.condiciones.append(np.random.randint(1,intervalosDataset[i].nintervalos))


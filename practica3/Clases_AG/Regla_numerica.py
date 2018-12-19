import numpy as np
# from Clases_AG.Regla import Regla

class Regla_numerica(object):

    def __init__(self,intervalosDataset):
        # super().__init__()
        self.tam = intervalosDataset.ntablas
        self.condiciones = []
        self.conclusion =  np.random.randint(0,2)

        for i in range(self.tam):
            self.condiciones.append(np.random.choice([0,np.random.randint(1,intervalosDataset.tablas[i].nintervalos+1)],p=[0.90,0.1]))
            # self.condiciones.append(0)


    def comparar(self,dato):
        l = [True if self.condiciones[i] == dato[i] or self.condiciones[i] == 0 else False for i in range(self.tam)]

        return all(l)

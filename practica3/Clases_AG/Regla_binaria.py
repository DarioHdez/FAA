import numpy as np
import Regla

class Regla_binaria(Regla):

    def __init__(self,intervalosDataset):

        super().__init__(intervalosDataset)

        for i in range(self.tam):
            self.condiciones.append(np.random.randint(2,size=intervalosDataset.tablas[i].nintervalos))

    def comparar(self,dato):

        l = [True if self.condiciones[i][dato] == 1 or self.condiciones[i] == 0 else False for i in range(self.tam)]

        # print(l,'\n')

        # return all(l)
        return True

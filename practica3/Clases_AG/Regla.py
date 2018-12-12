import numpy as np

class Regla(object):

    def __init__(self,intervalosDataset):
        self.tam = intervalosDataset.ntablas

        self.condiciones = []
        self.conclusion =  1

        for i in range(self.tam):
            self.condiciones.append(np.random.choice([0,np.random.randint(1,intervalosDataset.tablas[i].nintervalos+1)],p=[0.9,0.1]))
            # self.condiciones.append(0)


    def comparar(self,dato):
        l = [True if self.condiciones[i] == dato[i] or self.condiciones[i] == 0 else False for i in range(self.tam)]

        # print(l,'\n')

        return all(l)

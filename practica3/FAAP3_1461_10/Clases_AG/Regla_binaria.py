import numpy as np
from random import random
from Clases_AG.Regla import Regla
# import Regla

class Regla_binaria(Regla):

    def __init__(self,intervalosDataset):

        super().__init__()
        self.tam = intervalosDataset.ntablas
        self.condiciones = []
        self.conclusion =  np.random.randint(0,2)

        # print(intervalosDataset.tablas[0].nintervalos)

        for i in range(self.tam):
            self.condiciones.append(list(np.random.randint(2,size=intervalosDataset.tablas[i].nintervalos)))
            # cond = []
            # for j in range(intervalosDataset.tablas[i].nintervalos):
                # cond.append(np.random.choice([0,1],p=[0.10,0.90]))
                # cond.append(1)

            # self.condiciones.append(cond)


    def comparar(self,dato):

        # l = [True if self.condiciones[i][dato[]] == 1 or self.condiciones[i] == 0 else False for i in range(self.tam)]
        l = []
        # print(self.condiciones[0][0],dato[0])
        # print(len(dato),self.tam,len(self.condiciones),len(self.condiciones[0]))

        for num in range(len(dato)-1):
            for i in range(self.tam):
                # print(self.condiciones[i],self.condiciones[i][int(dato[num]-1)],int(dato[num]-1))
                if self.condiciones[i][int(dato[num]-1)]:
                    # print('Acierta')
                    l.append(True)
                else:
                    l.append(False)

        # print(l,'\n')

        return all(l)

    def mutar(self,probM):
        for cond in self.condiciones:
            for i in cond:
                if random() <= probM:
                    i = int(not i)

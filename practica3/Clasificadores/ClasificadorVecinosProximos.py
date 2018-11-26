from Clasificador import Clasificador

class ClasificadorVecinosProximos(Clasificador):

    def __init__(self, K=1):
        self.indicestrain = np.array(())
        self.k = K

    @staticmethod
    def distanciaEuclidea(instance1, instance2, length):
        distance = 0
        for x in range(length):
            distance += pow((instance1[x] - instance2[x]), 2)
        return distance**0.5


    def entrenamiento(self, datostrain, atributosDiscretos=None, diccionario=None, laplace=True):
        self.indicestrain = datostrain

    def clasifica(self, datostest, atributosDiscretos=None, diccionario=None):
        k = self.k
        distancia = []
        clases = {}
        clasificacion = []

        length = len(datostest[0]) - 1
        # Para cada punto
        for j in range(datostest.shape[0]):
            # Sacamos los vecinos
            for i in range(len(self.indicestrain)):
                dist = self.distanciaEuclidea(datostest[j],self.indicestrain[i], length)
                distancia.append((self.indicestrain[i], dist))

            distancia.sort(key=operator.itemgetter(1))

            k_vecinos = []
            for x in range(k):
                k_vecinos.append(distancia[x][0])

            # Sacamos la clase predominante de k_vecinos
            for i in range(len(k_vecinos)):

                clase = k_vecinos[i][-1]

                if not clase in clases:
                    clases[clase] = 1
                else:
                    clases[clase] += 1

            decision = max(clases.items(),key=operator.itemgetter(1))[0]

            clasificacion.append(decision)

        return np.array(clasificacion)

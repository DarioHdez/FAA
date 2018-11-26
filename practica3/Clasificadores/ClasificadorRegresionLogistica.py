from Clasificador import Clasificador

class ClasificadorRegresionLogistica(Clasificador):

    def __init__(self, nEpocas=0, cteAprendizaje=1):
        self.nEpocas = nEpocas
        self.cteAprendizaje = cteAprendizaje
        self.W = None

    def entrenamiento(self, datostrain, atributosDiscretos=None, diccionario=None,laplace=None):
        numColumnas = datostrain.shape[1]

        #generamos vector aleatorio entre -0.5 y 0..5
        W = np.random.uniform(low=-0.5, high=0.5, size=(numColumnas,))

        for e in range(self.nEpocas):

            for i in range(datostrain.shape[0]):
                #añadimos un 1 al inicio
                x = np.insert(datostrain[i], 0, 1)

                #vector por nuestra muestra
                wx = np.dot(W, x[:-1])

                #sigmoidal del resultado
                sigmo=  expit(wx)

                W = W - (self.cteAprendizaje * (sigmo - (1 - datostrain[-1]))) *x[:-1]

            self.W=W

    def clasifica(self, datostest, atributosDiscretos=None, diccionario=None):

        numFilas = datostest.shape[0]
        numColumnas = datostest.shape[1]

        ret = []

        for dato in datostest:

            x = np.ones(3)
            x[1:3] = dato[0:2]

            wx = np.dot(self.W, x)

            sigmo = expit(wx)

            if sigmo >= 0.5:
                ret.append(1)
            else: ret.append(0)


        return np.array(ret)

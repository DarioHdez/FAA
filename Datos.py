import numpy as np


class Datos(object):
    TiposDeAtributos = ('Continuo', 'Nominal')
    tipoAtributos = []
    nombreAtributos = []
    nominalAtributos = []
    datos = []
    diccionarios = []


    def __init__(self, nombreFichero):
        fichero = open(nombreFichero, 'r')

        # Leemos las 3 primeras lineas del fichero
        nDatos = int(fichero.readline())
        self.nombreAtributos = fichero.readline().strip().split(",")
        self.tipoAtributos = fichero.readline().strip().split(",")

        columnas = len(self.tipoAtributos) # Variable auxiliar

        # Comprobamos que todos los atributos sean nominales o continuos
        for atributo in Datos.tipoAtributos:
            if atributo == 'Continuo':
                Datos.nominalAtributos.append(False)
            elif atributo == 'Nominal':
                Datos.nominalAtributos.append(True)
            else:
                raise (ValueError)

        contador = [0]*(columnas)
        fila = [0]*(columnas)  # Variable auxiliar en la que vamos creando las filas
        self.datos = np.empty((0,columnas),np.float32) #Reestructuramos los datos para las columnas del fichero

        self.diccionarios = [{} for i in  range(len(self.tipoAtributos))]

        for i in range(nDatos):
            linea = fichero.readline().split('\n')[0].split(",")  # linea = [data,data,data....]
            for j in range(len(linea)):
                if self.tipoAtributos[j] == 'Nominal':
                    if not linea[j] in self.diccionarios[j]:    # Comprobamos si ese data esta en un diccionario
                        self.diccionarios[j].update({linea[j]:contador[j]})   # Añadimos en caso de que no esté
                        contador[j] += 1

                    fila[j] = self.diccionarios[j].get(linea[j])       # Añadimos a la fila el valor del diccionario
                else:
                    fila[j] = linea[j]    # Si es una variable continua la añadimos directamente

            self.datos = np.vstack([self.datos,[fila]])   # Añadimos la fila a datos

    def extraeDatos(self,idx):

        pass

dataset = Datos('balloons.data')

print(dataset.datos)


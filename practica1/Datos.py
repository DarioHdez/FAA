# -*- coding: utf-8 -*-
import numpy as np


class Datos(object):
    TiposDeAtributos = ('Continuo', 'Nominal')

    def __init__(self, nombreFichero):
        self.tipoAtributos = []
        self.nombreAtributos = []
        self.nominalAtributos = []
        self.datos = []
        self.diccionarios = []
        fichero = open(nombreFichero, 'r')
        columnas_dic = []


        # Leemos las 3 primeras lineas del fichero
        nDatos = int(fichero.readline())
        self.nombreAtributos = fichero.readline().strip().split(",")
        self.tipoAtributos = fichero.readline().strip().split(",")

        columnas = len(self.tipoAtributos) # Variable auxiliar

        # Comprobamos que todos los atributos sean nominales o continuos
        for atributo in self.tipoAtributos:
            if atributo == 'Continuo':
                self.nominalAtributos.append(False)
            elif atributo == 'Nominal':
                self.nominalAtributos.append(True)
            else:
                raise (ValueError)

        contador = [0]*(columnas)
        fila = [0]*(columnas)  # Variable auxiliar en la que vamos creando las filas
        self.datos = np.empty((0,columnas),np.float32) #Reestructuramos los datos para las columnas del fichero

        self.diccionarios = [{} for i in  range(len(self.tipoAtributos))]

        # Correción para poner los diccionarios, ahora esta todo en orden (fallo 13)
        matriz = np.array([x.split('\n')[0].split(",")   for x in fichero.readlines()])
        for i in range(columnas):
            col = sorted(set(matriz[:,i]))

            if self.nominalAtributos[i] == True :
                for j in col:
                    self.diccionarios[i].update({j:col.index(j)})

        #Cerramos el fichero (fallo 2)
        fichero.close()

        with open(nombreFichero) as f:
            f.readline()
            f.readline()
            f.readline()

            for i in range(nDatos):
                linea = f.readline().split('\n')[0].split(",")  # linea = [data,data,data....]
                for j in range(len(linea)):
                    if self.tipoAtributos[j] == 'Nominal':
                        fila[j] = self.diccionarios[j].get(linea[j])       # Anyadimos a la fila el valor del diccionario
                    else:
                        fila[j] = float(linea[j])    # Si es una variable continua la anyadimos directamente, convirtiendola a float primero (correción del fallo 12)

                self.datos = np.vstack([self.datos,[fila]])   # Anyadimos la fila a datos



    def extraeDatos(self,idx):
        filas = len(idx)
        columnas = self.datos.shape[1]

        data = np.zeros((filas,columnas))
        #ret = [ [] for i in self.datos if i in idx ]

        for i in range(filas):
            data[i] = self.datos[idx[i]]

        return data

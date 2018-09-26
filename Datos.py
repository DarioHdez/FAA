import numpy as np


class Datos(object):
    TiposDeAtributos = ('Continuo', 'Nominal')
    tipoAtributos = []
    nombreAtributos = []
    nominalAtributos = []
    datos = np.array([],dtype=np.int32)
    # Lista de diccionarios. Uno por cada atributo.
    diccionarios = []
    # TODO: procesar el fichero para asignar correctamente las variables
    # tipoAtributos, nombreAtributos, nominalAtributos, datos y diccionarios
    def __init__(self, nombreFichero):
        fichero = open(nombreFichero, 'r')

        nDatos = int(fichero.readline())
        self.nombreAtributos = fichero.readline().strip().split(",")
        self.tipoAtributos = fichero.readline().strip().split(",")

        for atributo in Datos.tipoAtributos:
            if atributo == 'Continuo':Datos.nominalAtributos.append(False)
            elif atributo == 'Nominal':Datos.nominalAtributos.append(True)
            else:
                raise (ValueError)

        contador = [0]*(len(self.tipoAtributos))
        fila = [0]*(len(self.tipoAtributos))

        self.diccionarios = [{} for i in  range(len(self.tipoAtributos))]

        for i in range(nDatos):
            linea = fichero.readline().split('\n')[0].split(",")  # linea = [data,data,data....]
            for j in range(len(linea)):
                if self.tipoAtributos[j] == 'Nominal':
                    if not linea[j] in self.diccionarios[j]:
                        self.diccionarios[j].update({linea[j]:contador[j]})
                        contador[j] += 1

                    fila[j] = self.diccionarios[j].get(linea[j])
                else:
                    fila[j] = linea[j]

            self.datos = np.append(self.datos)



        print(self.diccionarios)
        #self.datos = [fichero.readline().split('\n')[0].split(',') for i in range(nDatos)]

        #diccionario
        #for i in range(len(self.tipoAtributos)):




    def extraeDatos(self,idx):

        pass
dataset = Datos('balloons.data')

print(dataset.datos)


import numpy as np


class Datos(object):
    TiposDeAtributos = ('Continuo', 'Nominal')
    tipoAtributos = []
    nombreAtributos = []
    nominalAtributos = []
    datos = np.array([],dtype = np.int32)
    # Lista de diccionarios. Uno por cada atributo.
    diccionarios = []
    print ("hola")
    # TODO: procesar el fichero para asignar correctamente las variables tipoAtributos, nombreAtributos, nominalAtributos, datos y diccionarios
    def __init__(self, nombreFichero):
        fichero = open(nombreFichero, 'r')

        nDatos = int(fichero.readline())
        nombreAtributos = fichero.readline().strip().split(",")
        tipoAtributos = fichero.readline().strip().split(",")
        print(nombreAtributos)
        print(tipoAtributos)
        for atributo in Datos.tipoAtributos:
            if atributo == 'Continuo':Datos.nominalAtributos.append(False)
            elif atributo == 'Nominal':Datos.nominalAtributos.append(True)
            else:
                raise (ValueError)

        datos = [fichero.readline().split('\n')[0].split(',') for i in range(nDatos)]
        print(datos)
        #diccionario










        pass
    def extraeDatos(self,idx):

        pass
dataset = Datos('tic-tac-toe.data')

print(dataset.datos)


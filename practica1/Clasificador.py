# -*- coding: utf-8 -*-
from abc import ABCMeta,abstractmethod
import sys
import EstrategiaParticionado
import Datos


class Clasificador(object):

  # Clase abstracta
  __metaclass__ = ABCMeta

  # Metodos abstractos que se implementan en casa clasificador concreto
  @abstractmethod
  # TODO: esta funcion deben ser implementadas en cada clasificador concreto
  # datosTrain: matriz numpy con los datos de entrenamiento
  # atributosDiscretos: array bool con la indicatriz de los atributos nominales
  # diccionario: array de diccionarios de la estructura Datos utilizados para la codificacion
  # de variables discretas
  def entrenamiento(self,datosTrain,atributosDiscretos,diccionario):
    pass


  @abstractmethod
  # TODO: esta funcion deben ser implementadas en cada clasificador concreto
  # devuelve un numpy array con las predicciones
  def clasifica(self,datosTest,atributosDiscretos,diccionario):
    pass


  # Obtiene el numero de aciertos y errores para calcular la tasa de fallo
  # TODO: implementar
  def error(self,datos,pred):
    # Aqui se compara la prediccion (pred) con las clases reales y se calcula el error

    # Aqui se compara la prediccion (pred) con las clases reales y se calcula el error
    errores = 0
    Elems = datos.shape[0]

    if Elems != pred.shape[0]:
      return Elems

    for i in range(Elems):
      if datos[i] != pred[i]:
        errores += 1

    porc_err = errores /Elems
    return porc_err


  # Realiza una clasificacion utilizando una estrategia de particionado determinada
  # TODO: implementar esta funcion
  def validacion(self,particionado,dataset,clasificador,seed=None):
    # Creamos las particiones siguiendo la estrategia llamando a particionado.creaParticiones
    particionado.creaParticiones(dataset.datos, None)
    numPart = particionado.numeroParticiones
    errores = []
    # Validacion Simple
    #falta poner argumentos
    if (particionado.nombreEstrategia == "Validacion Simple"):
      clasificador.entrenamiento()
      pred = clasificador.clasifica()
      err = clasificador.error()
      errores.append(err)
    elif (particionado.nombreEstrategia == "Validacion Cruzada"):

      for i in range(numPart):
        clasificador.entrenamiento()
        pred = clasificador.clasifica()
        err = clasificador.error()
        errores.append(err)

    return errores;

    # - Para validacion cruzada: en el bucle hasta nv entrenamos el clasificador con la particion de train i
    # y obtenemos el error en la particion de test i
    # - Para validacion simple (hold-out): entrenamos el clasificador con la particion de train
    # y obtenemos el error en la particion test



##############################################################################

class ClasificadorNaiveBayes(Clasificador):

  diccAtributos = {}
  diccClases = {}
  diccVerosimilitudes = {}


  # TODO: implementar
  def entrenamiento(self,datostrain,atributosDiscretos,diccionario,laplace=None):
    numElem = datostrain.shape[0]
    clases = {}
    atributos = {}
    Indices = []
    LaPlace = []
    Cont = []
    







  # TODO: implementar
  def clasifica(self,datostest,atributosDiscretos,diccionario):
    pass


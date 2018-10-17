# -*- coding: utf-8 -*-
from abc import ABCMeta,abstractmethod
import random
import Datos
import numpy as np

class Particion():

  # Esta clase mantiene la lista de indices de Train y Test para cada partición del conjunto de particiones
  def __init__(self):
    self.indicesTrain=[]
    self.indicesTest=[]

#####################################################################################################

class EstrategiaParticionado(object):

  # Clase abstracta
  __metaclass__ = ABCMeta

  # Atributos: deben rellenarse adecuadamente para cada estrategia concreta: nombreEstrategia, numeroParticiones, listaParticiones. Se pasan en el constructor

  @abstractmethod
  def creaParticiones(self,datos,seed=None):
    pass


#####################################################################################################

class ValidacionSimple(EstrategiaParticionado):

  # Crea particiones segun el metodo tradicional de division de los datos segun el porcentaje deseado.
  # Devuelve una lista de particiones (clase Particion)
  def creaParticiones(self,datos,seed=None):
    p = Particion()
    num = datos.shape[0]/2
    random.seed(seed)

    while len(p.indicesTrain) < num:
        a =random.randint(0,datos.shape[0]-1)
        if not a in p.indicesTrain: p.indicesTrain.append(a)
    #p.indicesTrain = list({random.randint(0,datos.shape[0]-1) for n in range(num)})

    p.indicesTest = [n for n in range(datos.shape[0]) if n not in p.indicesTrain]

    return p

#####################################################################################################
class ValidacionCruzada(EstrategiaParticionado):

  # Crea particiones segun el metodo de validacion cruzada.
  # El conjunto de entrenamiento se crea con las nfolds-1 particiones y el de test con la particion restante
  # Esta funcion devuelve una lista de particiones (clase Particion)
  def creaParticiones(self,datos,seed=None):
    p= Particion()
    num = datos.shape[0]/3 # check this
    random.seed(seed)

    #Vamos a trabajar con los indices directamente
    lista=datos.tolist()
    listaInd = [n for n in range(len(lista))]
    random.shuffle(listaInd)

    p.indicesTrain = [ n for n in listaInd if listaInd.index(n) <= num*2]
    p.indicesTest = [ n for n in listaInd if n not in p.indicesTrain]

    return p


#####################################################################################################
class ValidacionBootstrap(EstrategiaParticionado):

  # Crea particiones segun el metodo de validacion por bootstrap.
  # Esta funcion devuelve una lista de particiones (clase Particion)
  def creaParticiones(self,datos,seed=None):
    p = Particion()
    num = datos.shape[0]
    random.seed(seed)

    p.indicesTrain = [random.randint(0,datos.shape[0]-1) for n in range(num)]
    p.indicesTest = [n for n in range(datos.shape[0]) if n not in p.indicesTrain]

    return p

from abc import ABCMeta,abstractmethod
import random
import Datos

class Particion():

  # Esta clase mantiene la lista de índices de Train y Test para cada partición del conjunto de particiones
  def __init__(self):
    self.indicesTrain=[]
    self.indicesTest=[]

#####################################################################################################

class EstrategiaParticionado(object):
  
  # Clase abstracta
  __metaclass__ = ABCMeta
  
  # Atributos: deben rellenarse adecuadamente para cada estrategia concreta: nombreEstrategia, numeroParticiones, listaParticiones. Se pasan en el constructor 
  
  @abstractmethod
  # TODO: esta funcion deben ser implementadas en cada estrategia concreta  
  def creaParticiones(self,datos,seed=None):
    pass
  

#####################################################################################################

class ValidacionSimple(EstrategiaParticionado):
  
  # Crea particiones segun el metodo tradicional de division de los datos segun el porcentaje deseado.
  # Devuelve una lista de particiones (clase Particion)
  # TODO: implementar
  def creaParticiones(self,datos,seed=None):
    p = Particion()
    num = datos.shape[0]/2

    random.seed(seed)

    while len(p.indicesTrain) < num:
        a =random.randint(0,datos.shape[0]-1)

        if not a in p.indicesTrain: p.indicesTrain.append(a)

    for i in range(datos.shape[0]):
        if not i in p.indicesTrain:
            p.indicesTest.append(i)

    return p


      
      
#####################################################################################################      
class ValidacionCruzada(EstrategiaParticionado):
  
  # Crea particiones segun el metodo de validacion cruzada.
  # El conjunto de entrenamiento se crea con las nfolds-1 particiones y el de test con la particion restante
  # Esta funcion devuelve una lista de particiones (clase Particion)
  # TODO: implementar
  def creaParticiones(self,datos,seed=None):   
    random.seed(seed)
    pass
    

#####################################################################################################      
class ValidacionBootstrap(EstrategiaParticionado):
  
  # Crea particiones segun el metodo de validacion por bootstrap.
  # Esta funcion devuelve una lista de particiones (clase Particion)
  # TODO: implementar
  def creaParticiones(self,datos,seed=None):   
    random.seed(seed)
    pass

    

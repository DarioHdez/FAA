# -*- coding: utf-8 -*-
from Datos.Datos import Datos
from Estrategias.Particion import Particion
from Estrategias.EstrategiaParticionado import EstrategiaParticionado
from Estrategias.ValidacionSimple import ValidacionSimple
from Estrategias.ValidacionCruzada import ValidacionCruzada
from Estrategias.ValidacionBootstrap import ValidacionBootstrap
from Clasificadores.Clasificador import Clasificador
from Clasificadores.ClasificadorNaiveBayes import ClasificadorNaiveBayes
from Clasificadores.ClasificadorVecinosProximos import ClasificadorVecinosProximos
from Clasificadores.ClasificadorRegresionLogistica import ClasificadorRegresionLogistica
import numpy as np


print('All loaded')

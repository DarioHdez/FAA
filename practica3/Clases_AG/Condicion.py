

class Condicion(object):

    def __init__(self,valor,Tabla):
        (self.minimo,self.maximo),self.intervalo = Tabla.getIntervalo(valor)


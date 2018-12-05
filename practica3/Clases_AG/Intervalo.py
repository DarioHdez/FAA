

class Intervalo(object):

    def __init__(self,Id,maximo,minimo):
        self.id = Id
        self.maximo = maximo
        self.minimo = minimo


    def esMio(self,valor):
        if valor <= self.maximo and valor >= self.minimo: return True
        else: return False
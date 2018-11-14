import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier

from Datos import Datos

print ("VECINOS PROXIMOS SCIKIT")
print ("---------------------------------")
print ("Procesando fichero: example3.data")
print ("---------------------------------")
dataset = Datos('ConjuntosDatos/example1.data')
X=dataset.datos[:,:-1]
Y=dataset.datos[:,-1]
for i in [1,3,5,11,21,51]:
    print ("K = ",  i)
    resultado = KNeighborsClassifier(n_neighbors=i)
    cvs = cross_val_score(resultado, X,Y, cv=10)
    print ("Media erronea del fichero: ",(1-np.mean((cvs))), "con Desviacion Tipica (std) = ", (np.std((cvs))))
    print ("---------------------------------")
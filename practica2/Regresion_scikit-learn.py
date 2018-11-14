#import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np
from sklearn.linear_model import LogisticRegression
import Datos

from sklearn.model_selection import cross_val_score
from Datos import Datos


print ("REGRESION LOGISTICA SCIKIT")
print ("---------------------------------")
print ("Procesando fichero: example1.data")
print ("---------------------------------")
dataset = Datos("./ConjuntosDatos/example1.data")

X=dataset.datos[:,:-1]
Y=dataset.datos[:,-1]

h = .02  # step size in the mesh

logreg = LogisticRegression(C=1e5) # Creando el modelo

logreg.fit(X, Y) #ajustando el modelo

# we create an instance of Neighbours Classifier and fit the data.
logreg.fit(X, Y)

cvs = cross_val_score(logreg, X,Y, cv=20)
print ("Media erronea del fichero: example3.data  :",(1-np.mean((cvs))), "con Desviacion Tipica (std) = ", (np.std((cvs))))
print ("---------------------------------")


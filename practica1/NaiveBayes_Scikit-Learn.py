
import numpy as np
from Datos import Datos
from sklearn import preprocessing
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import ShuffleSplit


dataset = Datos('german.data')
validacionSimple = ShuffleSplit(len(dataset.datos), test_size=.25, random_state=0)
validacionCruzada=9
#Validacion Simple Laplace
print ("Validacion Simple con Laplace")

atributos =preprocessing.OneHotEncoder(categorical_features=dataset.nominalAtributos[:-1],sparse=False)
X = atributos.fit_transform(dataset.datos[:,:-1])
Y=dataset.datos[:,-1]

clf = MultinomialNB(alpha=1, class_prior=None, fit_prior=True)
clf.fit(X, Y)

cvs = cross_val_score(clf, X,Y,cv=validacionSimple)
print ("La media de error de Naive Bayes es :",(1-np.mean((cvs))), "con Desviacion Tipica = " , (np.std((cvs))))



print ("Validacion Cruzada con Laplace")


atributos =preprocessing.OneHotEncoder(categorical_features=dataset.nominalAtributos[:-1],sparse=False)
X = atributos.fit_transform(dataset.datos[:,:-1])
Y=dataset.datos[:,-1]

clf = MultinomialNB(alpha=1, class_prior=None, fit_prior=True)
clf.fit(X, Y)

cvs = cross_val_score(clf, X,Y,cv=validacionCruzada)
print ("La media de error de Naive Bayes es :",(1-np.mean((cvs))), "con Desviacion Tipica = " , (np.std((cvs))))



#Validacion Simple Laplace
print ("Validacion Simple sin Laplace")

atributos =preprocessing.OneHotEncoder(categorical_features=dataset.nominalAtributos[:-1],sparse=False)
X = atributos.fit_transform(dataset.datos[:,:-1])
Y=dataset.datos[:,-1]

clf = MultinomialNB(alpha=0, class_prior=None, fit_prior=True)
clf.fit(X, Y)

cvs = cross_val_score(clf, X,Y,cv=validacionSimple)
print ("La media de error de Naive Bayes es :",(1-np.mean((cvs))), "con Desviacion Tipica = " , (np.std((cvs))))



print ("Validacion Cruzada sin Laplace")

atributos =preprocessing.OneHotEncoder(categorical_features=dataset.nominalAtributos[:-1],sparse=False)
X = atributos.fit_transform(dataset.datos[:,:-1])
Y=dataset.datos[:,-1]

clf = MultinomialNB(alpha=0, class_prior=None, fit_prior=True)
clf.fit(X, Y)

cvs = cross_val_score(clf, X,Y,cv=validacionCruzada)
print ("La media de error de Naive Bayes es :",(1-np.mean((cvs))), "con Desviacion Tipica = " , (np.std((cvs))))







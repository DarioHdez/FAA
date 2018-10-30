
import numpy as np
from Datos import Datos
from sklearn import preprocessing
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import ShuffleSplit


dataset = Datos('balloons.data')
validacionSimple = ShuffleSplit(len(dataset.datos), test_size=.25, random_state=0)
validacionCruzada=2
#Validacion Simple Laplace


atributos =preprocessing.OneHotEncoder(categorical_features=dataset.nominalAtributos[:-1],sparse=False)
X = atributos.fit_transform(dataset.datos[:,:-1])
Y=dataset.datos[:,-1]

clf = MultinomialNB(alpha=1, class_prior=None, fit_prior=True)
clf.fit(X, Y)

cvs = cross_val_score(clf, X,Y,cv=validacionSimple)
print ("La media de error de Naive Bayes  usando Validacion Simple con Laplace es :",(1-np.mean((cvs))))





atributos =preprocessing.OneHotEncoder(categorical_features=dataset.nominalAtributos[:-1],sparse=False)
X = atributos.fit_transform(dataset.datos[:,:-1])
Y=dataset.datos[:,-1]

clf = MultinomialNB(alpha=1, class_prior=None, fit_prior=True)
clf.fit(X, Y)

cvs = cross_val_score(clf, X,Y,cv=validacionCruzada)
print ("La media de error de Naive Bayes  usando Validacion Cruzada con Laplace es :",(1-np.mean((cvs))),)



#Validacion Simple Laplace


atributos =preprocessing.OneHotEncoder(categorical_features=dataset.nominalAtributos[:-1],sparse=False)
X = atributos.fit_transform(dataset.datos[:,:-1])
Y=dataset.datos[:,-1]

clf = MultinomialNB(alpha=0, class_prior=None, fit_prior=True)
clf.fit(X, Y)

cvs = cross_val_score(clf, X,Y,cv=validacionSimple)
print ("La media de error de Naive Bayes es  usando Validacion Simple sin Laplace es ::",(1-np.mean((cvs))))



print ("Validacion Cruzada sin Laplace")

atributos =preprocessing.OneHotEncoder(categorical_features=dataset.nominalAtributos[:-1],sparse=False)
X = atributos.fit_transform(dataset.datos[:,:-1])
Y=dataset.datos[:,-1]

clf = MultinomialNB(alpha=1, class_prior=None, fit_prior=True)
clf.fit(X, Y)

cvs = cross_val_score(clf, X,Y,cv=validacionCruzada)
print ("La media de error de Naive Bayes  usando Validacion Cruzada con Laplace es :",(1-np.mean((cvs))))







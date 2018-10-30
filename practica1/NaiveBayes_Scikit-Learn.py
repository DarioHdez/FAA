import numpy as np
from Datos import Datos
from sklearn import preprocessing
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import ShuffleSplit


dataset = Datos('german.data')
validacionSimple = ShuffleSplit(len(dataset.datos), test_size=.25, random_state=0)
validacionCruzada=2
#Validacion Simple Laplace
file = open("Scikit-Learn","w")


atributos =preprocessing.OneHotEncoder(categorical_features=dataset.nominalAtributos[:-1],sparse=False)
X = atributos.fit_transform(dataset.datos[:,:-1])
Y=dataset.datos[:,-1]

clf = MultinomialNB(alpha=1, class_prior=None, fit_prior=True)
clf.fit(X, Y)

cvs = cross_val_score(clf, X,Y,cv=validacionSimple)
file.write ("La media de error de Naive Bayes  usando Validacion Simple con Laplace es :" + str((1-np.mean((cvs))) )+ " con Desviacion Tipica = " +  str((np.std((cvs)))) + "\n")





atributos =preprocessing.OneHotEncoder(categorical_features=dataset.nominalAtributos[:-1],sparse=False)
X = atributos.fit_transform(dataset.datos[:,:-1])
Y=dataset.datos[:,-1]

clf = MultinomialNB(alpha=1, class_prior=None, fit_prior=True)
clf.fit(X, Y)

cvs = cross_val_score(clf, X,Y,cv=validacionCruzada)
file.write ("La media de error de Naive Bayes  usando Validacion Cruzada con Laplace es :" +str((1-np.mean((cvs))))+" con Desviacion Tipica = " +  str((np.std((cvs)))) + "\n")



#Validacion Simple Laplace


atributos =preprocessing.OneHotEncoder(categorical_features=dataset.nominalAtributos[:-1],sparse=False)
X = atributos.fit_transform(dataset.datos[:,:-1])
Y=dataset.datos[:,-1]

clf = MultinomialNB(alpha=0, class_prior=None, fit_prior=True)
clf.fit(X, Y)

cvs = cross_val_score(clf, X,Y,cv=validacionSimple)
file.write("La media de error de Naive Bayes es  usando Validacion Simple sin Laplace es :" +str((1-np.mean((cvs))))+" con Desviacion Tipica = " +  str((np.std((cvs)))) + "\n")



file.write("Validacion Cruzada sin Laplace")

atributos =preprocessing.OneHotEncoder(categorical_features=dataset.nominalAtributos[:-1],sparse=False)
X = atributos.fit_transform(dataset.datos[:,:-1])
Y=dataset.datos[:,-1]

clf = MultinomialNB(alpha=0, class_prior=None, fit_prior=True)
clf.fit(X, Y)

cvs = cross_val_score(clf, X,Y,cv=validacionCruzada)
file.write ("La media de error de Naive Bayes  usando Validacion Cruzada con Laplace es :"+ str((1-np.mean((cvs)))) +" con Desviacion Tipica = " +  str((np.std((cvs)))) + "\n")

file.close()

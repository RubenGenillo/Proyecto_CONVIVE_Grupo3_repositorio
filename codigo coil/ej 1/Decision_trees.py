#Conseguir un dataset con una dimension reducida, aplica la tecnica de seleccion de variables basada en arbol de decision mediante als importancias de cada variable (Decision Trees Importances)
#Filtra el tablón para quedarnos solamente con las variables que aglutinan hasta el 95% de la información que se requiere para estumar la variable objetivo
#random_state = 100

from sklearn import tree
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

# Cargar el csv
df = pd.read_csv('codigo coil/clusterizado_2.csv', sep=';')

# Separar en X e y
X = df.drop(['cluster'], axis=1)
y = df['cluster']

# Separar en train y test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

# Crear el modelo
model = DecisionTreeClassifier(random_state=100)

# Entrenar el modelo
model.fit(X_train, y_train)

# Predecir con el modelo
y_pred = model.predict(X_test)

# Calcular la precisión del modelo
print('Precisión del modelo: ', accuracy_score(y_test, y_pred))

# Mostrar las importancias de cada variable
importances = model.feature_importances_

# Mostrar las importancias de cada variable en un gráfico de cajas
plt.boxplot(importances)

# Mostrar el gráfico
plt.show()

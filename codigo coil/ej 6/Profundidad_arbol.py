# Aplicar XGBoost Classifier con los parámetros por defecto y reportar el accuracy score sobre el conjunto de test sobre la base NMT 1

import xgboost as xgb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Cargar el csv
df = pd.read_csv('codigo coil/clusterizado_1.csv', sep=';')

# Separar en X e y
X = df.drop(['cluster'], axis=1)
y = df['cluster']

# Separar en train y test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Crear el modelo
model_2 = xgb.XGBClassifier()

# Entrenar el modelo
model_2.fit(X_train, y_train)

# Predecir con el modelo
y_pred = model_2.predict(X_test)

# Calcular la precisión del modelo
print('Precisión del modelo: ', accuracy_score(y_test, y_pred))

# Mostrar las importancias de cada variable
importances = model_2.feature_importances_

#Calcular la profundidad del arbol generado
print('Profundidad del arbol: ', model_2.get_booster().get_dump()[0].count('\t'))
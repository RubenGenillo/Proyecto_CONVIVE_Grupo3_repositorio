import xgboost as xgb
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, classification_report

# Cargar el dataset
data = load_iris()
X, y = data.data, data.target

# Separar en train y test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

# Definir los rangos de valores para cada hiperparámetro
n_estimators_range = [100, 200, 300, 400, 500]
max_depth_range = range(6, 21, 2)
learning_rate_range = [0.01, 0.1, 0.3, 0.5]

# Inicializar las listas para almacenar los resultados de precisión
accuracy_results = []
f1_score_results = []

# Calcular la precisión para diferentes valores de n_estimators y max_depth
for n_estimators in n_estimators_range:
    accuracy_scores = []
    f1_scores = []
    for max_depth in max_depth_range:
        # Crear el modelo
        model = xgb.XGBClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=100)
        # Entrenar el modelo
        model.fit(X_train, y_train)
        # Predecir con el modelo
        y_pred = model.predict(X_test)
        # Calcular la precisión y f1-score
        accuracy = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred, average='weighted')
        accuracy_scores.append(accuracy)
        f1_scores.append(f1)
    # Guardar los resultados de precisión para este valor de n_estimators
    accuracy_results.append(accuracy_scores)
    f1_score_results.append(f1_scores)

# Crear la gráfica de la curva de complejidad para el número de árboles
plt.figure(figsize=(10,6))
for i in range(len(max_depth_range)):
    plt.plot(n_estimators_range, [row[i] for row in accuracy_results], label='max_depth: {}'.format(max_depth_range[i]))
plt.title('Model Complexity Curve (n_estimators)')
plt.xlabel('Number of Trees')
plt.ylabel('Accuracy')
plt.legend()
plt.show()



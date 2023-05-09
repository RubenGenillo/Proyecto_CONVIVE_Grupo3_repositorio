import xgboost as xgb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, f1_score, classification_report
from sklearn.model_selection import learning_curve

# Cargar el csv
df = pd.read_csv('codigo coil/clusterizado_1.csv', sep=';')

# Separar en X e y
X = df.drop(['cluster'], axis=1)
y = df['cluster']

# Separar en train y test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

# Crear el modelo con los valores por defecto
model_default = xgb.XGBClassifier(random_state=100)

# Entrenar el modelo por defecto
model_default.fit(X_train, y_train)

# Predecir con el modelo por defecto
y_pred_default = model_default.predict(X_test)

# Calcular la precisión y el F1-score del modelo por defecto
accuracy_default = accuracy_score(y_test, y_pred_default)
f1_default = f1_score(y_test, y_pred_default, average='weighted')
classification_report_default = classification_report(y_test, y_pred_default, zero_division=0)

print('Precisión del modelo por defecto: ', accuracy_default)
print('F1-score del modelo por defecto: ', f1_default)
print('Classification report del modelo por defecto:\n', classification_report_default)

# Curva de complejidad
param_grid = {
    'n_estimators': [100, 200, 300, 400, 500],
    'max_depth': range(6, 21, 2),
    'learning_rate': [0.01, 0.1, 0.3, 0.5],
}

grid = GridSearchCV(estimator=model_default, param_grid=param_grid, cv=3, n_jobs=-1, verbose=2)
grid.fit(X_train, y_train)

print("Mejores hiperparámetros encontrados: ", grid.best_params_)
print("Mejor score de validación cruzada: {:.2f}".format(grid.best_score_))

# Crear un nuevo modelo con los valores óptimos de los hiperparámetros
model_optimized = xgb.XGBClassifier(
    n_estimators=grid.best_params_['n_estimators'],
    max_depth=grid.best_params_['max_depth'],
    learning_rate=grid.best_params_['learning_rate'],
    random_state=100)

# Entrenar el modelo optimizado
model_optimized.fit(X_train, y_train)

# Predecir con el modelo optimizado
y_pred_optimized = model_optimized.predict(X_test)

# Calcular la precisión y el F1-score del modelo optimizado
accuracy_optimized = accuracy_score(y_test, y_pred_optimized)
f1_optimized = f1_score(y_test, y_pred_optimized, average='weighted')
classification_report_optimized = classification_report(y_test, y_pred_optimized, zero_division=0)

print('Precisión del modelo optimizado: ', accuracy_optimized)
print('F1-score del modelo optimizado: ', f1_optimized)
print('Classification report del modelo optimizado:\n', classification_report_optimized)

# Comparar las precisiones de los modelos
print('Mejora de precisión:', accuracy_optimized - accuracy_default)

# Función para plotear la curva de aprendizaje
def plot_learning_curve(model, X, y):
    train_sizes, train_scores, test_scores = learning_curve(model, X, y, cv=3, n_jobs=-1, 
                                                            train_sizes=np.linspace(0.1, 1.0, 10), 
                                                            scoring='accuracy')
    train_scores_mean = np.mean(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    
    plt.figure(figsize=(8,6))
    plt.plot(train_sizes, train_scores_mean, 'o-', color='b', label='Entrenamiento')
    plt.plot(train_sizes, test_scores_mean, 'o-', color='r', label='Validación')
    plt.xlabel('Tamaño del conjunto de entrenamiento')
    plt.ylabel('Accuracy')
    plt.title('Curva de aprendizaje')
    plt.legend(loc='best')
    plt.show()

# Crear y mostrar la curva de aprendizaje
plot_learning_curve(model_optimized, X, y)
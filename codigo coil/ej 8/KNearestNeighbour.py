from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt
import numpy as np

# Cargar los datos
from sklearn.datasets import load_digits
digits = load_digits()

# Dividir los datos en entrenamiento y prueba
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, random_state=100)

# Entrenar modelos KNN
knn_default = KNeighborsClassifier()
knn_1 = KNeighborsClassifier(n_neighbors=1)
knn_100 = KNeighborsClassifier(n_neighbors=100)

knn_default.fit(X_train, y_train)
knn_1.fit(X_train, y_train)
knn_100.fit(X_train, y_train)

# Obtener las predicciones
y_pred_default = knn_default.predict(X_test)
y_pred_1 = knn_1.predict(X_test)
y_pred_100 = knn_100.predict(X_test)

# Obtener las métricas
from sklearn.metrics import accuracy_score, f1_score, classification_report
print("KNN con configuración por defecto:")
print("Accuracy:", accuracy_score(y_test, y_pred_default))
print("F1-score (weighted):", f1_score(y_test, y_pred_default, average='weighted'))
print(classification_report(y_test, y_pred_default, zero_division=0))

print("KNN con 1 vecino más cercano:")
print("Accuracy:", accuracy_score(y_test, y_pred_1))
print("F1-score (weighted):", f1_score(y_test, y_pred_1, average='weighted'))
print(classification_report(y_test, y_pred_1, zero_division=0))

print("KNN con 100 vecinos más cercanos:")
print("Accuracy:", accuracy_score(y_test, y_pred_100))
print("F1-score (weighted):", f1_score(y_test, y_pred_100, average='weighted'))
print(classification_report(y_test, y_pred_100, zero_division=0))

# Definir función para graficar Learning Curves
def plot_learning_curve(estimator, title, X, y, ylim=None, cv=None,
                        n_jobs=None, train_sizes=np.linspace(.1, 1.0, 5)):
    plt.figure()
    plt.title(title)
    if ylim is not None:
        plt.ylim(*ylim)
    plt.xlabel("Training examples")
    plt.ylabel("Score")
    train_sizes, train_scores, test_scores = learning_curve(
        estimator, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes)
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    plt.grid()
    plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std, alpha=0.1,
                     color="r")
    plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                     test_scores_mean + test_scores_std, alpha=0.1, color="g")
    plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
             label="Training score")
    plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
             label="Cross-validation score")
    plt.legend(loc="best")
    return plt

# Grafos

import networkx as nx

# Creamos un grafo vacío
G = nx.Graph()

# Agregamos los nodos
G.add_nodes_from(range(1, 6))

# Agregamos las aristas
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 4)
G.add_edge(2, 5)
G.add_edge(3, 4)
G.add_edge(4, 5)

# Dibujamos el grafo
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')

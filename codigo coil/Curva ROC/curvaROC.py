import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

# Con esto buscamos que tan certeras seran las predicciones de nuestro modelo

# Cargar el csv
df = pd.read_csv('codigo coil/clusterizado_1.csv', sep=';')

# Definir la variable objetivo (Cluster 0 o no)
df['target'] = df['cluster'].apply(lambda x: 1 if x == 0 else 0)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(df[['dia', 'LAEQ']], df['target'], test_size=0.3, random_state=42)

# Entrenar un modelo de regresión logística
lr = LogisticRegression(random_state=42)
lr.fit(X_train, y_train)

# Generar la curva ROC y calcular el AUC
y_pred_proba = lr.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
auc = roc_auc_score(y_test, y_pred_proba)

# Graficar la curva ROC
plt.plot(fpr, tpr)
plt.title('Curva ROC')
plt.xlabel('Tasa de Falsos Positivos')
plt.ylabel('Tasa de Verdaderos Positivos')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.plot([0, 1], [0, 1], 'k--')
plt.text(0.5, 0.3, 'AUC = {:.2f}'.format(auc))
plt.show()

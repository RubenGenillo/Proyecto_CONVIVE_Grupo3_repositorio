import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import math
from sklearn.preprocessing import StandardScaler

# Cargar el csv
df = pd.read_csv('codigo coil/NMT3.csv', sep=';')

# Leer el archivo csv y crear un DataFrame de Pandas
data = df[['anio', 'mes', 'dia', 'LAEQ', 'LAS01', 'LAS10', 'LAS50', 'LAS90', 'LAS99', 'tipo_D', 'tipo_E', 'tipo_N', 'tipo_T']]

# Normalizamos los datos para que todas las columnas tengan la misma escala
scaler = StandardScaler()
data_norm = scaler.fit_transform(data)

# Seleccionar el número de clusters y aplucar el algoritmo de clusterización
kmeans = KMeans(n_clusters=3, random_state=0).fit(data_norm)

# Agregar las etiquetas de cluster al DataFrame original
df['cluster'] = kmeans.labels_

#Guardar el DataFrame en un nuevo archivo csv
df.to_csv('codigo coil/clusterizado_3.csv', index=False, sep=';')


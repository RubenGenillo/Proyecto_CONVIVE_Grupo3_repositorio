import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el csv
df = pd.read_csv('codigo coil/clusterizado_1.csv', sep=';')
df2 = pd.read_csv('codigo coil/clusterizado_2.csv', sep=';')
df3 = pd.read_csv('codigo coil/clusterizado_3.csv', sep=';')
df4 = pd.read_csv('codigo coil/clusterizado_4.csv', sep=';')

# Mostrar los clusters en una matriz 2x2 de gráficos, dia frente a LAEQ
fig, axs = plt.subplots(2, 2)

axs[0, 0].scatter(df['dia'], df['LAEQ'], c=df['cluster'])
axs[0, 0].set_title('NMT1')
axs[0, 0].set_xlabel('dia')
axs[0, 0].set_ylabel('LAEQ')

axs[0, 1].scatter(df2['dia'], df2['LAEQ'], c=df2['cluster'])
axs[0, 1].set_title('NMT2')
axs[0, 1].set_xlabel('dia')
axs[0, 1].set_ylabel('LAEQ')

axs[1, 0].scatter(df3['dia'], df3['LAEQ'], c=df3['cluster'])
axs[1, 0].set_title('NMT3')
axs[1, 0].set_xlabel('dia')
axs[1, 0].set_ylabel('LAEQ')

axs[1, 1].scatter(df4['dia'], df4['LAEQ'], c=df4['cluster'])
axs[1, 1].set_title('NMT4')
axs[1, 1].set_xlabel('dia')
axs[1, 1].set_ylabel('LAEQ')

plt.show()
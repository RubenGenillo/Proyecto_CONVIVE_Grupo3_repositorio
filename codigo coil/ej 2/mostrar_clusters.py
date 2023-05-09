import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el csv
df = pd.read_csv('codigo coil/clusterizado_1.csv', sep=';')

# Gráfico de dispersión
fig, axs = plt.subplots(2, 2)

for i, ax in enumerate(axs.flatten()):
    if i+1 > 4: break  # en caso de haber más de 4 archivos
    dftemp = pd.read_csv(f'codigo coil/clusterizado_{i+1}.csv', sep=';')
    ax.scatter(dftemp['dia'], dftemp['LAEQ'], c=dftemp['cluster'])
    ax.set_title(f'NMT{i+1}')
    ax.set_xlabel('dia')
    ax.set_ylabel('LAEQ')

    # Línea de regresión
    x = dftemp['dia']
    y = dftemp['LAEQ']
    coeffs = np.polyfit(x, y, 1)
    poly_eqn = np.poly1d(coeffs)
    ax.plot(x, poly_eqn(x), color='red')

    # Coeficiente de correlación
    corr = np.corrcoef(x, y)[0, 1]
    ax.text(0.05, 0.95, f'Corr: {corr:.2f}', transform=ax.transAxes, ha='left', va='top')

plt.show()

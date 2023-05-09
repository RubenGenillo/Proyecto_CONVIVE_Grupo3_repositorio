#eliminar los csv NMTx

import os
import config as cfg
import pandas as pd

# Cargar el csv
df = pd.read_csv(cfg.DATABASE_PATH, sep=';')

#Eliminar los ficheros NMT del 1 al 86

for i in range(1, 87):
    os.remove('codigo coil/NMT' + str(i) + '.csv')
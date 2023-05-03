import pandas as pd
import config as cfg

# Cargar el csv
df = pd.read_csv(cfg.DATABASE_PATH, sep=';')

# Separar el fichero en otros ficheros en funcion del NMT, numeros de 1 a 86 que esten en la columna NMT
for i in range(1, 87):
    df[df['NMT'] == i].to_csv('codigo coil/NMT' + str(i) + '.csv', index=False, sep=';') if not df[df['NMT'] == i].empty else None

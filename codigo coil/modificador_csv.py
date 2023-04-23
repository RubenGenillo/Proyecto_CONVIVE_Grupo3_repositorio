from sklearn.preprocessing import OneHotEncoder
import pandas as pd

df = pd.read_csv('Ruido_diario_acumulado.csv', sep=';')

ohe = OneHotEncoder()
resultado_ohe = ohe.fit_transform(df[['tipo']])
columnas_ohe = ohe.get_feature_names_out(['tipo'])
df_ohe = pd.DataFrame(resultado_ohe.toarray(), columns=columnas_ohe)

df_modificado = pd.concat([df, df_ohe], axis=1).drop(['tipo'], axis=1)

# Agregar una columna de ID
df_modificado.insert(0, 'ID', range(1, 1+len(df_modificado)))

# Guardar el csv modificado con la columna de ID
df_modificado.to_csv('Ruido_diario_acumulado_modificado.csv', index=False)
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

df = pd.read_csv('codigo coil/Ruido_diario_acumulado.csv', sep=';')
df = df.replace(',', '.', regex=True)

ohe = OneHotEncoder()
resultado_ohe = ohe.fit_transform(df[['tipo']])
columnas_ohe = ohe.get_feature_names_out(['tipo'])
df_ohe = pd.DataFrame(resultado_ohe.toarray(), columns=columnas_ohe)

df_modificado = df.join(df_ohe, rsuffix='_ohe').drop(['tipo'], axis=1)

# Agregar una columna de ID
df_modificado.insert(0, 'ID', range(1, 1+len(df_modificado)))

print(df.isna().any().sum())
print(df.isnull().any().sum())
# Guardar el csv modificado con la columna de ID
df_modificado.to_csv('codigo coil/Ruido_diario_acumulado_id_modificado.csv', sep=';', index=False)
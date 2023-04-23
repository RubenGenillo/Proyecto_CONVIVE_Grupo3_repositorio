from sklearn.preprocessing import OneHotEncoder
import pandas as pd

df = pd.read_csv('codigo coil/Ruido_diario_acumulado.csv', sep = ';')

ohe = OneHotEncoder()

resultado_ohe = ohe.fit_transform(df[['tipo']])
columnas_ohe = ohe.get_feature_names_out(['tipo'])
df_ohe = pd.DataFrame(resultado_ohe.toarray(), columns=columnas_ohe)

df_aux = pd.concat([df, df_ohe], axis=1)

df_fin = df_aux.drop(['tipo'], axis=1)

df_fin.to_csv('codigo coil/Ruido_diario_acumulado_modificado.csv', index=False)

print(df_fin)
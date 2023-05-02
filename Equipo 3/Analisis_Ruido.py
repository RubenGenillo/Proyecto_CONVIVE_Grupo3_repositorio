import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
df_ruido=pd.read_csv("DatosRuidocomas.csv")


print("Tabla de datos Ruido:") 
print(df_ruido)
#Identifica los datos NaN o no validos o valores nulos/NO EXISTENTES. El resultado lo suma por columna
print(df_ruido.isna().sum()) 
print("El resultado de datos no validos en la columna LAEQ es:",df_ruido["LAEQ"].isna().sum()) #Suma los datos no validos de la columna "LAEQ"
print("El resultado de datos no validos en la columna 'tipo' es:",df_ruido["tipo"].isna().sum()) #Suma los datos no validos de la columna "tipo"

# #Mostrar los valores nulos para cada campo // NO EXISTEN
# valor_nulo=df_ruido["LAEQ"][df_ruido["LAEQ"].isna()]
# print(valor_nulo)

#Crear grafica de barras
conteo_anio = df_ruido["anio"].value_counts()
print("Conteo de Mediciones por año:")
print(conteo_anio)
print("El año en el que se tuvieron mas mediciones conto con:",conteo_anio.max(),"(2022), mientras que con menos mediciones se encuentra el periodo de medicion actual con:",conteo_anio.min())

#Conteo de mediciones por estacion
conteo_estacion = df_ruido["NMT"].value_counts()
print("Conteo de Mediciones por Estacion:")
print(conteo_estacion)
#Grafica de Conteo de Mediciones por estacion 
conteo_estacion.plot(kind="bar")
plt.xlabel("NMT(Número de estacion de medida)")
plt.ylabel("Conteo")
plt.title("CONTEO MEDICIONES POR ESTACION")
plt.show()

##Grafica de tipo D con respecto a sus valores en LAEQ
conteo_tipoD = df_ruido[(df_ruido['tipo'] == 'D')]
print("Conteo de Tipo:")
print(conteo_tipoD)
conteo_tipoD_Niveles = conteo_tipoD['LAEQ']
plt.hist(conteo_tipoD_Niveles)
plt.title('Histograma de Tipo D con respecto a sus valores en LAEQ')
plt.xlabel('LAEQ')
plt.ylabel('Frecuencia')
plt.show()

##Grafica de tipo D con respecto a sus valores en LAEQ
conteo_tipoD = df_ruido[df_ruido['tipo'] == 'D']
longitud_D = len(conteo_tipoD)
fig, ax = plt.subplots()
plt.title('Grafica de aparciones de D y sus valores en LAEQ')
ax.plot(range(0, longitud_D), conteo_tipoD["LAEQ"])
plt.show()



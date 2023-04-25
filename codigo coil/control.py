import pandas as pd 
import config as cfg

# Cargar el csv
df = pd.read_csv(cfg.DATABASE_PATH, sep=';')

def añadir_fila(NMT, anio, mes, dia, LAEQ, LAS01, LAS10, LAS50, LAS90, LAS99, tipo_D, tipo_E, tipo_N, tipo_T):
    new_id = df['ID'].max() + 1
    nueva_fila = {'ID': new_id, 'NMT': NMT, 'anio': anio, 'mes': mes, 'dia': dia, 'LAEQ': LAEQ,
                  'LAS01': LAS01, 'LAS10': LAS10, 'LAS50': LAS50, 'LAS90': LAS90, 'LAS99': LAS99,
                  'tipo_D': tipo_D, 'tipo_E': tipo_E, 'tipo_N': tipo_N, 'tipo_T': tipo_T}
    df.loc[new_id] = nueva_fila
    df.to_csv(cfg.DATABASE_PATH, index=False, sep=';')

def eliminar_fila(ID):
    df = pd.read_csv(cfg.DATABASE_PATH, sep=';')
    df = df[df['ID'] != ID]
    df.to_csv(cfg.DATABASE_PATH, index=False)

def eliminar_filas(IDs):
    for id in IDs:
        eliminar_fila(id)

def eliminar_ultima_fila():
    df = pd.read_csv(cfg.DATABASE_PATH, sep=';')
    df = df.drop(df.tail(1).index)
    df.to_csv(cfg.DATABASE_PATH, index=False)

def modificar_fila(ID, NMT, anio, mes, dia, LAEQ, LAS01, LAS10, LAS50, LAS90, LAS99, tipo_D, tipo_E, tipo_N, tipo_T):
    df = pd.read_csv(cfg.DATABASE_PATH, sep=';')
    df.loc[ID, 'NMT'] = NMT
    df.loc[ID, 'anio'] = anio
    df.loc[ID, 'mes'] = mes
    df.loc[ID, 'dia'] = dia
    df.loc[ID, 'LAEQ'] = LAEQ
    df.loc[ID, 'LAS01'] = LAS01
    df.loc[ID, 'LAS10'] = LAS10
    df.loc[ID, 'LAS50'] = LAS50
    df.loc[ID, 'LAS90'] = LAS90
    df.loc[ID, 'LAS99'] = LAS99
    df.loc[ID, 'tipo_D'] = tipo_D
    df.loc[ID, 'tipo_E'] = tipo_E
    df.loc[ID, 'tipo_N'] = tipo_N
    df.loc[ID, 'tipo_T'] = tipo_T
    df.to_csv(cfg.DATABASE_PATH, index=False, sep=";")

def mostrar_fila(ID):
    #Si no muestra la siguiente a la que se busca, restar 1 a la ID
    ID = ID - 1
    df = pd.read_csv(cfg.DATABASE_PATH, sep=';')
    print(df.loc[ID])

def main():
    #Mostrar fila 1
    mostrar_fila(1)
    #Añadir fila
    # añadir_fila(3, 2014, 1, 1, 57.4, 66.6, 61.1, 54.3, 49.1, 45.1, 1.0, 0.0, 0.0, 0.0)
    # eliminar_ultima_fila()
    # eliminar_fila(393252)
    #Modificar fila 1
    # modificar_fila(1, 3, 2014, 1, 1, 57.4, 66.6, 61.1, 54.3, 49.1, 45, 0.0, 0.0, 0.0, 1.0)
    # mostrar_fila(1)

if __name__ == '__main__':
    main()
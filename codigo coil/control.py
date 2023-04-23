import pandas as pd 
import config as cfg

# Cargar el csv
df = pd.read_csv(cfg.DATABASE_PATH, sep=',')

class Informacion:
    def __init__(self, ID, NMT, mes, dia, año, LAEQ, LAS01, LAS10, LAS50, LAS90, LAS99, tipo_D, tipo_E, tipo_N, tipo_T):
        self.ID = ID
        self.NMT = NMT
        self.mes = mes
        self.dia = dia
        self.año = año
        self.LAEQ = LAEQ
        self.LAS01 = LAS01
        self.LAS10 = LAS10
        self.LAS50 = LAS50
        self.LAS90 = LAS90
        self.LAS99 = LAS99
        self.tipo_D = tipo_D
        self.tipo_E = tipo_E
        self.tipo_N = tipo_N
        self.tipo_T = tipo_T

    def __str__(self):
        return f"ID: {self.ID}, NMT: {self.NMT}, mes: {self.mes}, dia: {self.dia}, año: {self.año}, LAEQ: {self.LAEQ}, LAS01: {self.LAS01}, LAS10: {self.LAS10}, LAS50: {self.LAS50}, LAS90: {self.LAS90}, LAS99: {self.LAS99}, tipo_D: {self.tipo_D}, tipo_E: {self.tipo_E}, tipo_N: {self.tipo_N}, tipo_T: {self.tipo_T}"
    
    def to_dict(self):
        return {
            'ID': self.ID,
            'NMT': self.NMT,
            'mes': self.mes,
            'dia': self.dia,
            'año': self.año,
            'LAEQ': self.LAEQ,
            'LAS01': self.LAS01,
            'LAS10': self.LAS10,
            'LAS50': self.LAS50,
            'LAS90': self.LAS90,
            'LAS99': self.LAS99,
            'tipo_D': self.tipo_D,
            'tipo_E': self.tipo_E,
            'tipo_N': self.tipo_N,
            'tipo_T': self.tipo_T
        }
    

def añadir_fila(NMT, mes, dia, año, LAEQ, LAS01, LAS10, LAS50, LAS90, LAS99, tipo_D, tipo_E, tipo_N, tipo_T):
    nueva_fila = Informacion(NMT, mes, dia, año, LAEQ, LAS01, LAS10, LAS50, LAS90, LAS99, tipo_D, tipo_E, tipo_N, tipo_T)
    df = pd.read_csv(cfg.DATABASE_PATH, sep=',')
    df = df.append(nueva_fila.to_dict(), ignore_index=True)
    df.to_csv(cfg.DATABASE_PATH, index=False)

def eliminar_fila(ID):
    df = pd.read_csv(cfg.DATABASE_PATH, sep=',')
    df = df.drop(ID)
    df.to_csv(cfg.DATABASE_PATH, index=False)

def modificar_fila(ID, NMT, mes, dia, año, LAEQ, LAS01, LAS10, LAS50, LAS90, LAS99, tipo_D, tipo_E, tipo_N, tipo_T):
    df = pd.read_csv(cfg.DATABASE_PATH, sep=',')
    df.loc[ID, 'NMT'] = NMT
    df.loc[ID, 'mes'] = mes
    df.loc[ID, 'dia'] = dia
    df.loc[ID, 'año'] = año
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
    df.to_csv(cfg.DATABASE_PATH, index=False)

def mostrar_fila(ID):
    #Si no muestra la siguiente a la que se busca, restar 1 a la ID
    ID = ID - 1
    df = pd.read_csv(cfg.DATABASE_PATH, sep=',')
    print(df.loc[ID])

def main():
    #Mostrar fila 200
    mostrar_fila(200)

if __name__ == '__main__':
    main()
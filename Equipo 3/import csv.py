import csv
import pandas as pd

# Abrir y leer el archivo
with open('R.txt', 'r') as f:
    text = f.read()

# Escribir el archivo como csv
with open('datosRuido.csv', 'w', newline='') as f:
    f.write(text)

# Separar los valores por punto y coma (;)
with open('datosRuido.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    rows = list(reader)

# Escribir resultado en un nuevo archivo separado por comas
with open('DatosRuidocomas.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    for row in rows:
        writer.writerow(row)
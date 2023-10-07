"""
import csv
import json

# Leer el archivo CSV
with open('datos_totales.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Inicializar variables
    encabezados = []
    datos = []
    fila_actual = {}
    
    # Iterar a través de las filas del archivo CSV
    for fila in csv_reader:
        if not fila:  # Salta filas vacías
            continue
        
        if ':' in fila[0]:
            # Si la fila contiene un ':' en el primer elemento, es un encabezado
            encabezado = fila[0].strip(':')
            encabezados.append(encabezado)
            
            if fila_actual:
                # Agregar la fila actual al conjunto de datos
                datos.append(fila_actual)
                fila_actual = {}
        else:
            # Si no es un encabezado, agrega la fila al diccionario fila_actual
            fila_actual[encabezados[-1]] = fila[0]
    
    # Agregar la última fila actual al conjunto de datos
    if fila_actual:
        datos.append(fila_actual)

# Guardar los datos en un archivo JSON
with open('datosnew.json', 'w', encoding='utf-8') as json_file:
    json.dump(datos, json_file, ensure_ascii=False, indent=4)

print("Los datos se han guardado en 'datos.json'")
"""


import csv
import json

# Nombre de los archivos de entrada y salida
csv_file = 'datos_totales.csv'
json_file = 'salida.json'

# Leer el archivo CSV y convertirlo a una lista de diccionarios
data = []
with open(csv_file, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',')
    for row in csvreader:
        data.append(row)

# Escribir los datos en formato JSON en un archivo
with open(json_file, 'w') as jsonfile:
    json.dump(data, jsonfile, indent=4)

print(f"Se ha convertido el archivo CSV '{csv_file}' a JSON '{json_file}'.")

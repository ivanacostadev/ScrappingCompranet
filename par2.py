
"""
from bs4 import BeautifulSoup
import csv

# Leer el archivo HTML
with open('PC-2023-00001389.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Encuentra todas las etiquetas <label> en el HTML
etiquetas_label = soup.find_all('label')

# Crear una lista de listas para almacenar los datos
datos_csv = []

# Extraer el texto de cada etiqueta <label> y agregarlo a la lista de datos_csv
for etiqueta in etiquetas_label:
    texto = etiqueta.text.strip()  # Eliminar espacios en blanco al principio y al final
    datos_csv.append([texto])

# Escribir los datos en un archivo CSV
with open('datos.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(datos_csv)

print("Los datos se han guardado en 'datos.csv'")
"""

from bs4 import BeautifulSoup
import csv
import os

# Crear una lista para almacenar los datos de todas las páginas
datos_totales = []

# Obtener la lista de archivos HTML en el directorio
archivos_html = [archivo for archivo in os.listdir('.') if archivo.endswith('.html')]

for archivo_html in archivos_html:
    with open(archivo_html, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Encuentra todas las etiquetas <label> en el HTML
    etiquetas_label = soup.find_all('label')
    
    # Crear una lista para almacenar los datos de esta página
    datos_pagina = []
    
    # Extraer el texto de cada etiqueta <label> y agregarlo a la lista de datos_pagina
    for etiqueta in etiquetas_label:
        texto = etiqueta.text.strip()  # Eliminar espacios en blanco al principio y al final
        datos_pagina.append(texto)
    
    datos_totales.append(datos_pagina)

# Escribir los datos en un archivo CSV
with open('datos_totales.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(datos_totales)

print("Los datos se han guardado en 'datos_totales.csv'")

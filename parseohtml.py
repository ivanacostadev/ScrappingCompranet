
from bs4 import BeautifulSoup

with open('PC-2023-00001389.html', 'r', encoding='utf-8') as file:
    html_content = file.read()


soup = BeautifulSoup(html_content, 'html.parser')

# Encuentra todas las etiquetas <p> en el HTML
datos = soup.find_all('label')

# Imprime el texto de cada etiqueta <p>
for p in datos:
    print(p.text)

"""

import json
from bs4 import BeautifulSoup

with open('PC-2023-00001389.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Encuentra todas las etiquetas <label> en el HTML
datos = soup.find_all('label')

# Crear una lista para almacenar los valores de p.text
data_list = []

# Agregar cada valor de p.text a la lista
for p in datos:
    data_list.append(p.text.strip())

# Convertir la lista en una cadena JSON
json_data = json.dumps(data_list, indent=4, ensure_ascii=False)

# Imprimir la cadena JSON
print(json_data)

# Opcionalmente, guardar la cadena JSON en un archivo
with open('output.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)


###################
import json
from bs4 import BeautifulSoup

# Abrir y leer el archivo HTML
with open('PC-2023-00001389.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Crear el objeto BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Encuentra todas las etiquetas <label> en el HTML
datos = soup.find_all('label')

# Crear una lista para almacenar los datos como diccionarios
data_list = []

# Iterar sobre las etiquetas <label> en pasos de dos
for i in range(0, len(datos), 2):
    if i + 1 < len(datos):  # Verificar si hay suficientes elementos
        cabecera = datos[i].text.strip()
        contenido = datos[i + 1].text.strip()

        # Crear un diccionario con la cabecera y el contenido
        data_dict = {
            'cabecera': cabecera,
            'contenido': contenido
        }

        # Agregar el diccionario a la lista
        data_list.append(data_dict)

# Convertir la lista de diccionarios en una cadena JSON
json_data = json.dumps(data_list, indent=4, ensure_ascii=False)

# Imprimir la cadena JSON
print(json_data)

# Opcionalmente, guardar la cadena JSON en un archivo
with open('outputin.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)


"""

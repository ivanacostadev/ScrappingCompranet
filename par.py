from bs4 import BeautifulSoup
import json

with open('PC-2023-00001389.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Find all label tags in the HTML
datos = soup.find_all('label')

# Create a dictionary to store the extracted data
data_dict = {}

# Iterate through the label tags and extract the desired information
for label in datos:
    label_text = label.text.strip()
    if ':' in label_text:
        label_name, label_value = label_text.split(':', 1)
        data_dict[label_name.strip()] = label_value.strip()
    else:
        print(f"Label text without colon: {label_text}")
# Define the list of keys you want to include in the JSON
desired_keys = [
    "Código del expediente",
    "Código del proyecto de convocatoria",
    "Estatus del proyecto de convocatoria",
    "Dependencia o Entidad",
    "Ramo",
    "Unidad compradora",
    "Responsable de la captura",
    "Correo electrónico unidad compradora",
    "Código del proyecto de convocatoria",
    "Referencia / Número de control interno",
    "Nombre del proyecto de convocatoria",
    "Descripción detallada del proyecto de convocatoria",
    "Ley que rige la contratación",
    "Tipo de procedimiento de contratación",
    "Entidad Federativa donde se llevará a cabo la contratación",
    "Año del ejercicio presupuestal",
    "Procedimiento exclusivo para MIPYMES",
    "Fecha y hora límite para recepción de comentarios",
    "Reunión pública de revisión del proyecto (art.35 fr. III del RLOPSRM",
    "Plazo del procedimiento de contratación",
    "Fecha estimada del inicio del contrato",
    "Participación de Testigo Social",
    "Tipo de contratación",
    "Criterio de evaluación",
    "Medio o forma de participación",
    "Carácter",
    "Idioma(s) de presentación de proposiciones",
    "Anticipo",
    "Porcentaje del anticipo (Deberá entregar una garantía por el 100% del anticipo)",
    "Caso fortuito o fuerza mayor",
    "Moneda",
    "¿Permite participación conjunta?",
    "Subcontratación de partes de los trabajos",
    "Ubicación del sitio o sitios de los trabajos",
    "Fecha estimada del inicio de la obra",
    "Plazo de ejecucion en dias naturales",
    "Condiciones de pago en los contratos",
    "Es plurianual",
    "Garantía de cumplimiento",
    "Porcentaje del monto del contrato a garantizar",
    "Garantía sobre obras o servicios y vicios ocultos",
    "Número de meses que debe cumplir la garantía",
    "Otros seguros"
    
]

# Create a new dictionary with only the desired keys
filtered_data = {key: data_dict[key] for key in desired_keys if key in data_dict}

# Save the filtered data as JSON
output_filename = 'output.json'
with open(output_filename, 'w') as json_file:
    json.dump(filtered_data, json_file, ensure_ascii=False, indent=4)

print(f"Filtered data has been saved to {output_filename}")

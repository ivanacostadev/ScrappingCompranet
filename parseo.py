
import pandas as pd
from bs4 import BeautifulSoup
import csv
from csv import writer
import os
import re
import requests
import time
import json
import os
import spacy 
from spacy_download import load_spacy
import nltk
from nltk.corpus import wordnet as wn
import glob
import fnmatch
import shutil




def muevehtmls():
    carpeta_actual = "/Users/yetzihernandez/Desktop/licyserver/"
    # Ruta de la carpeta "HTMLs"
    carpeta_destino = os.path.join(carpeta_actual, "htmlprevio")
    # Crear la carpeta "HTMLs" si no existe
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    # Obtener la lista de archivos en la carpeta actual
    archivos = os.listdir(carpeta_actual)

    for archivo in archivos:
        if archivo.endswith(".html"):
            # Ruta completa del archivo de origen
            ruta_origen = os.path.join(carpeta_actual, archivo)
        
            # Ruta completa del archivo de destino
            ruta_destino = os.path.join(carpeta_destino, archivo)
        
            # Mover el archivo, sobrescribiendo si existe
            shutil.move(ruta_origen, ruta_destino)
            #print(f"Se movió {archivo} a la carpeta 'HTMLs'.")
    print("Se movieron archivos HTML")


def Envia_errores(folio, error):
    url = 'https://lizzi.appsholos.com/api/index_get'
    params = {
        'action': 'envioIncidencias',
        'folio': folio,
        '_pass': 'holoscommsistemasdisruptivos',
        'licitador': 1,
        'error': error,
        'proceso': 'Parseo de HTML'
    }

    try:
        response = requests.get(url, params=params)
        text_respuesta = response.text
        # Aquí puedes hacer algo con la respuesta recibida

        # Finaliza la ejecución del programa
        return
        ## sys.exit()

    except requests.exceptions.RequestException as e:
        print('Error al enviar errores al servicio web:', e)
        # Finaliza la ejecución del programa
        return
        ## sys.exit()


def parseo():
    url = "https://lizzi.appsholos.com/api/folio_nuevo"
    parametros = {
        "id_licitador": 1,
        "_pass": 'holoscommsistemasdisruptivos'
    }
    response = requests.get(url,params=parametros)

    respuestaserver=response.json()
    estatus=respuestaserver.get("estatus")
    textoserver=respuestaserver.get("texto")
    n_folio=respuestaserver.get("parametros")

    if estatus == 0:
        text_error= "Error en la solicitud al webservice: folio_nuevo."
        Envia_errores(0, text_error)
    ######################################==Se genera folio===###########################################
    folio = str(n_folio).zfill(6)

    anexos = folio+'_anexos'+'.csv'
    detalle=folio+'_detalles'+'.csv'
    register_list = []
    anexos_list = []

    nombre_carpetas= fnmatch.filter(os.listdir('.'), '*.html')
    for filehtml in nombre_carpetas:
        nombre_arch = str(filehtml)
        file = open(nombre_arch, encoding='utf-8')
        soup = BeautifulSoup(file, 'html.parser', from_encoding='utf-8')
        caja = soup.find('div', class_='page-header')
        id_licitacion = caja.find('small').get_text()
        id_licitacion = id_licitacion[5:]
        register_list.append(id_licitacion)

        arch = 1
        tablas = pd.read_html(nombre_arch, encoding='utf8', index_col=False)
        
        links_sobrantes = 0
        tabla_detalle = tablas[0]
        list_tabla_detalle = tabla_detalle[1].to_list()

        for atributo in list_tabla_detalle:
            register_list.append(atributo)
   
        with open(detalle, 'a', newline='', encoding='utf8') as f_object:
        
            writer_object = writer(f_object)
            writer_object.writerow(register_list)
            f_object.close()
        register_list.clear()
        

    #DETALLES JSON 
    csv_file_path = "/Users/yetzihernandez/Desktop/licyserver/%s_detalles.csv"%folio
       
    def convert_csv_to_json(csv_file_path):
        json_array = []
        with open(csv_file_path,'r',encoding='utf-8') as csv_file:
            csv_data = csv.reader(csv_file)
            headers = next(csv_data)
            
            for row in csv_data:
                json_obj = {
                    "licitacion_numero": row[0],
                   "licitacion_area_contratante": row[2],
                   "licitacion_entidad": row[3],
                   "licitacion_descripcion": row[4],
                   "licitacion_detalle": row[5],
                   "licitacion_concurso": row[6],
                   "licitacion_tipo": row[7],
                   "licitacion_estado": row[8],
                   "licitacion_testigo": row[9],
                    "licitacion_fecha": row[10],
                  "licitacion_adjudicado"  : row[11],
                   "licitacion_monto_adj": row[12],
                   "licitacion_tipo_moneda": row[13],
                   "licitacion_tipo_cambio": row[14],
                   "licitacion_monto_adj_pesos_mexicanos": row[15],
                   "licitacion_keywords": row[16]
                }
                json_array.append(json_obj)
                

        json_data = json.dumps(json_array, indent=4)
        return json_data
    
    detalles_json = convert_csv_to_json(csv_file_path)
    #print(detalles_json)
    






    flagdetalles=0
    flaganexos=0
    flagproceso=0

    text_error= "Se inicio proceso de Parseo"
    Envia_errores(folio, text_error)

    url = 'https://lizzi.appsholos.com/Api/index_post'

    data = {
        'detalles': detalles_json,
        'folio': folio
    }
    # Convert the data to JSON format
    json_data = json.dumps(data)
    


    # Set the headers
    headers = {'Content-Type': 'application/json'}

    # Make the POST request with JSON data and headers
    response = requests.post(url, data=json_data, headers=headers)

    r1=response.status_code

    if r1 == 200:
        flagdetalles=1
        print(response.text)
    else:
        flagdetalles=2
        print('Request Error:', response.status_code)
        print(response.text)
        print("Error detalles")
        text_error= "Error en envio de detalles"
        Envia_errores(folio, text_error)

        muevehtmls()




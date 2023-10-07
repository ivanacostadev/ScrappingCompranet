from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import date
from datetime import timedelta
from dateutil import parser
from bs4 import BeautifulSoup
import os 

"""
#Params
proceso
leydecontratacion
tipocontratacion
tipoprocedimento
"""

def iniciar(proceso,ley,tipocontrata,tipoproc,dias):
    #Calculo de dias hacia atras
    hoyendia=datetime.now()
    hoy=hoyendia.strftime("%d-%m-%Y")
    diasrestar=dias
    fecharesta=hoyendia - timedelta(days=diasrestar)
    fecharesultante=fecharesta.strftime("%d-%m-%Y")

    #URL CONFIG
    weburl="https://upcp-compranet.hacienda.gob.mx/sitiopublico/#/"
    rutachromedriver="/Users/yetzihernandez/Desktop/scrappingcn/chromedriver_mac64"
    driver = webdriver.Chrome(rutachromedriver)
    driver.get(weburl)

    time.sleep(5)

    
    #PROCESO
    wait = WebDriverWait(driver, 10)
    dropdown_element = wait.until(EC.visibility_of_element_located((By.NAME, 'proceso')))
    # Hacer clic en el elemento
    dropdown_element.click()

    xpath_expression=f"//li[@aria-label='{proceso}']"
    dropdown_item = wait.until(EC.visibility_of_element_located((By.XPATH, xpath_expression)))
    dropdown_item.click()
    time.sleep(5)


    #LEY QUEN RIGE LA CONTRATACION
    dropdown_element2 = wait.until(EC.visibility_of_element_located((By.NAME, 'ley')))
    dropdown_element2.click()
    xpath_expression=f"//li[@aria-label='{ley}']"
    dropdown_item2 =wait.until(EC.visibility_of_element_located((By.XPATH, xpath_expression)))
    dropdown_item2.click()
    time.sleep(5)

    #TIPO DE CONTRATACION
    dropdown_element3=wait.until(EC.visibility_of_element_located((By.NAME, 'contratacion')))
    dropdown_element3.click()
    time.sleep(5)
    xpath_expression=f"//li[@aria-label='{tipocontrata}']"
    dropdown_item3=wait.until(EC.visibility_of_element_located((By.XPATH, xpath_expression)))
    dropdown_item3.click()
    time.sleep(5)

    #PORCEDIMIENTO
    dropdown_element4=wait.until(EC.visibility_of_element_located((By.NAME, 'procedimiento')))
    dropdown_element4.click()
    time.sleep(5)
    xpath_expression=f"//li[@aria-label='{tipoproc}']"
    dropdown_item4 =wait.until(EC.visibility_of_element_located((By.XPATH, xpath_expression)))
    dropdown_item4.click()
    time.sleep(5)

   
    #FILTROS
    filtro_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//p-button[@label='Filtros']")))
    filtro_button.click()
    fechadesde=wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='fechaDesdeP']")))
    fechadesde.send_keys(hoy)
    fechahasta=wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='fechaHastaP']")))
    fechahasta.send_keys(fecharesultante)
    time.sleep(5)
    
    #BUSCAR

    buscar_button =wait.until(EC.visibility_of_element_located((By.XPATH, "//p-button[@label='Buscar']")))
    buscar_button.click()
    time.sleep(25)


    filas = driver.find_elements(By.XPATH, "//tbody[@class='p-datatable-tbody']/tr")

    # Iterar sobre las filas y abrir cada elemento
    for i, fila in enumerate(filas, start=1):
        numero_identificacion = fila.find_element(By.XPATH, ".//td[@class='p-link2']").text
        print(f"Abriendo elemento {i}: {numero_identificacion}")
        
        # Hacer clic en el enlace para abrir los detalles
        fila.find_element(By.XPATH, ".//td[@class='p-link2']").click()
        
        # Esperar un breve tiempo para asegurarse de que la página se cargue correctamente
        time.sleep(10)
        
        # Obtener el contenido de la página
        contenido_html = driver.page_source
        
        # Guardar el contenido HTML en un archivo individual
        with open(f"contenido_{numero_identificacion}.html", "w", encoding="utf-8") as file:
            file.write(contenido_html)
        
        # Regresar a la página anterior
        driver.back()

    # Cerrar el navegador
    driver.quit()

    print("Contenido HTML guardado exitosamente.")


"""
    elementos_identificacion = driver.find_elements(By.CLASS_NAME, "p-link2")

    # Lista para almacenar los números de identificación
    numeros_identificacion = []

    for elemento_identificacion in elementos_identificacion:
        # Obtén el número de identificación
        numero_identificacion = elemento_identificacion.text
        numeros_identificacion.append(numero_identificacion)

        # Itera sobre los números de identificación y realiza el proceso de clic y guardado
    for numero_identificacion in numeros_identificacion:
        try:
            # Encuentra el elemento con el número de identificación específico
            elemento_identificacion = driver.find_element(By.XPATH, f'//td[@class="p-link2" and contains(text(), "{numero_identificacion}")]')

            # Abre el elemento en una nueva ventana utilizando JavaScript
            driver.execute_script("arguments[0].setAttribute('target', '_blank');", elemento_identificacion)
            
            # Haz clic en el elemento de identificación para abrirlo en una nueva ventana
            elemento_identificacion.click()

            # Cambia el control del driver a la nueva ventana abierta
            driver.switch_to.window(driver.window_handles[1])

            # Espera a que el contenido se cargue (ajusta el tiempo según sea necesario)
            driver.implicitly_wait(45)

            # Obtén el HTML del elemento expandido
            html = driver.page_source

            # Guarda el HTML en un archivo con el nombre del número de identificación
            archivo_nombre = f'{numero_identificacion}.html'
            with open(archivo_nombre, 'w', encoding='utf-8') as archivo:
                archivo.write(html)

            print(f"Archivo '{archivo_nombre}' guardado.")

            # Cierra la ventana actual y cambia el control del driver de nuevo a la ventana original
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

        except NoSuchElementException:
            print(f"No se pudo encontrar el elemento con el número de identificación: {numero_identificacion}")

    # Cierra el navegador al final del ciclo
    driver.quit()




  


      #FILTROS
    filtro_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//p-button[@label='Filtros']")))
    filtro_button.click()

"""








from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

# Configurar Firefox para descargar automáticamente los PDF
options = Options()
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir", "D:/python-diario/hackerrank_pdfs")  # Cambia esta ruta a la carpeta donde quieres descargar los PDF
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")

# Inicializar el driver de Firefox
driver = webdriver.Firefox(options=options)

# Abrir la página principal de HackerRank
url = "https://www.hackerrank.com/domains/python"
driver.get(url)

# Esperar a que la página cargue
time.sleep(5)

# Obtener todos los elementos de los problemas
problem_elements = driver.find_elements(By.XPATH, '//h4[@class="challengecard-title"]')

# Lista para guardar los enlaces de los PDFs
pdf_links = []

# Iterar sobre cada problema y descargar el enunciado
for element in problem_elements:
    # Hacer doble clic en el elemento del problema para entrar
    action = ActionChains(driver)
    action.double_click(element).perform()

    # Esperar a que la página del problema cargue
    time.sleep(5)

    # Buscar y obtener el enlace del botón de descarga del PDF
    try:
        download_button = driver.find_element(By.XPATH, '//span[text()="Download problem statement"]/..')
        pdf_link = download_button.get_attribute('href')
        pdf_links.append(pdf_link)
        print(f"Enlace del PDF encontrado: {pdf_link}")
    except Exception as e:
        print(f"No se pudo encontrar el enlace de descarga para el problema: {e}")

    # Volver a la página principal de los problemas
    driver.get(url)
    time.sleep(5)

# Cerrar el navegador
driver.quit()

# Mostrar los enlaces de los PDFs guardados
for link in pdf_links:
    print(link)

from bs4 import BeautifulSoup
import re
from buffer import Buffer
import pandas as pd

# Variables utilizadas para scrapping
name_file = "video_games_max.html"
url_images = 'https://backoffice.max.com.gt/media/catalog/product/'
regex_name_product = r'<a class="relative flex w-full justify-center"[^>]*>\s*<img alt="([^"]+)"'
regex_url_image = rf'({re.escape(url_images)}[^"]+\.(?:jpg|png|jpeg))'

# Limpiar los nombres: eliminar saltos de línea, espacios innecesarios y decodificar HTML
def limpiarData(limpiarDatos, data):

  if limpiarDatos:
    cleaned_products = [re.sub(r'\s+', ' ', product.strip()) for product in data]
    return cleaned_products
  else:
    return data

# Función para explorar datos regex en objeto html
def exploracionData(data_html):
  
  # Banderas para ver resultados
  ver_imagenes = False
  ver_productos = False
  limpiar_data = False
  ver_data = False
  
  # Buscar los nombres de los productos por regex
  if ver_productos:
    name_products = re.findall(regex_name_product, data_html, re.DOTALL)
    name_products = limpiarData(limpiarDatos=limpiar_data, data=name_products)
  
  # Buscar las url de imagenes por regex
  if ver_imagenes:
    # Imágenes
    url_images = re.findall(regex_url_image, data_html)
  
  if ver_productos and ver_imagenes:
    return name_products, url_images
  
  if ver_data:
    print("Hay", len(name_products), "productos:")
    # print(name_products)
    [print(nProduct) for nProduct in name_products]
    print()
    print("Hay", len(url_images), "imágenes:")
    # print(url_images)
    [print(url) for url in url_images]

# Agregar valores a la pila
def detectarTipoContenido(flag, pila, data):
  pila.append(data[0])
  return pila, not(flag)

# Identificar el par de datos (NOMBRE PRODUCTO, URL IMAGEN) del archivo HTML con re
def identifyPairData(data_html):
  
  # exploracionData(data_html)
  buffer = Buffer(entrada=data_html, inicio=0, tamano_buffer=10)
  buffer.execute()
  lexemas = buffer.lexemas
  pila_contenido = []
  contenido = ""
  FLAG_DETECCION = True

  for lex in lexemas:
    contenido += " " +lex
    if FLAG_DETECCION:
      nombres = re.findall(regex_name_product, contenido)
      if len(nombres) > 0:
        # print("Contenido:", contenido, "\nEncontre con contenido anterior: ", nombres[-1])
        pila_contenido, FLAG_DETECCION = detectarTipoContenido(flag=FLAG_DETECCION, pila=pila_contenido, data=nombres)
        contenido = ""
      
    elif not FLAG_DETECCION:
      imagenes = re.findall(regex_url_image, contenido)
      if len(imagenes) > 0:
        # print("\nContenido:", contenido, "\nEncontre con contenido anterior: ", imagenes[-1])
        pila_contenido, FLAG_DETECCION = detectarTipoContenido(flag=FLAG_DETECCION, pila=pila_contenido, data=imagenes)
        contenido = ""
          
  return pila_contenido

def convertir_a_csv(productos, url):
  data = {
    "Productos": productos,
    "Imagenes": url
  }
  df = pd.DataFrame(data)
  df.to_csv("./data/Listado_productos.csv", index = False)

def cargarHTML(name_file):
  
  file_path = f"./src/{name_file}"

  # Abrir el archivo y crear un objeto soup
  with open(file_path, "r", encoding="utf-8") as file:
      
    soup = BeautifulSoup(file, "html.parser")
    html_content = soup.prettify()
    # print(html_content)
    data = identifyPairData(html_content)
    
    if len(data) % 2 == 0: 
        name_products = [data[i] for i in range(len(data)) if i % 2 == 0]
        url_images = [data[i] for i in range(len(data)) if i % 2 != 0]
        
        # Limpiamos la data de nombre para eliminar caracteres que se interpretaron mal en el proceso de scrapping
        name_products_clean = [item.replace("&amp;", "&") for item in name_products]
        convertir_a_csv(name_products_clean, url_images)
        print("Los productos se han guardado en la carpeta 'data'.")
    else:
        print("La cantidad de datos no es par, revisa la estructura de 'data'.")


cargarHTML(name_file=name_file)

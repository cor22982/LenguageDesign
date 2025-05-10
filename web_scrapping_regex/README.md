# Web Scraping con Expresiones Regulares 🧑‍💻🔍

En esta actividad, se utilizó la librería `re` para crear **expresiones regulares** y `BeautifulSoup` para manejar archivos **HTML**. El objetivo fue extraer **nombres de productos** y sus correspondientes **URL de imágenes** desde un archivo HTML descargado en la carpeta `src`. Los datos obtenidos (nombre del producto y URL de la imagen) se almacenaron en un archivo **CSV** dentro de la carpeta `data`.

## 🐍 Entorno

**Lenguaje**: Python

**Versión**: 3.12.3

### Pasos del Proceso

1. **Lectura y Tokenización**: Se utilizó un **buffer** para separar el código HTML en **lexemas** y se omitieron caracteres en blanco con el token `ws`.

2. **Construcción de Cadenas**: Se unieron los lexemas para evaluar si la cadena construida hacía *match* con las expresiones regulares definidas.

3. **Extracción de Datos**:

   - Se buscaron los **nombres de los productos**.
   - Con un **booleano/bandera**, se alternó entre `False` (para indicar que se busca la URL de la imagen correspondiente) y `True` (para continuar con la búsqueda de otro producto).

4. **Asegurando la Correspondencia**:

   - Este proceso asegura que cada **imagen** esté correctamente asociada a su **producto**.

5. **Generación de CSV**: Finalmente, se construyó un archivo **CSV** con los pares de datos (nombre del producto y URL de la imagen), guardado en la carpeta `data`.

## 📜 Instrucciones

1. Clona el repositorio:

   1.1 HTTPS:

    ```bash
    git clone https://github.com/JosueSay/LenguageDesign
    ```

   1.2 SSH:

    ```bash
    git clone git@github.com:JosueSay/LenguageDesign.git
    ```

2. Navega a la carpeta con:

   ```bash
   cd web_scrapping_regex
   ```

3. Crea tu entorno virtual y luego instala las dependencias o simplemente instala las dependencias con:

   ```bash
   pip install -r requirements
   ```

4. Ejecuta el código Python:

   ```bash
   python main.py
   ```

## ⚙️ Modificando el código

Si decides tomarlo como base, puedes descargar otro código fuente usando el comando:

```bash
wget -O <name_file> <url>
```

Descarga el código fuente de la página mencionada, asignándole un nombre, y colócalo en la carpeta `web_scrapping_regex/src`, o ejecuta el comando desde esa carpeta.

En `main.py`, intercambia los regex para buscar el producto y sus imágenes de acuerdo al código HTML que descargues:

```python
name_file = "file.html"
regex_name_product = r'regex_name_product'
regex_url_image = r'regex_url_images'
```

> **Nota:** Cambia el nombre del archivo por el archivo HTML que descargaste.

Si deseas hacer más búsquedas con otras `expresiones regulares`, puedes editar el comportamiento de `FLAG_DETECCION` para buscar otros elementos además del nombre del producto y su URL de imagen.

## 🎥 Multimedia

### Demostración

[Enlace a demostración en YouTube](https://youtu.be/vYqSOCZqxDY)

### Explicación

[Enlace a explicativo en YouTube](https://youtu.be/qIZ97Qx9ews)

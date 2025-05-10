# Implementación de un Búfer de Entrada 📦

Se simuló un pequeño buffer en Python utilizando centinelas "eof" para identificar el final de los datos. Se recorren los datos con los punteros "inicioLexema" y "avance" en un buffer de tamaño 10 caracteres, recargando los datos para el siguiente buffer y tomando en cuenta los ya leídos.

## 🐍 Entorno

- **Lenguaje:** Python
- **Versión:** 3.12.3

## 📜 Instrucciones

1. **Clonar el repositorio**:

   1.1 HTTPS:

    ```bash
    git clone https://github.com/JosueSay/LenguageDesign
    ```

   1.2 SSH:

    ```bash
    git clone git@github.com:JosueSay/LenguageDesign.git
    ```

2. **Navegar a la carpeta `bufer_entrada`**:

   ```bash
   cd bufer_entrada
   ```

3. **Ejecutar el archivo**:

   ```bash
   python main.py
   ```

4. **Salida esperada**:

   ```text
   Lexema procesado: Esto
   Lexema procesado: es
   Lexema procesado: un
   Lexema procesado: ejemplo
   Lexema procesado: eof
   ```

### Cambiar la entrada

Para probar otro ejemplo de entrada, abre el archivo `main.py` y cambia la cadena de:

```python
entrada = list("Esto es un ejemplo eof")
```

a otra cadena, como por ejemplo:

```python
entrada = list("Esto es otro ejemplo")
```

## 🎥 Multimedia

### Demostración

[Enlace a demostración en YouTube](https://youtu.be/zqwE50POofQ)

### Explicación

[Enlace a explicativo en YouTube](https://youtu.be/Z8z-ykfaNjg)
